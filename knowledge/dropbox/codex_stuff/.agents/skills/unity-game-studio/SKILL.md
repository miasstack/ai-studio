---
name: unity-game-studio
description: Coordinate Unity game development using a combined Codex workflow: Unity MCP live-editor control, TheOne Unity coding standards, App UI skills, and a game-studio production process inspired by Claude Code Game Studios. Use when building, prototyping, debugging, reviewing, planning, testing, or polishing Unity games, especially when the user wants Codex to work inside Unity more effectively.
---

# Unity Game Studio

Use this skill whenever the user asks to build, prototype, fix, review, or plan a Unity game.

## Core Stack

- **Unity MCP**: Prefer live Unity Editor inspection/control when an MCP server is installed and connected.
- **TheOne Unity standards**: Apply `theone-unity-standards` for all Unity C# implementation and review.
- **App UI skills**: Apply `app-ui`, `app-ui-mvvm`, `app-ui-navigation`, `app-ui-redux`, and `app-ui-theming` when building Unity UI.
- **Studio workflow**: Use lightweight director/lead/specialist thinking from `references/studio-workflow.md` for game design, scope, QA, and production gates.
- **Superpowers reasoning**: Use `references/superpowers.md` for spec-first planning, TDD, systematic debugging, and verification-before-completion habits.

## Operating Workflow

1. Identify project state: concept, prototype, existing Unity project, bugfix, polish pass, or release prep.
2. Find the Unity project root. Prefer `ProjectSettings/ProjectVersion.txt`, `Assets/`, and `Packages/manifest.json` over guessing.
3. Read the local project structure before editing. If graphify data exists, follow `AGENTS.md` graphify rules.
4. If Unity MCP is available, inspect the editor/project through MCP before making scene, GameObject, prefab, package, UI, or build changes. See `references/unity-mcp.md`.
5. Keep implementation scoped to the requested game feature. Preserve user edits.
6. Validate with the strongest practical loop: compile, Unity tests, editor console, scene checks, play-mode smoke test, or screenshots.
7. Summarize changed files, test evidence, and remaining risks.

## Unity Implementation Rules

- Use existing project patterns first.
- For runtime C#, load and follow `theone-unity-standards`.
- For UI Toolkit/App UI work, load the relevant App UI skill.
- Prefer proven Unity packages/features for established domains: Input System, Cinemachine, Addressables, NavMesh, Timeline, DOTS/ECS only when the project already uses it or the need is clear.
- Avoid broad architecture rewrites during feature work.
- Avoid hardcoded scene object names unless the project already relies on them; prefer serialized references, ScriptableObjects, dependency injection, or registries.
- Treat prefabs, scenes, Addressables groups, and project settings as high-impact files. Inspect first and verify after edits.

## Quality Gates

Before calling work done, check the gates that fit the request:

- **Design**: core loop, target player, win/loss/fail states, controls, feedback, progression.
- **Code**: compiles, follows project architecture, no new warnings, no unmanaged allocations in hot paths without reason.
- **Unity**: scene/prefab references valid, assets imported, packages resolved, no console errors.
- **Gameplay**: feature can be exercised in editor or a small test scene.
- **UI**: layout works at target resolutions, text fits, controls are discoverable and stateful.
- **Performance**: obvious per-frame allocations, physics overload, asset loading spikes, and Update-heavy scripts are checked.

## Reference Routing

- Read `references/unity-mcp.md` when connecting Unity MCP, using Unity editor tools, or diagnosing MCP setup.
- Read `references/studio-workflow.md` when planning a full game, slicing features, creating milestones, doing QA, or coordinating larger work.
- Read `references/superpowers.md` when the request is broad, ambiguous, bug-focused, or requires multi-step implementation discipline.
