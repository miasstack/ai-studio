---
name: textbelt-sms
description: Send one-off SMS messages or check SMS quota with Textbelt from this workspace.
---

# Textbelt SMS

Use this skill when the user wants to send a one-off SMS from Codex or check available Textbelt quota.

## What this plugin does

- Sends SMS through Textbelt's hosted API.
- Defaults to the public `textbelt` key when `TEXTBELT_API_KEY` is not set.
- Supports a safe `--test` mode that validates the request without consuming quota.

## Important limits

- The hosted public key supports only one free SMS per day.
- For more than that, the user needs their own Textbelt API key in `TEXTBELT_API_KEY`.
- Do not send a real SMS unless the user explicitly asked to send it and provided or confirmed the recipient and message.
- This is not appropriate for emergency or life-safety use.

## Commands

Send a real SMS:

```bash
bash plugins/textbelt-sms/scripts/send_sms.sh \
  --to +15551234567 \
  --message "Your render is done."
```

Validate without sending:

```bash
bash plugins/textbelt-sms/scripts/send_sms.sh \
  --to +15551234567 \
  --message "Test message" \
  --test
```

Check remaining quota:

```bash
bash plugins/textbelt-sms/scripts/check_quota.sh
```

Use a private key for higher volume:

```bash
TEXTBELT_API_KEY=your_key_here \
bash plugins/textbelt-sms/scripts/send_sms.sh \
  --to +15551234567 \
  --message "Hello from Codex"
```

## Notes

- Phone numbers should be sent in E.164 format when possible, for example `+15551234567`.
- The scripts use `curl --data-urlencode` so `+` in the phone number and special characters in the message are encoded correctly.
