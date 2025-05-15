class UdonInterface:
    """Send Udon events into VRChat via OSC or other bridge."""
    def send_event(self, event: str, payload: dict) -> None:
        raise NotImplementedError("UdonInterface not implemented yet")