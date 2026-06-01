"""
Startup script: registers BlenderMCP addon and starts the socket server.
Run as: blender --python blender_start_mcp.py
"""
import bpy
import sys
import os

addon_path = os.path.expanduser("~/Desktop/blender_mcp_addon.py")

# Install addon from file
bpy.ops.preferences.addon_install(filepath=addon_path, overwrite=True)

# Enable it
addon_name = "blender_mcp_addon"
bpy.ops.preferences.addon_enable(module=addon_name)

# Start the server directly
if hasattr(bpy.types, "blendermcp_server"):
    bpy.types.blendermcp_server.start()
    print("[BlockQuest] BlenderMCP socket server started on localhost:9876")
else:
    # Fallback: call the start operator if panel registered it
    try:
        bpy.ops.blendermcp.start_server()
        print("[BlockQuest] BlenderMCP server started via operator")
    except Exception as e:
        print(f"[BlockQuest] Server start fallback failed: {e}")
        # Manual instantiation
        from blender_mcp_addon import BlenderMCPServer
        server = BlenderMCPServer()
        server.start()
        bpy.types.blendermcp_server = server
        print("[BlockQuest] BlenderMCP server started manually on localhost:9876")

print("[BlockQuest] Blender is ready. Claude can now connect via MCP.")
