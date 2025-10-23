"""
Example configuration for platform-specific model fine-tuning.
"""

# Training data templates for different platforms
TRAINING_TEMPLATES = {
    "twitch": {
        "system_instructions": [
            "Understanding Twitch emotes and culture",
            "Raid strategies and networking",
            "Subscription tier benefits optimization",
            "Bits integration and incentives",
            "Category selection and discoverability",
            "Community moderation best practices"
        ],
        "example_queries": [
            "How do I grow my Twitch channel from 0 to 100 followers?",
            "What's the best streaming schedule for maximum reach?",
            "How should I handle trolls in chat?",
            "What overlays and alerts should I use?",
            "How do I prepare for my first raid?"
        ]
    },
    "youtube": {
        "system_instructions": [
            "YouTube algorithm and discovery",
            "SEO optimization for live streams",
            "Thumbnail and title best practices",
            "Super Chat and membership setup",
            "Premiere feature utilization",
            "Cross-promotion with VOD content"
        ],
        "example_queries": [
            "How do I optimize my stream for YouTube search?",
            "What's the best way to promote my live stream?",
            "How do I set up channel memberships?",
            "Should I enable Super Chat for my streams?",
            "How do I convert live viewers to subscribers?"
        ]
    },
    "tiktok": {
        "system_instructions": [
            "TikTok LIVE engagement tactics",
            "Gift receiving and viewer rewards",
            "Trend integration during streams",
            "Short-form content promotion",
            "Hashtag strategy for discoverability",
            "Viral moment creation"
        ],
        "example_queries": [
            "How do I go LIVE on TikTok?",
            "What trends should I incorporate in my stream?",
            "How do I encourage viewers to send gifts?",
            "Should I stream gaming or IRL content?",
            "How do I promote my LIVE stream through short videos?"
        ]
    },
    "kick": {
        "system_instructions": [
            "Kick's 95/5 revenue split optimization",
            "Transitioning from other platforms",
            "Building community on Kick",
            "Leveraging creator-friendly policies",
            "Content creation freedom",
            "Subscriber incentive strategies"
        ],
        "example_queries": [
            "Should I switch from Twitch to Kick?",
            "How do I maximize the 95/5 split on Kick?",
            "What content policies are different on Kick?",
            "How do I build an audience on Kick from scratch?",
            "Can I multistream on Kick?"
        ]
    }
}

# Model fine-tuning parameters
FINE_TUNING_CONFIG = {
    "temperature": 0.7,
    "max_tokens": 1024,
    "top_p": 0.9,
    "frequency_penalty": 0.3,
    "presence_penalty": 0.3
}

# Platform-specific strategies
PLATFORM_STRATEGIES = {
    "beginner": {
        "focus_areas": [
            "Basic setup and equipment",
            "Consistent streaming schedule",
            "Chat engagement fundamentals",
            "Content planning basics",
            "Community building foundations"
        ]
    },
    "intermediate": {
        "focus_areas": [
            "Growth optimization tactics",
            "Monetization strategies",
            "Advanced engagement techniques",
            "Networking and collaborations",
            "Brand development"
        ]
    },
    "advanced": {
        "focus_areas": [
            "Multi-platform strategies",
            "Business optimization",
            "Team management",
            "Sponsorship acquisition",
            "Long-term sustainability"
        ]
    }
}
