DEFAULT_PROVIDER = "anthropic"
SUPPORTED_LM_PROVIDERS = ("anthropic", "openai")


def normalize_provider(provider):
    provider = (provider or DEFAULT_PROVIDER).strip().lower() or DEFAULT_PROVIDER
    if provider not in SUPPORTED_LM_PROVIDERS:
        supported = ", ".join(SUPPORTED_LM_PROVIDERS)
        raise ValueError(f"Unsupported LLM provider '{provider}'. Supported providers: {supported}.")
    return provider
