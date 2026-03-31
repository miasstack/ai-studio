"""
Async client for the ComfyUI REST + WebSocket API.
"""

import json
import uuid
import aiohttp
import asyncio
from typing import Optional, AsyncIterator


class ComfyClient:
    def __init__(self, host: str = "127.0.0.1", port: int = 8188):
        self.base_url = f"http://{host}:{port}"
        self.ws_url = f"ws://{host}:{port}/ws"
        self.client_id = str(uuid.uuid4())

    # ------------------------------------------------------------------ #
    # Queue / Prompt                                                       #
    # ------------------------------------------------------------------ #

    async def queue_prompt(self, workflow: dict) -> str:
        """Submit a workflow and return the prompt_id."""
        payload = {"prompt": workflow, "client_id": self.client_id}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/prompt", json=payload
            ) as resp:
                resp.raise_for_status()
                data = await resp.json()
                return data["prompt_id"]

    async def get_queue(self) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/queue") as resp:
                resp.raise_for_status()
                return await resp.json()

    async def interrupt(self):
        async with aiohttp.ClientSession() as session:
            await session.post(f"{self.base_url}/interrupt")

    # ------------------------------------------------------------------ #
    # History / Results                                                    #
    # ------------------------------------------------------------------ #

    async def get_history(self, prompt_id: str) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.base_url}/history/{prompt_id}"
            ) as resp:
                resp.raise_for_status()
                return await resp.json()

    async def get_all_history(self) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/history") as resp:
                resp.raise_for_status()
                return await resp.json()

    async def get_image_bytes(
        self, filename: str, subfolder: str = "", img_type: str = "output"
    ) -> bytes:
        params = {"filename": filename, "subfolder": subfolder, "type": img_type}
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.base_url}/view", params=params
            ) as resp:
                resp.raise_for_status()
                return await resp.read()

    # ------------------------------------------------------------------ #
    # System info                                                          #
    # ------------------------------------------------------------------ #

    async def get_system_stats(self) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/system_stats") as resp:
                resp.raise_for_status()
                return await resp.json()

    async def get_object_info(self) -> dict:
        """Returns all available node types and their parameters."""
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/object_info") as resp:
                resp.raise_for_status()
                return await resp.json()

    async def upload_image(self, filename: str, data: bytes) -> str:
        """Upload an image to ComfyUI's input directory. Returns the stored filename."""
        form = aiohttp.FormData()
        form.add_field("image", data, filename=filename, content_type="image/png")
        form.add_field("overwrite", "true")
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}/upload/image", data=form) as resp:
                resp.raise_for_status()
                result = await resp.json()
                return result["name"]

    async def list_loras(self) -> list:
        """Get available LoRA filenames from ComfyUI via object_info."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"{self.base_url}/object_info/LoraLoader",
                    timeout=aiohttp.ClientTimeout(total=10)
                ) as resp:
                    if resp.status != 200:
                        return []
                    data = await resp.json()
                    lora_names = (
                        data.get("LoraLoader", {})
                            .get("input", {})
                            .get("required", {})
                            .get("lora_name", [[]])[0]
                    )
                    return lora_names if isinstance(lora_names, list) else []
        except Exception:
            return []

    async def is_alive(self) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"{self.base_url}/system_stats", timeout=aiohttp.ClientTimeout(total=3)
                ) as resp:
                    return resp.status == 200
        except Exception:
            return False

    # ------------------------------------------------------------------ #
    # WebSocket progress streaming                                         #
    # ------------------------------------------------------------------ #

    async def stream_progress(
        self, prompt_id: str
    ) -> AsyncIterator[dict]:
        """
        Yields progress events until the job is complete.
        Each event is a dict with keys: type, data
        """
        import websockets

        uri = f"{self.ws_url}?clientId={self.client_id}"
        async with websockets.connect(uri) as ws:
            while True:
                try:
                    raw = await asyncio.wait_for(ws.recv(), timeout=120)
                    msg = json.loads(raw)
                    msg_type = msg.get("type")

                    if msg_type == "progress":
                        yield {
                            "type": "progress",
                            "value": msg["data"]["value"],
                            "max": msg["data"]["max"],
                        }
                    elif msg_type == "executing":
                        node = msg["data"].get("node")
                        pid = msg["data"].get("prompt_id")
                        if pid == prompt_id and node is None:
                            # None node means execution finished
                            yield {"type": "done", "prompt_id": prompt_id}
                            return
                        yield {"type": "executing", "node": node}
                    elif msg_type == "execution_error":
                        yield {
                            "type": "error",
                            "message": msg["data"].get("exception_message", "Unknown error"),
                        }
                        return
                except asyncio.TimeoutError:
                    yield {"type": "timeout"}
                    return
