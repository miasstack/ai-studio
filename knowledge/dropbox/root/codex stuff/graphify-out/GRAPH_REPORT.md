# Graph Report - codex stuff  (2026-05-12)

## Corpus Check
- 54 files · ~22,890,289 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 723 nodes · 1498 edges · 34 communities detected
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 62 edges (avg confidence: 0.79)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]

## God Nodes (most connected - your core abstractions)
1. `TreasureTownGame` - 94 edges
2. `KidNationGrandPrix` - 43 edges
3. `build_character()` - 18 edges
4. `create_character()` - 16 edges
5. `KidNationRigPrefabBuilder` - 15 edges
6. `build_arjun()` - 13 edges
7. `render()` - 12 edges
8. `paste_center()` - 12 edges
9. `main()` - 11 edges
10. `make_frame()` - 11 edges

## Surprising Connections (you probably didn't know these)
- `ensureDir()` --calls--> `saveFailureScreenshot()`  [INFERRED]
  /Users/damoneden/Documents/codex stuff/generate-a-video/scripts/lib/fs-utils.js → /Users/damoneden/Documents/codex stuff/generate-a-video/scripts/lib/browser.js
- `SearchStore` --uses--> `CreatorRadarHandler`  [INFERRED]
  /Users/damoneden/Documents/codex stuff/creator-radar-mvp/services.py → /Users/damoneden/Documents/codex stuff/creator-radar-mvp/server.py
- `TrendFinderService` --uses--> `CreatorRadarHandler`  [INFERRED]
  /Users/damoneden/Documents/codex stuff/creator-radar-mvp/services.py → /Users/damoneden/Documents/codex stuff/creator-radar-mvp/server.py
- `main()` --calls--> `getArg()`  [INFERRED]
  /Users/damoneden/Documents/codex stuff/generate-a-video/scripts/resume-run.js → /Users/damoneden/Documents/codex stuff/generate-a-video/scripts/lib/browser.js
- `main()` --calls--> `getLatestRunId()`  [INFERRED]
  /Users/damoneden/Documents/codex stuff/generate-a-video/scripts/resume-run.js → /Users/damoneden/Documents/codex stuff/generate-a-video/scripts/lib/run-state.js

## Communities

### Community 0 - "Community 0"
Cohesion: 0.07
Nodes (1): TreasureTownGame

### Community 1 - "Community 1"
Cohesion: 0.03
Nodes (79): dart:convert, dart:math, package:flutter/material.dart, package:flutter/services.dart, package:shared_preferences/shared_preferences.dart, _answer, _BridgeBuildZone, build (+71 more)

### Community 2 - "Community 2"
Cohesion: 0.07
Nodes (44): getArg(), launchBrowserWithSession(), saveFailureScreenshot(), getFfmpegPath(), getPlaywrightOptions(), loadEnvFile(), loadSitesConfig(), parseBoolean() (+36 more)

### Community 3 - "Community 3"
Cohesion: 0.09
Nodes (28): CreatorRadarHandler, ApifyTikTokProvider, _creator_rank(), ensure_data_dir(), _expand_query_terms(), _extract_author(), _extract_created_at(), _extract_hashtags() (+20 more)

### Community 4 - "Community 4"
Cohesion: 0.1
Nodes (4): KidNationGrandPrix, RacerProfile, RacerState, StarPickup

### Community 5 - "Community 5"
Cohesion: 0.17
Nodes (30): add_armature_skeleton(), add_hair(), add_idle_keys(), add_outfit(), add_stage(), add_subsurf(), add_text(), build_character() (+22 more)

### Community 6 - "Community 6"
Cohesion: 0.13
Nodes (28): active_word(), add_word_timings(), audio_features(), decay(), draw_background(), draw_brand(), draw_character_pair(), draw_chorus() (+20 more)

### Community 7 - "Community 7"
Cohesion: 0.17
Nodes (24): active_word(), add_word_timings(), audio_features(), cover(), decay_curve(), draw_brand(), draw_chorus(), draw_hit_bars() (+16 more)

### Community 8 - "Community 8"
Cohesion: 0.23
Nodes (22): add_studio(), add_subsurf(), armature(), build_arjun(), camera(), cube(), curve(), empty() (+14 more)

### Community 9 - "Community 9"
Cohesion: 0.22
Nodes (21): add_clean_face_details(), add_kidnation_clothes(), add_studio(), assign_single_material(), camera(), convert_curves_to_meshes(), cube(), curve_tube() (+13 more)

### Community 10 - "Community 10"
Cohesion: 0.19
Nodes (18): active_word_for_event(), add_word_timings(), audio_features(), bg_frame(), cover_resize(), draw_confetti(), draw_kinetic_lyrics(), draw_paper_rays() (+10 more)

### Community 11 - "Community 11"
Cohesion: 0.26
Nodes (19): add_armature(), add_lighting_and_camera(), add_pose_animation(), CharacterSpec, create_character(), create_cube(), create_cylinder(), create_hair() (+11 more)

### Community 12 - "Community 12"
Cohesion: 0.12
Nodes (11): MonoBehaviour, KidNationRigAnimator, CharacterDef, DistrictClickTarget, DistrictDef, DistrictView, NumberRound, PatternRound (+3 more)

### Community 13 - "Community 13"
Cohesion: 0.35
Nodes (18): art_block_party(), art_crew_lineup(), art_dance_crew(), art_future_builders(), art_heroes(), art_mystery_club(), art_pixel_power(), art_sticker_bomb() (+10 more)

### Community 14 - "Community 14"
Cohesion: 0.24
Nodes (2): CharacterSpec, KidNationRigPrefabBuilder

### Community 15 - "Community 15"
Cohesion: 0.24
Nodes (14): audio_levels(), bg_frame(), cover_resize(), draw_confetti(), draw_kinetic_lyrics(), draw_paper_rays(), font(), make_word() (+6 more)

### Community 16 - "Community 16"
Cohesion: 0.3
Nodes (14): add_studio(), assign(), camera(), convert_generated_curves(), cube(), curve_tube(), ensure_dirs(), export_and_render() (+6 more)

### Community 17 - "Community 17"
Cohesion: 0.33
Nodes (13): add_metadata(), add_stand(), build_lineup_render(), build_single_character(), ensure_dirs(), look_at(), main(), make_armature() (+5 more)

### Community 18 - "Community 18"
Cohesion: 0.51
Nodes (10): add_exhibit_a(), add_exhibit_heading(), add_main_agreement(), add_page_break(), add_regular_lod(), add_soundexchange_lod(), main(), p() (+2 more)

### Community 19 - "Community 19"
Cohesion: 0.36
Nodes (10): audio_levels(), draw_centered_lines(), heart_points(), load_font(), lyric_layout(), make_background(), parse_srt(), render() (+2 more)

### Community 20 - "Community 20"
Cohesion: 0.4
Nodes (9): assertFile(), clickIfPresent(), fillPrompt(), loadConfig(), main(), prepareClip(), promptUser(), setFileOnInput() (+1 more)

### Community 21 - "Community 21"
Cohesion: 0.39
Nodes (1): KidNationRigPreviewRenderer

### Community 22 - "Community 22"
Cohesion: 0.42
Nodes (8): debugShot(), dragMediaToPrompt(), ensureComposer(), fillPrompt(), findButtonFromText(), focusUploadedMedia(), main(), uploadFiles()

### Community 23 - "Community 23"
Cohesion: 0.62
Nodes (6): delete_paragraph(), main(), replace_everywhere(), replace_in_paragraph(), set_cell_paragraphs(), set_para_text_keep_format()

### Community 24 - "Community 24"
Cohesion: 0.48
Nodes (5): estimate_background(), flood_background(), main(), make_cutout(), trim_alpha()

### Community 25 - "Community 25"
Cohesion: 0.48
Nodes (1): KidNationGrandPrixSetup

### Community 26 - "Community 26"
Cohesion: 0.53
Nodes (1): TreasureTownAutoSetup

### Community 27 - "Community 27"
Cohesion: 0.4
Nodes (2): refreshRecent(), renderRecent()

### Community 28 - "Community 28"
Cohesion: 0.7
Nodes (4): main(), parse_args(), slugify(), write_text()

### Community 29 - "Community 29"
Cohesion: 0.7
Nodes (4): load_rig_module(), main(), render_portrait(), render_portrait_lineup()

### Community 30 - "Community 30"
Cohesion: 0.7
Nodes (4): main(), parse_srt(), srt_time_to_ass(), wrap_lyric()

### Community 31 - "Community 31"
Cohesion: 0.83
Nodes (3): getArg(), main(), promptUser()

### Community 32 - "Community 32"
Cohesion: 0.83
Nodes (3): character_slug(), load_dialogue(), main()

### Community 33 - "Community 33"
Cohesion: 1.0
Nodes (2): main(), promptUser()

## Knowledge Gaps
- **91 isolated node(s):** `CharacterSpec`, `CharacterSpec`, `RacerProfile`, `RacerState`, `StarPickup` (+86 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 0`** (94 nodes): `.RollNext()`, `TreasureTownGame`, `.AddBasketballHoop()`, `.AddBillboard()`, `.AddBlockQuestMegaLogo()`, `.AddBlockSpectacle()`, `.AddBodyText()`, `.AddCoinTrail()`, `.AddFeedback()`, `.AddFestivalLantern()`, `.AddFlowerPlanters()`, `.AddGraffitiWall()`, `.AddHeroLineup()`, `.AddHoopCourt()`, `.AddKeyArtMural()`, `.AddMailbox()`, `.AddMountain()`, `.AddPictureStreetSet()`, `.AddPineTree()`, `.AddPuddleCluster()`, `.AddRoad()`, `.AddStreetRow()`, `.AnimateDistricts()`, `.AnimateIntro()`, `.AnimateSceneProps()`, `.ApplyAvatarPose()`, `.BuildActivityPanel()`, `.BuildDistrict()`, `.BuildDock()`, `.BuildEnterPanel()`, `.BuildHud()`, `.BuildIntroPanel()`, `.BuildPlayer()`, `.BuildSpeech()`, `.BuildStructure()`, `.BuildUi()`, `.BuildVoiceClip()`, `.BuildWorld()`, `.CharacterById()`, `.CheckNearbyDistrict()`, `.ClearChildren()`, `.CloseActivity()`, `.CreateAccessory()`, `.CreateButton()`, `.CreateCharacterAvatar()`, `.CreateHudPill()`, `.CreateImage()`, `.CreateLogoTile()`, `.CreatePanel()`, `.CreatePrimitivePart()`, `.CreateText()`, `.CreateWorldLabel()`, `.DistrictById()`, `.DrawNumberActivity()`, `.DrawPatternActivity()`, `.DrawSprintActivity()`, `.DrawSprintRoadObject()`, `.DrawWordActivity()`, `.EnsureDistrictProgressInitialized()`, `.FaceBillboards()`, `.FindDistrictNearPoint()`, `.FollowCamera()`, `.HandleInput()`, `.InitializeCharacterPortraits()`, `.IsDistrictHelperAvatar()`, `.LoadCharacterPortrait()`, `.LoadProgress()`, `.LoadSprite()`, `.MakeMaterial()`, `.MakeUnlitMaterial()`, `.MovePlayer()`, `.NextVoiceRandom()`, `.OpenActivity()`, `.PlayVoice()`, `.PointLight()`, `.RebuildDistrict()`, `.RefreshPlayerCharacter()`, `.Reward()`, `.SaveProgress()`, `.Say()`, `.SetCharacterImage()`, `.SetGridRect()`, `.SetRect()`, `.SetupAudio()`, `.SetupRendering()`, `.Start()`, `.StartNumberActivity()`, `.StartPatternActivity()`, `.StartSprintActivity()`, `.StartWordActivity()`, `.Update()`, `.UpdateCharacterAvatars()`, `.UpdateEnterPanel()`, `.UpdateHud()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 14`** (17 nodes): `CharacterSpec`, `KidNationRigPrefabBuilder`, `.AddBone()`, `.BuildBody()`, `.BuildBones()`, `.BuildCharacterPrefab()`, `.BuildHair()`, `.BuildLimbs()`, `.BuildOutfitDetails()`, `.CreatePart()`, `.EnsureCharacterRigPrefabs()`, `.EnsureFolder()`, `.FindShader()`, `.GetMaterial()`, `.GetPrefabPath()`, `.RebuildCharacterRigPrefabs()`, `KidNationRigPrefabBuilder.cs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 21`** (9 nodes): `KidNationRigPreviewRenderer`, `.CreateCamera()`, `.CreateFloor()`, `.CreateLighting()`, `.FindShader()`, `.PlaceCharacters()`, `.Render()`, `.RenderContactSheet()`, `KidNationRigPreviewRenderer.cs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 25`** (7 nodes): `KidNationGrandPrixSetup`, `.BuildMacGrandPrix()`, `.ConfigureCharacterImports()`, `.CreateScene()`, `.EnsureScene()`, `.RebuildScene()`, `KidNationGrandPrixSetup.cs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 26`** (6 nodes): `TreasureTownAutoSetup`, `.ConfigureCharacterTextureImports()`, `.CreateScene()`, `.EnsureProjectScene()`, `.RebuildDemoScene()`, `TreasureTownAutoSetup.cs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 27`** (6 nodes): `app.js`, `formatNumber()`, `refreshHealth()`, `refreshRecent()`, `renderRecent()`, `renderResults()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 33`** (3 nodes): `main()`, `promptUser()`, `name-reference.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `TreasureTownGame` connect `Community 0` to `Community 12`?**
  _High betweenness centrality (0.039) - this node is a cross-community bridge._
- **Why does `KidNationGrandPrix` connect `Community 4` to `Community 12`?**
  _High betweenness centrality (0.023) - this node is a cross-community bridge._
- **What connects `CharacterSpec`, `CharacterSpec`, `RacerProfile` to the rest of the system?**
  _91 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.07 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.03 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.07 - nodes in this community are weakly interconnected._
- **Should `Community 3` be split into smaller, more focused modules?**
  _Cohesion score 0.09 - nodes in this community are weakly interconnected._