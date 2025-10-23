"""
AI Live Genie - Master set of AI fine-tuned Groq models for live streaming platforms
with strategy and host training bot capabilities.
"""

__version__ = "0.1.0"
__author__ = "MIHAchoppa"

from .models.groq_model import GroqModel
from .training.host_training_bot import HostTrainingBot
from .platforms.platform_manager import PlatformManager

__all__ = ["GroqModel", "HostTrainingBot", "PlatformManager"]
