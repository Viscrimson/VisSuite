class SpeakerID:
    """Identify speaker based on audio metadata or fingerprint."""
    def identify(self, audio_chunk: bytes) -> str:
        """Return speaker key like 'char1', 'char2'."""
        raise NotImplementedError("Speaker identification not implemented yet")