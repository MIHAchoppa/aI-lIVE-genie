"""
Streaming Platform Data
Contains payout rates and conversion information for various streaming platforms.
"""

import json
import os
from typing import Dict, Any, Optional, List
from datetime import datetime


class StreamingPlatformData:
    """Manages streaming platform payouts and conversion rates."""
    
    # Default payout rates per platform (per 1000 views/streams)
    DEFAULT_PAYOUT_RATES = {
        "youtube": {
            "name": "YouTube",
            "payout_per_1000_views": {
                "min": 0.25,
                "max": 4.00,
                "average": 1.50,
                "currency": "USD"
            },
            "factors": [
                "CPM (Cost Per Mille) varies by country",
                "Content category affects rates",
                "Ad engagement impacts earnings",
                "YouTube Premium views pay more"
            ],
            "monetization_requirements": {
                "subscribers": 1000,
                "watch_hours_12_months": 4000
            }
        },
        "twitch": {
            "name": "Twitch",
            "payout_per_1000_views": {
                "min": 2.00,
                "max": 10.00,
                "average": 3.50,
                "currency": "USD"
            },
            "subscription_tiers": {
                "tier_1": 4.99,
                "tier_2": 9.99,
                "tier_3": 24.99,
                "streamer_cut_percentage": 50
            },
            "bits_value": {
                "per_100_bits": 1.00,
                "currency": "USD"
            },
            "factors": [
                "Ad revenue depends on viewer count",
                "Subscriptions provide steady income",
                "Bits provide direct support",
                "Partner status affects rates"
            ]
        },
        "spotify": {
            "name": "Spotify",
            "payout_per_1000_streams": {
                "min": 3.00,
                "max": 5.00,
                "average": 4.00,
                "currency": "USD"
            },
            "factors": [
                "Pays per stream, not per listener",
                "Premium streams pay more than free tier",
                "Country of listener affects rate",
                "Artist's agreement impacts payout"
            ]
        },
        "tiktok": {
            "name": "TikTok",
            "payout_per_1000_views": {
                "min": 0.02,
                "max": 0.04,
                "average": 0.03,
                "currency": "USD"
            },
            "creator_fund": {
                "min_followers": 10000,
                "min_views_30_days": 100000,
                "min_age": 18
            },
            "factors": [
                "Views alone pay relatively low",
                "Live gifts can be lucrative",
                "Brand partnerships are primary income",
                "Engagement rate matters more than views"
            ]
        },
        "facebook_gaming": {
            "name": "Facebook Gaming",
            "payout_per_1000_views": {
                "min": 0.01,
                "max": 0.02,
                "average": 0.015,
                "currency": "USD"
            },
            "stars_value": {
                "per_star": 0.01,
                "currency": "USD"
            },
            "factors": [
                "Stars are primary monetization",
                "Level Up program requirements apply",
                "Ad breaks provide additional revenue",
                "Gaming category affects earnings"
            ]
        },
        "instagram": {
            "name": "Instagram",
            "payout_per_1000_views": {
                "min": 0.20,
                "max": 2.00,
                "average": 0.50,
                "currency": "USD"
            },
            "reels_bonus": {
                "play_based": "Variable",
                "invite_only": True
            },
            "factors": [
                "Reels Play Bonus is invite-only",
                "Brand partnerships main income source",
                "IGTV ads available for some creators",
                "Badges in Live provide income"
            ]
        },
        "apple_music": {
            "name": "Apple Music",
            "payout_per_1000_streams": {
                "min": 6.00,
                "max": 10.00,
                "average": 7.50,
                "currency": "USD"
            },
            "factors": [
                "Higher per-stream rate than most platforms",
                "All streams are from premium subscribers",
                "Geographic location affects rates",
                "Consistent payout structure"
            ]
        }
    }
    
    # Conversion rate data (engagement to monetization)
    CONVERSION_RATES = {
        "view_to_subscriber": {
            "youtube": {
                "average": 0.02,  # 2% of viewers subscribe
                "good": 0.05,     # 5% is considered good
                "excellent": 0.10  # 10% is excellent
            },
            "twitch": {
                "average": 0.015,
                "good": 0.04,
                "excellent": 0.08
            }
        },
        "viewer_to_paid_subscriber": {
            "youtube_membership": {
                "average": 0.001,  # 0.1% of viewers become members
                "good": 0.005,
                "excellent": 0.01
            },
            "twitch_sub": {
                "average": 0.005,  # 0.5% of viewers subscribe
                "good": 0.02,
                "excellent": 0.05
            },
            "patreon": {
                "average": 0.002,
                "good": 0.01,
                "excellent": 0.03
            }
        },
        "view_to_click": {
            "average_ctr": 0.02,  # 2% click-through rate
            "good_ctr": 0.05,
            "excellent_ctr": 0.10
        },
        "engagement_rate": {
            "youtube": {
                "average": 0.04,  # 4% like/comment
                "good": 0.08,
                "excellent": 0.15
            },
            "instagram": {
                "average": 0.03,
                "good": 0.06,
                "excellent": 0.12
            },
            "tiktok": {
                "average": 0.06,
                "good": 0.12,
                "excellent": 0.20
            }
        }
    }
    
    def __init__(self, storage_path: str = "streaming_data.json"):
        self.storage_path = storage_path
        self.custom_data = self._load_custom_data()
    
    def _load_custom_data(self) -> Dict[str, Any]:
        """Load custom streaming data if exists."""
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}
    
    def _save_custom_data(self):
        """Save custom streaming data."""
        with open(self.storage_path, 'w') as f:
            json.dump(self.custom_data, f, indent=2)
    
    def get_platform_data(self, platform: str) -> Optional[Dict[str, Any]]:
        """Get payout data for a specific platform."""
        # Check custom data first
        if platform in self.custom_data:
            return self.custom_data[platform]
        # Fall back to default data
        return self.DEFAULT_PAYOUT_RATES.get(platform.lower())
    
    def get_all_platforms(self) -> List[str]:
        """Get list of all available platforms."""
        platforms = list(self.DEFAULT_PAYOUT_RATES.keys())
        platforms.extend([p for p in self.custom_data.keys() if p not in platforms])
        return sorted(platforms)
    
    def get_conversion_rates(self, conversion_type: str) -> Optional[Dict[str, Any]]:
        """Get conversion rate data for a specific type."""
        return self.CONVERSION_RATES.get(conversion_type)
    
    def calculate_earnings(self, platform: str, views: int) -> Dict[str, Any]:
        """Calculate estimated earnings for a given number of views."""
        platform_data = self.get_platform_data(platform)
        if not platform_data:
            return {"error": f"Platform '{platform}' not found"}
        
        payout_data = platform_data.get("payout_per_1000_views") or platform_data.get("payout_per_1000_streams")
        if not payout_data:
            return {"error": "Payout data not available"}
        
        factor = views / 1000.0
        return {
            "platform": platform,
            "views": views,
            "estimated_earnings": {
                "min": round(payout_data["min"] * factor, 2),
                "max": round(payout_data["max"] * factor, 2),
                "average": round(payout_data["average"] * factor, 2),
                "currency": payout_data.get("currency", "USD")
            }
        }
    
    def calculate_subscribers_from_views(self, platform: str, views: int, 
                                         quality: str = "average") -> int:
        """Calculate expected subscribers from views based on conversion rates."""
        conversion_data = self.CONVERSION_RATES.get("view_to_subscriber", {}).get(platform)
        if not conversion_data:
            # Use average across platforms if specific data not available
            conversion_rate = 0.02
        else:
            conversion_rate = conversion_data.get(quality, conversion_data.get("average", 0.02))
        
        return int(views * conversion_rate)
    
    def add_custom_platform(self, platform: str, platform_data: Dict[str, Any]):
        """Add or update custom platform data."""
        self.custom_data[platform] = {
            **platform_data,
            "custom": True,
            "last_updated": datetime.now().isoformat()
        }
        self._save_custom_data()
    
    def compare_platforms(self, views: int) -> List[Dict[str, Any]]:
        """Compare earnings across all platforms for given views."""
        results = []
        for platform in self.get_all_platforms():
            earnings = self.calculate_earnings(platform, views)
            if "error" not in earnings:
                results.append(earnings)
        
        # Sort by average earnings, highest first
        results.sort(key=lambda x: x["estimated_earnings"]["average"], reverse=True)
        return results
    
    def get_monetization_requirements(self, platform: str) -> Optional[Dict[str, Any]]:
        """Get monetization requirements for a platform."""
        platform_data = self.get_platform_data(platform)
        if platform_data:
            return platform_data.get("monetization_requirements")
        return None
    
    def get_earning_factors(self, platform: str) -> Optional[List[str]]:
        """Get factors that affect earnings on a platform."""
        platform_data = self.get_platform_data(platform)
        if platform_data:
            return platform_data.get("factors")
        return None
