# AI Agent Profiles Index

All agents live in `~/.claude/agents/`. Each is a specialized AI persona with deep expertise.

## Game Development Agents
| Agent | Role |
|-------|------|
| `game-designer` | Game design, mechanics, systems, GDD authoring |
| `gameplay-programmer` | Gameplay code, input systems, player controller |
| `engine-programmer` | Low-level engine work, performance, core systems |
| `lead-programmer` | Technical leadership, architecture decisions |
| `tools-programmer` | Editor tools, pipeline tools, automation |
| `network-programmer` | Multiplayer, netcode, server architecture |
| `ui-programmer` | UI code, HUD systems, menu flow |
| `prototyper` | Rapid prototyping, proof-of-concept builds |

## Unity Specialists
| Agent | Role |
|-------|------|
| `unity-specialist` | General Unity development |
| `unity-ui-specialist` | Unity UI Toolkit, Canvas, UGUI |
| `unity-shader-specialist` | Unity shaders, HLSL, ShaderGraph |
| `unity-dots-specialist` | DOTS, ECS, Jobs, Burst |
| `unity-addressables-specialist` | Addressables, asset bundles, memory |

## Unreal Specialists
| Agent | Role |
|-------|------|
| `unreal-specialist` | General Unreal Engine development |
| `ue-blueprint-specialist` | Blueprint visual scripting |
| `ue-gas-specialist` | Gameplay Ability System |
| `ue-replication-specialist` | Unreal multiplayer replication |
| `ue-umg-specialist` | UMG UI development |

## Godot Specialists
| Agent | Role |
|-------|------|
| `godot-specialist` | General Godot development |
| `godot-gdscript-specialist` | GDScript programming |
| `godot-csharp-specialist` | Godot with C# |
| `godot-gdextension-specialist` | GDExtension/native plugins |
| `godot-shader-specialist` | Godot shaders, visual shaders |

## Art & 3D Agents
| Agent | Role |
|-------|------|
| `art-director` | Visual direction, art style, aesthetic decisions |
| `creative-director` | Creative vision, brand, cross-discipline direction |
| `technical-artist` | Shaders, VFX, art pipeline, optimization |
| `modeler` | 3D modeling, hard surface, organic |
| `animator` | Character animation, rigging-adjacent |
| `texturer` | Texturing, PBR materials, substance |
| `3d-analyst` | 3D asset analysis, quality assessment |
| `asset-optimizer` | Asset optimization, LODs, memory |
| `world-builder` | Environment art, level dressing, world design |
| `vtuber-specialist` | VTuber pipelines, avatar rigging |

## Design & UX Agents
| Agent | Role |
|-------|------|
| `ux-designer` | UX research, wireframes, user flows |
| `level-designer` | Level design, spatial design, pacing |
| `economy-designer` | Game economy, monetization, balance |
| `live-ops-designer` | Live ops, events, retention mechanics |
| `systems-designer` | Game systems, progression, meta |

## Production Agents
| Agent | Role |
|-------|------|
| `producer` | Project management, milestone tracking, scope |
| `release-manager` | Release process, builds, certification |
| `qa-lead` | QA strategy, test planning |
| `qa-tester` | Test execution, bug reporting |
| `accessibility-specialist` | Accessibility standards, inclusive design |
| `localization-lead` | Localization pipeline, i18n, L10n |
| `devops-engineer` | CI/CD, build pipelines, infrastructure |
| `security-engineer` | Security audits, threat modeling |
| `performance-analyst` | Profiling, optimization, benchmarking |

## Narrative & Audio Agents
| Agent | Role |
|-------|------|
| `narrative-director` | Story, dialogue, world lore |
| `writer` | Writing, copy, script |
| `audio-director` | Audio direction, sound design strategy |
| `sound-designer` | Sound effects, audio implementation |

## Analytics & Marketing Agents
| Agent | Role |
|-------|------|
| `analytics-engineer` | Data pipelines, metrics, analytics |
| `community-manager` | Community strategy, social, engagement |
| `ai-programmer` | AI/ML integration, NPC behavior |

## SEO Agents
| Agent | Role |
|-------|------|
| `seo-backlinks` | Link building strategy |
| `seo-cluster` | Topic clustering, content strategy |
| `seo-content` | SEO content writing |
| `seo-drift`, `seo-flow` | SEO workflow tools |
| `seo-geo` | Local/geo SEO |
| `seo-google` | Google Search Console, rankings |
| `seo-schema` | Structured data, schema markup |

## Usage

To use an agent, reference it by name in your request:
- "Act as the `unity-specialist` agent for this..."
- "Use the `game-designer` agent to review this GDD"
- "Have `technical-director` weigh in on this architecture"

Agent files contain full personas, expertise areas, decision frameworks, and communication style.
