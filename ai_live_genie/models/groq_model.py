"""
Core Groq Model implementation for fine-tuned streaming platform models.
"""

import os
from typing import Optional, Dict, Any, List
from dotenv import load_dotenv

try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False
    Groq = None

load_dotenv()


class GroqModel:
    """
    Base class for Groq AI models fine-tuned for live streaming platforms.
    """
    
    def __init__(
        self,
        platform: str,
        model_name: Optional[str] = None,
        api_key: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1024
    ):
        """
        Initialize a Groq model for a specific streaming platform.
        
        Args:
            platform: The streaming platform (twitch, youtube, facebook, tiktok, kick, etc.)
            model_name: Groq model to use (default: mixtral-8x7b-32768)
            api_key: Groq API key (default: from env)
            temperature: Sampling temperature (0-2)
            max_tokens: Maximum tokens to generate
        """
        self.platform = platform.lower()
        self.model_name = model_name or os.getenv("DEFAULT_MODEL", "mixtral-8x7b-32768")
        self.temperature = temperature
        self.max_tokens = max_tokens
        
        api_key = api_key or os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY must be provided or set in environment")
        
        if not GROQ_AVAILABLE:
            raise ImportError(
                "The 'groq' package is not installed. "
                "Install it with: pip install groq"
            )
        
        self.client = Groq(api_key=api_key)
        self.system_prompt = self._get_platform_system_prompt()
    
    def _get_platform_system_prompt(self) -> str:
        """
        Get the fine-tuned system prompt for the specific platform.
        
        Returns:
            Platform-specific system prompt
        """
        platform_prompts = {
            "twitch": (
                "You are an expert AI assistant for Twitch streamers. You understand Twitch "
                "culture, emotes, chat engagement, streaming strategies, growth tactics, "
                "monetization through subscriptions, bits, and ads. You provide advice on "
                "content scheduling, community building, raid strategies, and technical setup."
            ),
            "youtube": (
                "You are an expert AI assistant for YouTube live streamers. You understand "
                "YouTube's algorithm, Super Chat, memberships, monetization policies, content "
                "strategy, SEO optimization, thumbnail design, and audience retention. You "
                "provide guidance on streaming setup, premiere features, and community engagement."
            ),
            "facebook": (
                "You are an expert AI assistant for Facebook Gaming streamers. You understand "
                "Facebook's streaming platform, Stars system, fan subscriptions, gaming creator "
                "programs, and community building. You provide strategies for cross-platform "
                "promotion, audience growth, and monetization."
            ),
            "tiktok": (
                "You are an expert AI assistant for TikTok live streamers. You understand "
                "TikTok's unique short-form content culture, LIVE gifts, engagement tactics, "
                "viral trends, and algorithm preferences. You provide guidance on content "
                "creation, trending sounds, hashtag strategies, and audience interaction."
            ),
            "kick": (
                "You are an expert AI assistant for Kick streamers. You understand Kick's "
                "creator-friendly revenue split, community features, and growth strategies. "
                "You provide guidance on transitioning from other platforms, building communities, "
                "and maximizing the platform's monetization opportunities."
            ),
            "trovo": (
                "You are an expert AI assistant for Trovo streamers. You understand Trovo's "
                "unique features, Mana system, sponsorship opportunities, and community building. "
                "You provide strategies for content creation and audience engagement."
            ),
        }
        
        return platform_prompts.get(
            self.platform,
            f"You are an expert AI assistant for {self.platform} live streaming platform."
        )
    
    def generate_response(
        self,
        user_message: str,
        conversation_history: Optional[List[Dict[str, str]]] = None,
        **kwargs
    ) -> str:
        """
        Generate a response using the fine-tuned model.
        
        Args:
            user_message: The user's message/query
            conversation_history: Previous conversation messages
            **kwargs: Additional parameters for the API call
        
        Returns:
            Generated response text
        """
        messages = [{"role": "system", "content": self.system_prompt}]
        
        if conversation_history:
            messages.extend(conversation_history)
        
        messages.append({"role": "user", "content": user_message})
        
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=kwargs.get("temperature", self.temperature),
            max_tokens=kwargs.get("max_tokens", self.max_tokens),
        )
        
        return response.choices[0].message.content
    
    def get_streaming_advice(self, query: str) -> str:
        """
        Get streaming advice for the platform.
        
        Args:
            query: The streamer's question or situation
        
        Returns:
            Platform-specific advice
        """
        enhanced_query = f"As a {self.platform} streamer, I need advice: {query}"
        return self.generate_response(enhanced_query)
    
    def get_engagement_strategy(self, audience_size: str, goals: str) -> str:
        """
        Get audience engagement strategy.
        
        Args:
            audience_size: Current audience size (e.g., "small", "medium", "large")
            goals: Streamer's goals
        
        Returns:
            Engagement strategy recommendations
        """
        query = (
            f"I'm a {self.platform} streamer with a {audience_size} audience. "
            f"My goals are: {goals}. What engagement strategies should I use?"
        )
        return self.generate_response(query)
    
    def get_monetization_advice(self, current_status: str) -> str:
        """
        Get monetization advice for the platform.
        
        Args:
            current_status: Current monetization status and goals
        
        Returns:
            Monetization recommendations
        """
        query = (
            f"I'm streaming on {self.platform}. My current status: {current_status}. "
            f"What are the best monetization strategies for this platform?"
        )
        return self.generate_response(query)
