class FollowerAI:
    """Simple leader-follower movement logic."""
    def __init__(self, leader_id: str) -> None:
        self.leader_id = leader_id

    def update(self) -> None:
        raise NotImplementedError("FollowerAI.update not implemented yet")