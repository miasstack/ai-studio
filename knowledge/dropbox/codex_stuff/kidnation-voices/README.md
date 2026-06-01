# KidNation Voices

Local character voice generation using Chatterbox MLX on Apple Silicon.

## Setup

The Python 3.11 environment is already created at `.venv311`.

Activate it:

```bash
source .venv311/bin/activate
```

## Add Character Voices

Put one clean WAV reference per character in `voices/`.

Use lowercase filenames that match the character slug:

```text
voices/
  mia.wav
  jax.wav
  luma.wav
```

For best results, use a clean 10-30 second voice reference with no music.

## Generate Dialogue

Edit `dialogue.json`, then run:

```bash
.venv311/bin/python scripts/generate_dialogue.py
```

Outputs land in `output/`:

```text
output/001_mia.wav
output/002_jax.wav
```

You can tune a line with optional fields:

```json
{
  "character": "mia",
  "text": "We have one shot. Make it count.",
  "exaggeration": 0.65,
  "cfg": 0.45,
  "seed": 1234
}
```

You can also use the raw CLI:

```bash
.venv311/bin/python -m chatterbox "Hello from KidNation." --voice voices/mia.wav -o output/test_mia.wav
```
