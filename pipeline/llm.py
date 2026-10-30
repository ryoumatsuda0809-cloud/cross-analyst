"""The only file that talks to an LLM API (the "provider adapter").

The model gets text, and nothing else: no file access, no web search, no tools.
What it sees is decided entirely by stages.py. To switch to another provider,
rewrite the three functions below (call, list_models, _client) and the SDK line
in requirements.txt. Nothing else in the project depends on the provider.

Current adapter: the google-genai SDK. Get an API key from the provider's
developer console and put it in .env as LLM_API_KEY.
"""
from __future__ import annotations

import os
import time


def model_name(cli_model: str | None = None) -> str:
    name = cli_model or os.environ.get("LLM_MODEL")
    if not name:
        raise SystemExit("LLM_MODEL is not set. Run `python diagnose.py models` and put a model name in .env "
                         "(or run with --mock to test the pipeline without a model).")
    return name


def _client():
    try:
        from google import genai
    except ImportError:
        raise SystemExit("The LLM SDK is not installed. Run: pip install -r requirements.txt")
    key = os.environ.get("LLM_API_KEY")
    if not key:
        raise SystemExit("LLM_API_KEY is not set. Copy .env.example to .env and put your key there "
                         "(or run with --mock to test the pipeline without a key).")
    return genai.Client(api_key=key)


def call(prompt: str, model: str, temperature: float = 0.2, retries: int = 3) -> dict:
    """Send one prompt. Returns {"text", "model", "input_tokens", "output_tokens", "seconds"}."""
    from google.genai import types
    client = _client()
    t0 = time.time()
    last_err = None
    for attempt in range(1, retries + 1):
        try:
            r = client.models.generate_content(
                model=model, contents=prompt,
                config=types.GenerateContentConfig(temperature=temperature))
            u = r.usage_metadata
            return {"text": r.text or "", "model": model,
                    "input_tokens": getattr(u, "prompt_token_count", None),
                    "output_tokens": getattr(u, "candidates_token_count", None),
                    "seconds": round(time.time() - t0, 1)}
        except Exception as e:          # rate limits and timeouts: wait and retry
            last_err = e
            if attempt < retries:
                wait = 10 * attempt
                print(f"  ! LLM API error ({type(e).__name__}): retrying in {wait}s ({attempt}/{retries})")
                time.sleep(wait)
    raise SystemExit(f"LLM API call failed after {retries} attempts: {last_err}")


def list_models() -> list[str]:
    client = _client()
    names = []
    for m in client.models.list():
        actions = getattr(m, "supported_actions", None) or []
        if not actions or "generateContent" in actions:
            names.append(m.name.removeprefix("models/"))
    return sorted(names)
