# Studio Workflow Reference

This adapts the useful structure of Claude Code Game Studios to Codex without copying its Claude-specific slash-command system.

## Roles To Simulate

Use these lenses as needed:

- **Creative director**: player fantasy, tone, game feel, clarity.
- **Technical director**: architecture, Unity constraints, packages, platform risk.
- **Producer**: scope, milestones, dependencies, what ships now vs later.
- **Game designer**: loop, mechanics, progression, balance.
- **Gameplay programmer**: player systems, AI, combat, interactions.
- **UI/UX designer**: screens, flows, feedback, accessibility.
- **Technical artist**: shaders, VFX, animation, lighting, asset pipeline.
- **QA lead**: test plan, regressions, edge cases, reproduction steps.

## Project Stages

- **Concept**: define player, fantasy, core loop, platform, scope.
- **Prototype**: prove one mechanic with placeholder assets.
- **Vertical slice**: one polished loop with representative art, UI, sound, and progression.
- **Production**: expand content while protecting architecture and performance.
- **Polish**: game feel, UX, onboarding, performance, bugs.
- **Release**: build pipeline, platform checks, save compatibility, QA evidence.

## Feature Slice Template

For medium or large features, produce:

- Goal: what the player can do after the feature lands.
- Scope: included and excluded behavior.
- Unity surfaces: scenes, prefabs, scripts, ScriptableObjects, UI, packages, settings.
- Implementation plan: small steps with verification after each.
- Tests: edit-mode, play-mode, manual smoke, screenshot/video checks.
- Risks: asset dependencies, performance, platform, input, save data, networking.

## QA Gates

- Can a new player understand what to do?
- Does the core loop have feedback for success, failure, and progress?
- Do controls work with the intended input devices?
- Are scene references, prefab overrides, and serialized fields valid?
- Are there console errors or warnings?
- Does the feature survive scene reload, pause/resume, and edge cases?
- Is there a low-cost way to regression test it later?
