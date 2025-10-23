"""
Base integration class for streaming platforms.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
import asyncio


class PlatformIntegration(ABC):
    """
    Abstract base class for streaming platform integrations.
    """
    
    def __init__(self, platform: str, api_key: Optional[str] = None):
        """
        Initialize platform integration.
        
        Args:
            platform: Platform name
            api_key: API key for the platform (if required)
        """
        self.platform = platform
        self.api_key = api_key
        self.connected = False
    
    @abstractmethod
    async def connect(self) -> bool:
        """
        Connect to the platform API.
        
        Returns:
            True if connected successfully
        """
        pass
    
    @abstractmethod
    async def disconnect(self) -> None:
        """Disconnect from the platform API."""
        pass
    
    @abstractmethod
    async def get_stream_info(self) -> Dict[str, Any]:
        """
        Get current stream information.
        
        Returns:
            Stream information dictionary
        """
        pass
    
    @abstractmethod
    async def get_chat_messages(self, limit: int = 100) -> List[Dict[str, Any]]:
        """
        Get recent chat messages.
        
        Args:
            limit: Maximum number of messages to retrieve
        
        Returns:
            List of chat messages
        """
        pass
    
    @abstractmethod
    async def send_chat_message(self, message: str) -> bool:
        """
        Send a message to chat.
        
        Args:
            message: Message to send
        
        Returns:
            True if sent successfully
        """
        pass
    
    @abstractmethod
    async def get_viewer_count(self) -> int:
        """
        Get current viewer count.
        
        Returns:
            Number of viewers
        """
        pass
    
    @abstractmethod
    async def get_analytics(self) -> Dict[str, Any]:
        """
        Get stream analytics.
        
        Returns:
            Analytics data
        """
        pass


class MockPlatformIntegration(PlatformIntegration):
    """
    Mock integration for testing and demonstration.
    """
    
    def __init__(self, platform: str, api_key: Optional[str] = None):
        super().__init__(platform, api_key)
        self.mock_viewers = 50
        self.mock_messages = []
    
    async def connect(self) -> bool:
        """Connect to mock platform."""
        await asyncio.sleep(0.1)  # Simulate connection delay
        self.connected = True
        return True
    
    async def disconnect(self) -> None:
        """Disconnect from mock platform."""
        self.connected = False
    
    async def get_stream_info(self) -> Dict[str, Any]:
        """Get mock stream information."""
        return {
            "platform": self.platform,
            "stream_id": "mock_stream_123",
            "title": "Test Stream",
            "is_live": True,
            "started_at": "2024-01-01T00:00:00Z",
            "viewer_count": self.mock_viewers
        }
    
    async def get_chat_messages(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Get mock chat messages."""
        return [
            {
                "id": f"msg_{i}",
                "user": f"user_{i}",
                "message": f"Test message {i}",
                "timestamp": "2024-01-01T00:00:00Z"
            }
            for i in range(min(limit, 10))
        ]
    
    async def send_chat_message(self, message: str) -> bool:
        """Send mock chat message."""
        self.mock_messages.append(message)
        return True
    
    async def get_viewer_count(self) -> int:
        """Get mock viewer count."""
        return self.mock_viewers
    
    async def get_analytics(self) -> Dict[str, Any]:
        """Get mock analytics."""
        return {
            "platform": self.platform,
            "total_views": 1000,
            "average_viewers": 45,
            "peak_viewers": 75,
            "chat_messages": 500,
            "new_followers": 10,
            "engagement_rate": 0.42
        }
