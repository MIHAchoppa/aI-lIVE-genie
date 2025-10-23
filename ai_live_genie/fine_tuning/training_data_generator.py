"""
Training data generator for fine-tuning Groq models with platform-specific content.
"""

from typing import List, Dict, Any
import json
from ..config import TRAINING_TEMPLATES


class TrainingDataGenerator:
    """
    Generate training data for fine-tuning models for specific streaming platforms.
    """
    
    def __init__(self, platform: str):
        """
        Initialize the training data generator.
        
        Args:
            platform: Target streaming platform
        """
        self.platform = platform.lower()
    
    def generate_training_examples(
        self,
        num_examples: int = 100
    ) -> List[Dict[str, Any]]:
        """
        Generate training examples for the platform.
        
        Args:
            num_examples: Number of training examples to generate
        
        Returns:
            List of training examples in chat format
        """
        examples = []
        
        if self.platform not in TRAINING_TEMPLATES:
            return examples
        
        template = TRAINING_TEMPLATES[self.platform]
        
        # Generate examples for each query type
        for query in template.get("example_queries", []):
            example = {
                "messages": [
                    {
                        "role": "system",
                        "content": self._get_system_prompt()
                    },
                    {
                        "role": "user",
                        "content": query
                    },
                    {
                        "role": "assistant",
                        "content": self._generate_response_template(query)
                    }
                ]
            }
            examples.append(example)
        
        return examples
    
    def _get_system_prompt(self) -> str:
        """Get the system prompt for the platform."""
        prompts = {
            "twitch": (
                "You are an expert streaming coach for Twitch. You provide specific, "
                "actionable advice about Twitch streaming, including growth strategies, "
                "engagement tactics, monetization, and technical setup."
            ),
            "youtube": (
                "You are an expert streaming coach for YouTube Live. You provide specific "
                "advice about YouTube's platform, SEO, monetization through Super Chat and "
                "memberships, and content strategy."
            ),
            "tiktok": (
                "You are an expert coach for TikTok LIVE streaming. You provide advice on "
                "TikTok's unique culture, LIVE gifts, trending content, and short-form video "
                "integration."
            ),
            "kick": (
                "You are an expert streaming coach for Kick. You provide advice on leveraging "
                "Kick's creator-friendly 95/5 split, platform features, and growth strategies."
            )
        }
        return prompts.get(self.platform, f"You are an expert streaming coach for {self.platform}.")
    
    def _generate_response_template(self, query: str) -> str:
        """
        Generate a response template for a query.
        
        Args:
            query: The example query
        
        Returns:
            Template response
        """
        # This would normally be filled with actual expert responses
        # For demonstration, we provide a structured template
        return (
            f"Here's my advice for your question about {self.platform}:\n\n"
            "1. **Immediate Actions**: [Specific steps to take now]\n"
            "2. **Short-term Strategy**: [What to focus on this week/month]\n"
            "3. **Long-term Goals**: [Where this fits in your growth plan]\n"
            "4. **Platform-Specific Tips**: [Unique features or tactics for this platform]\n"
            "5. **Common Pitfalls**: [What to avoid]\n\n"
            "Remember, consistency and authenticity are key to success!"
        )
    
    def export_jsonl(self, examples: List[Dict[str, Any]], filepath: str) -> None:
        """
        Export training examples to JSONL format.
        
        Args:
            examples: Training examples
            filepath: Path to save the JSONL file
        """
        with open(filepath, 'w') as f:
            for example in examples:
                f.write(json.dumps(example) + '\n')
    
    def create_fine_tuning_dataset(
        self,
        additional_examples: List[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Create a complete fine-tuning dataset.
        
        Args:
            additional_examples: Additional custom examples
        
        Returns:
            Complete dataset with metadata
        """
        examples = self.generate_training_examples()
        
        if additional_examples:
            examples.extend(additional_examples)
        
        dataset = {
            "platform": self.platform,
            "num_examples": len(examples),
            "training_data": examples,
            "metadata": {
                "version": "1.0",
                "created_for": f"{self.platform} streaming",
                "data_type": "chat_completions"
            }
        }
        
        return dataset
    
    @staticmethod
    def validate_training_data(data: List[Dict[str, Any]]) -> bool:
        """
        Validate training data format.
        
        Args:
            data: Training data to validate
        
        Returns:
            True if valid, False otherwise
        """
        for item in data:
            if "messages" not in item:
                return False
            
            messages = item["messages"]
            if not isinstance(messages, list) or len(messages) < 2:
                return False
            
            for message in messages:
                if "role" not in message or "content" not in message:
                    return False
                
                if message["role"] not in ["system", "user", "assistant"]:
                    return False
        
        return True
