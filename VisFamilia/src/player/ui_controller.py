import logging
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel, QComboBox, QFrame
from PyQt6.QtCore import Qt
from player.settings_manager import SettingsManager
from typing import Any

logger = logging.getLogger(__name__)

class UIController(QWidget):
    """Main UI for player input, transcription and routing."""
    def __init__(self, settings: SettingsManager, tts: Any, audio_mgr: Any, transcription: Any) -> None:
        super().__init__()
        self.settings = settings
        self.tts = tts
        self.audio = audio_mgr
        self.transcription = transcription
        self.init_ui()

    def init_ui(self) -> None:
        layout = QVBoxLayout()
        # TODO: build UI per design.md
        self.setLayout(layout)
        self.show()