"""
Platform Manager - Manages platform-specific configurations and integrations.
"""

from typing import Dict, List, Optional
from ..models.groq_model import GroqModel


class PlatformManager:
    """
    Manages multiple streaming platform integrations and model instances.
    """
    
    SUPPORTED_PLATFORMS = [
        "twitch",
        "youtube",
        "facebook",
        "tiktok",
        "kick",
        "trovo",
    ]
    
    def __init__(self):
        """Initialize the platform manager."""
        self._models: Dict[str, GroqModel] = {}
    
    def get_model(self, platform: str) -> GroqModel:
        """
        Get or create a model for the specified platform.
        
        Args:
            platform: The streaming platform name
        
        Returns:
            GroqModel instance for the platform
        
        Raises:
            ValueError: If platform is not supported
        """
        platform = platform.lower()
        
        if platform not in self.SUPPORTED_PLATFORMS:
            raise ValueError(
                f"Platform '{platform}' is not supported. "
                f"Supported platforms: {', '.join(self.SUPPORTED_PLATFORMS)}"
            )
        
        if platform not in self._models:
            self._models[platform] = GroqModel(platform=platform)
        
        return self._models[platform]
    
    def get_all_platforms(self) -> List[str]:
        """
        Get list of all supported platforms.
        
        Returns:
            List of platform names
        """
        return self.SUPPORTED_PLATFORMS.copy()
    
    def is_platform_supported(self, platform: str) -> bool:
        """
        Check if a platform is supported.
        
        Args:
            platform: The platform name to check
        
        Returns:
            True if supported, False otherwise
        """
        return platform.lower() in self.SUPPORTED_PLATFORMS
    
    def get_platform_info(self, platform: str) -> Dict[str, str]:
        """
        Get information about a specific platform.
        
        Args:
            platform: The platform name
        
        Returns:
            Dictionary with platform information
        """
        platform = platform.lower()
        
        platform_info = {
            "twitch": {
                "name": "Twitch",
                "description": "Leading live streaming platform for gaming and creative content",
                "monetization": "Subscriptions, Bits, Ads",
                "features": "Raids, Clips, VODs, Extensions"
            },
            "youtube": {
                "name": "YouTube",
                "description": "World's largest video platform with live streaming capabilities",
                "monetization": "Super Chat, Memberships, Ads",
                "features": "Premieres, Shorts, Community Tab, Analytics"
            },
            "facebook": {
                "name": "Facebook Gaming",
                "description": "Social media integrated gaming and live streaming platform",
                "monetization": "Stars, Subscriptions, Creator Programs",
                "features": "Groups, Events, Cross-posting, Gaming Hub"
            },
            "tiktok": {
                "name": "TikTok",
                "description": "Short-form video platform with live streaming features",
                "monetization": "LIVE Gifts, Creator Fund, Brand Partnerships",
                "features": "Duets, Stitches, Trending Sounds, Effects"
            },
            "kick": {
                "name": "Kick",
                "description": "Creator-first streaming platform with favorable revenue splits",
                "monetization": "Subscriptions (95/5 split), Tips",
                "features": "Low latency, Creator-friendly policies"
            },
            "trovo": {
                "name": "Trovo",
                "description": "Interactive live streaming platform with unique features",
                "monetization": "Mana system, Subscriptions, Sponsorships",
                "features": "Built-in tools, Community features"
            },
        }
        
        if platform not in platform_info:
            return {
                "name": platform.title(),
                "description": "Platform information not available",
                "monetization": "Unknown",
                "features": "Unknown"
            }
        
        return platform_info[platform]
    
    def compare_platforms(
        self,
        platforms: List[str],
        criteria: Optional[str] = None
    ) -> str:
        """
        Compare multiple platforms using AI analysis.
        
        Args:
            platforms: List of platforms to compare
            criteria: Specific comparison criteria (optional)
        
        Returns:
            Comparison analysis
        """
        # Use any model for comparison (they all have access to cross-platform knowledge)
        model = self.get_model(platforms[0] if platforms else "twitch")
        
        query = f"Compare these live streaming platforms: {', '.join(platforms)}."
        
        if criteria:
            query += f"\nFocus on: {criteria}"
        
        query += "\n\nProvide a detailed comparison including pros, cons, and best use cases."
        
        return model.generate_response(query)
