"""
AI Live Genie - Memory Management and Streaming Analytics
An AI-powered assistant for live streamers and content creators.
"""

__version__ = "1.0.0"
__author__ = "MIHAchoppa"
__license__ = "MIT"

from .memory_manager import (
    ConversationalMemory,
    LongTermMemory,
    GoalsManager,
    MemoryManager
)
from .streaming_data import StreamingPlatformData

__all__ = [
    "ConversationalMemory",
    "LongTermMemory",
    "GoalsManager",
    "MemoryManager",
    "StreamingPlatformData",
]
