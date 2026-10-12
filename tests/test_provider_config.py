import importlib.util
import unittest
from pathlib import Path


PROVIDER_MODULE_PATH = (
    Path(__file__).resolve().parents[1] / "mcp-client" / "routes" / "providers.py"
)


def load_provider_module():
    spec = importlib.util.spec_from_file_location("provider_config", PROVIDER_MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ProviderConfigTest(unittest.TestCase):
    def test_normalize_provider_defaults_to_anthropic(self):
        providers = load_provider_module()

        self.assertEqual(providers.normalize_provider(None), "anthropic")
        self.assertEqual(providers.normalize_provider(""), "anthropic")

    def test_normalize_provider_accepts_supported_providers_case_insensitively(self):
        providers = load_provider_module()

        self.assertEqual(providers.normalize_provider(" OpenAI "), "openai")
        self.assertEqual(providers.normalize_provider("ANTHROPIC"), "anthropic")

    def test_normalize_provider_rejects_unsupported_providers(self):
        providers = load_provider_module()

        with self.assertRaises(ValueError) as context:
            providers.normalize_provider("gemini")

        self.assertIn("Unsupported LLM provider 'gemini'", str(context.exception))
        self.assertIn("anthropic, openai", str(context.exception))


if __name__ == "__main__":
    unittest.main()
