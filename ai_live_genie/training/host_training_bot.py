"""
Host Training Bot - AI-powered training bot for live stream hosts.
Provides personalized training, strategy guidance, and real-time coaching.
"""

from typing import List, Dict, Any, Optional
from ..models.groq_model import GroqModel


class HostTrainingBot:
    """
    AI-powered training bot for live stream hosts across all platforms.
    Provides strategy guidance, content planning, and performance coaching.
    """
    
    def __init__(self, platform: str, model: Optional[GroqModel] = None):
        """
        Initialize the host training bot.
        
        Args:
            platform: Target streaming platform
            model: Custom GroqModel instance (optional)
        """
        self.platform = platform
        self.model = model or GroqModel(platform=platform)
        self.training_history: List[Dict[str, Any]] = []
    
    def create_training_plan(
        self,
        experience_level: str,
        content_type: str,
        goals: List[str]
    ) -> Dict[str, Any]:
        """
        Create a personalized training plan for the host.
        
        Args:
            experience_level: "beginner", "intermediate", or "advanced"
            content_type: Type of content (gaming, creative, IRL, etc.)
            goals: List of streamer's goals
        
        Returns:
            Comprehensive training plan
        """
        query = f"""
        Create a detailed training plan for a {experience_level} {self.platform} streamer.
        Content type: {content_type}
        Goals: {', '.join(goals)}
        
        Include:
        1. Weekly milestones
        2. Skill development areas
        3. Content strategy recommendations
        4. Engagement tactics
        5. Growth metrics to track
        """
        
        response = self.model.generate_response(query)
        
        training_plan = {
            "platform": self.platform,
            "experience_level": experience_level,
            "content_type": content_type,
            "goals": goals,
            "plan": response
        }
        
        self.training_history.append({
            "action": "training_plan_created",
            "data": training_plan
        })
        
        return training_plan
    
    def get_streaming_tips(self, situation: str) -> str:
        """
        Get real-time streaming tips for specific situations.
        
        Args:
            situation: Current streaming situation or challenge
        
        Returns:
            Actionable tips and advice
        """
        query = f"""
        I'm currently streaming on {self.platform} and facing this situation: {situation}
        
        Provide immediate, actionable tips to handle this effectively.
        """
        
        return self.model.generate_response(query)
    
    def analyze_performance(
        self,
        metrics: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Analyze streaming performance and provide improvement suggestions.
        
        Args:
            metrics: Performance metrics (viewers, engagement, duration, etc.)
        
        Returns:
            Performance analysis and recommendations
        """
        metrics_str = "\n".join([f"{k}: {v}" for k, v in metrics.items()])
        
        query = f"""
        Analyze these streaming performance metrics for {self.platform}:
        
        {metrics_str}
        
        Provide:
        1. Performance assessment
        2. Strengths to leverage
        3. Areas for improvement
        4. Specific action items
        5. Benchmark comparisons
        """
        
        analysis = self.model.generate_response(query)
        
        result = {
            "platform": self.platform,
            "metrics": metrics,
            "analysis": analysis
        }
        
        self.training_history.append({
            "action": "performance_analyzed",
            "data": result
        })
        
        return result
    
    def suggest_content_ideas(
        self,
        trending_topics: Optional[List[str]] = None,
        target_audience: Optional[str] = None
    ) -> List[str]:
        """
        Generate content ideas tailored to the platform and audience.
        
        Args:
            trending_topics: Current trending topics (optional)
            target_audience: Description of target audience (optional)
        
        Returns:
            List of content ideas
        """
        query = f"Generate 10 creative content ideas for {self.platform} streaming."
        
        if trending_topics:
            query += f"\nConsider these trending topics: {', '.join(trending_topics)}"
        
        if target_audience:
            query += f"\nTarget audience: {target_audience}"
        
        query += "\n\nProvide each idea on a new line with a brief description."
        
        response = self.model.generate_response(query)
        
        # Parse the response into a list
        ideas = [line.strip() for line in response.split('\n') if line.strip()]
        
        return ideas
    
    def get_engagement_tactics(
        self,
        viewer_count: int,
        chat_activity: str
    ) -> str:
        """
        Get engagement tactics based on current stream conditions.
        
        Args:
            viewer_count: Current number of viewers
            chat_activity: Description of chat activity level
        
        Returns:
            Engagement tactics and strategies
        """
        query = f"""
        I'm streaming on {self.platform} with {viewer_count} viewers.
        Chat activity: {chat_activity}
        
        What engagement tactics should I use right now to increase interaction
        and keep viewers engaged?
        """
        
        return self.model.generate_response(query)
    
    def prepare_stream_session(
        self,
        stream_title: str,
        duration_minutes: int,
        special_events: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Prepare for an upcoming stream session with a structured plan.
        
        Args:
            stream_title: Title/topic of the stream
            duration_minutes: Planned stream duration
            special_events: Any special events or segments planned
        
        Returns:
            Stream preparation plan
        """
        events_str = ""
        if special_events:
            events_str = f"\nSpecial events: {', '.join(special_events)}"
        
        query = f"""
        Help me prepare for a {self.platform} stream:
        Title: {stream_title}
        Duration: {duration_minutes} minutes
        {events_str}
        
        Provide:
        1. Stream structure and pacing
        2. Key talking points
        3. Engagement milestones
        4. Technical checklist
        5. Contingency plans
        """
        
        response = self.model.generate_response(query)
        
        plan = {
            "platform": self.platform,
            "stream_title": stream_title,
            "duration_minutes": duration_minutes,
            "special_events": special_events or [],
            "preparation_plan": response
        }
        
        return plan
    
    def get_training_history(self) -> List[Dict[str, Any]]:
        """
        Get the training history for this bot instance.
        
        Returns:
            List of training actions and their data
        """
        return self.training_history
