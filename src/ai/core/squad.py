from .npc import NPC

class SquadManager:
    """Manage multiple NPC instances."""
    def __init__(self, ini_paths: list[str]) -> None:
        self.npcs = [NPC(path) for path in ini_paths]

    def run(self) -> None:
        """Main loop: call tick() on each NPC."""
        while True:
            for npc in self.npcs:
                npc.tick()