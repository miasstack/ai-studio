# Unity MCP Reference

Use Unity MCP as the live bridge between Codex and the Unity Editor when available.

## Install In Unity

In Unity:

1. Open `Window > Package Manager`.
2. Click `+`.
3. Choose `Add package from git URL...`.
4. Use:

```text
https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#main
```

For beta features, use:

```text
https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#beta
```

## Start And Connect

1. Open `Window > MCP for Unity`.
2. Start the server.
3. Default endpoint:

```text
http://localhost:8080/mcp
```

4. Confirm the client shows connected before relying on editor tools.

## Preferred Tool Use

When tools are available, prefer Unity MCP for:

- Reading project info, scenes, selection, GameObjects, prefabs, components, tags, layers, and packages.
- Creating or editing scripts through Unity-aware tools.
- Managing scenes, GameObjects, components, materials, prefabs, UI, cameras, animation, physics, shaders, textures, VFX, builds, and packages.
- Running Unity tests and reading the editor console.
- Using `batch_execute` for multiple editor operations.
- Using `unity_docs` and `unity_reflect` before depending on uncertain Unity APIs.

## Fallback

If Unity MCP is not installed or not connected:

- Work from the filesystem.
- Use Unity project files and package manifests as source of truth.
- Ask the user to open Unity and start MCP only when live editor state is needed.
- Do not pretend scene or prefab changes were verified in-editor unless they were.

## Safety

- Treat scene, prefab, build settings, package, and project settings edits as high impact.
- Inspect before modifying.
- Prefer additive changes and focused patches.
- Verify editor console after changes when MCP is available.
