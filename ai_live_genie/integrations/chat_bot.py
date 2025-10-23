"""
AI-powered chat bot for live streaming platforms.
Integrates with platform APIs and uses AI models for intelligent responses.
"""

from typing import Optional, Dict, Any, Callable, List
import asyncio
from ..models.groq_model import GroqModel
from .base_integration import PlatformIntegration, MockPlatformIntegration


class StreamChatBot:
    """
    AI-powered chat bot for live streams.
    Monitors chat and provides intelligent, context-aware responses.
    """
    
    def __init__(
        self,
        platform: str,
        model: Optional[GroqModel] = None,
        integration: Optional[PlatformIntegration] = None
    ):
        """
        Initialize the stream chat bot.
        
        Args:
            platform: Streaming platform
            model: GroqModel instance (creates one if not provided)
            integration: Platform integration (uses mock if not provided)
        """
        self.platform = platform
        self.model = model or GroqModel(platform=platform)
        self.integration = integration or MockPlatformIntegration(platform=platform)
        self.is_running = False
        self.message_handlers: List[Callable] = []
        self.conversation_history: List[Dict[str, str]] = []
    
    async def start(self) -> None:
        """Start the chat bot."""
        await self.integration.connect()
        self.is_running = True
        print(f"Chat bot started for {self.platform}")
    
    async def stop(self) -> None:
        """Stop the chat bot."""
        self.is_running = False
        await self.integration.disconnect()
        print(f"Chat bot stopped for {self.platform}")
    
    def add_message_handler(self, handler: Callable) -> None:
        """
        Add a custom message handler.
        
        Args:
            handler: Function to handle messages
        """
        self.message_handlers.append(handler)
    
    async def process_message(self, message: Dict[str, Any]) -> Optional[str]:
        """
        Process a chat message and generate response if needed.
        
        Args:
            message: Chat message dictionary
        
        Returns:
            Response message or None
        """
        user = message.get("user", "Unknown")
        text = message.get("message", "")
        
        # Run custom handlers
        for handler in self.message_handlers:
            result = handler(message)
            if result:
                return result
        
        # Check if message is directed at bot (contains keywords)
        bot_keywords = ["bot", "ai", "help", "advice", "question"]
        should_respond = any(keyword in text.lower() for keyword in bot_keywords)
        
        if should_respond:
            # Generate AI response
            context = f"A viewer named {user} in chat asks: {text}"
            response = self.model.generate_response(
                context,
                conversation_history=self.conversation_history[-5:]  # Last 5 messages
            )
            
            # Update conversation history
            self.conversation_history.append({
                "role": "user",
                "content": text
            })
            self.conversation_history.append({
                "role": "assistant",
                "content": response
            })
            
            return response
        
        return None
    
    async def monitor_chat(self, response_callback: Optional[Callable] = None) -> None:
        """
        Monitor chat and respond to messages.
        
        Args:
            response_callback: Function to call with responses
        """
        print(f"Monitoring chat for {self.platform}...")
        
        while self.is_running:
            # Get recent messages
            messages = await self.integration.get_chat_messages(limit=10)
            
            for message in messages:
                response = await self.process_message(message)
                
                if response:
                    if response_callback:
                        response_callback(response)
                    else:
                        # Send response to chat
                        await self.integration.send_chat_message(response)
            
            # Wait before checking again
            await asyncio.sleep(2)
    
    async def get_stream_insights(self) -> Dict[str, Any]:
        """
        Get AI-powered insights about the current stream.
        
        Returns:
            Stream insights and recommendations
        """
        # Get current stream data
        stream_info = await self.integration.get_stream_info()
        analytics = await self.integration.get_analytics()
        
        # Generate insights using AI
        insight_query = f"""
        Analyze this stream session on {self.platform}:
        
        Viewer Count: {stream_info.get('viewer_count', 0)}
        Average Viewers: {analytics.get('average_viewers', 0)}
        Peak Viewers: {analytics.get('peak_viewers', 0)}
        Chat Messages: {analytics.get('chat_messages', 0)}
        New Followers: {analytics.get('new_followers', 0)}
        Engagement Rate: {analytics.get('engagement_rate', 0)}
        
        Provide:
        1. Performance assessment
        2. What's working well
        3. Areas to improve
        4. Immediate action items
        """
        
        insights = self.model.generate_response(insight_query)
        
        return {
            "platform": self.platform,
            "stream_info": stream_info,
            "analytics": analytics,
            "ai_insights": insights
        }
    
    async def suggest_chat_response(self, context: str) -> str:
        """
        Suggest a response to a specific chat situation.
        
        Args:
            context: Description of the chat situation
        
        Returns:
            Suggested response
        """
        query = f"""
        I'm streaming on {self.platform} and need help responding to this chat situation:
        
        {context}
        
        Suggest a good response that is:
        - Engaging and friendly
        - Platform-appropriate
        - Encourages further interaction
        """
        
        return self.model.generate_response(query)
