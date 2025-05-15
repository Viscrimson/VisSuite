class NPC:
    """Single NPC behavior and state manager."""
    def __init__(self, ini_path: str) -> None:
        # TODO: read per-character config
        self.ini_path = ini_path

    def tick(self) -> None:
        """Perform one cycle: listen, think, speak."""
        raise NotImplementedError("NPC.tick not implemented yet")