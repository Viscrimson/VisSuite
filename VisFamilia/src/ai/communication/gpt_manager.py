class GPTManager:
    """Interface for GPT calls and splitting multi-character responses."""
    def __init__(self, api_url: str = None) -> None:
        self.api_url = api_url

    def generate(self, context: str) -> dict[str, str]:
        """Send context to GPT and return { 'char1': resp1, ... }"""
        raise NotImplementedError("GPTManager.generate not implemented yet")