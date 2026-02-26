# OpenClaw Model Configuration Reference

## Provider Schema

```json
{
  "models": {
    "providers": {
      "<provider-name>": {
        "baseUrl": "https://api.example.com/v1",
        "apiKey": "sk-...",
        "api": "openai-completions",
        "models": [
          {
            "id": "model-id",
            "name": "Display Name",
            "reasoning": true,
            "input": ["text", "image"],
            "cost": {
              "input": 0.001,
              "output": 0.003,
              "cacheRead": 0.0002,
              "cacheWrite": 0
            },
            "contextWindow": 200000,
            "maxTokens": 32768,
            "compat": {
              "supportsDeveloperRole": true
            }
          }
        ]
      }
    }
  }
}
```

## Alias Schema (agents.defaults.models)

```json
{
  "agents": {
    "defaults": {
      "models": {
        "<provider>/<model-id>": {
          "alias": "shortname",
          "params": {
            "thinking": {"type": "enabled"},
            "reasoning_effort": "high"
          }
        }
      }
    }
  }
}
```

## Important Notes

1. **Alias conflicts:** Cannot have two models with same alias
2. **Provider names:** Used in model references as `<provider>/<model-id>`
3. **Agent model assignment:** Named agents use `"model": "provider/model-id"` NOT the alias
4. **Defaults override:** `agents.defaults.models` affects what aliases are available
5. **Primary model:** Set at `agents.defaults.model.primary`

## Common Mistakes

1. Using alias instead of full provider/model-id for agent assignments
2. Duplicate aliases across providers
3. Missing apiKey in provider block
4. Wrong baseUrl format (needs `/v1` for OpenAI-compatible)
