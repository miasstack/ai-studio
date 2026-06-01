# Superpowers Reference

This adapts useful ideas from `obra/superpowers` for Unity work in Codex.

## Core Habits

- **Spec before code**: When the request is broad or ambiguous, clarify the desired player outcome, constraints, platform, and acceptance criteria before implementation.
- **Small readable design chunks**: Present compact design sections for approval when building a larger feature or game system.
- **Plan before execution**: Convert approved designs into small tasks with file paths, verification steps, and clear stop conditions.
- **TDD where practical**: For deterministic gameplay logic, data transforms, save/load, economy, inventory, dialogue state, and utility code, prefer red-green-refactor.
- **Unity-aware testing**: Use edit-mode tests for pure logic and play-mode/manual smoke tests for scene, prefab, physics, animation, UI, input, and timing behavior.
- **YAGNI and DRY**: Build the smallest useful version that fits the current feature. Remove duplication when it is real, not hypothetical.
- **Systematic debugging**: Reproduce, isolate, explain root cause, fix the cause, then verify the fix.
- **Evidence over claims**: Do not say a bug is fixed or a feature works without compile/test/editor-console/manual evidence.

## Unity Planning Template

For substantial Unity work:

1. Confirm the gameplay/user outcome.
2. Identify affected Unity surfaces: scripts, scenes, prefabs, ScriptableObjects, UI, assets, packages, project settings.
3. Decide the verification route before editing.
4. Implement in small steps.
5. Run the cheapest meaningful check after each risky step.
6. Do a final verification pass and report evidence.

## Debugging Template

1. Reproduce or inspect the failure evidence.
2. List likely causes and pick the fastest falsifiable one.
3. Instrument or inspect narrowly.
4. Fix the root cause, not just the symptom.
5. Add a regression test or manual smoke check when feasible.
6. Re-run the failing path and check the Unity console.

## Completion Bar

Work is not complete until at least one appropriate verification path has been run or the final response clearly says why verification was not possible.
