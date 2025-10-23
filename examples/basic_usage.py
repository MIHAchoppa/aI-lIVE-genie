#!/usr/bin/env python3
"""
Basic usage example of AI Live Genie models.
"""

from ai_live_genie import GroqModel

def main():
    # Initialize a Twitch-focused model
    print("Initializing Twitch model...")
    twitch_model = GroqModel(platform="twitch")
    
    # Get streaming advice
    print("\n=== Getting Streaming Advice ===")
    advice = twitch_model.get_streaming_advice(
        "I'm a new streamer with low viewer count. How can I grow my audience?"
    )
    print(advice)
    
    # Get engagement strategy
    print("\n=== Getting Engagement Strategy ===")
    strategy = twitch_model.get_engagement_strategy(
        audience_size="small",
        goals="Increase followers and build a loyal community"
    )
    print(strategy)
    
    # Get monetization advice
    print("\n=== Getting Monetization Advice ===")
    monetization = twitch_model.get_monetization_advice(
        current_status="No affiliate yet, streaming for 2 months"
    )
    print(monetization)
    
    # Try with YouTube
    print("\n\n=== YouTube Model ===")
    youtube_model = GroqModel(platform="youtube")
    
    youtube_advice = youtube_model.get_streaming_advice(
        "How do I optimize my stream titles and descriptions for YouTube SEO?"
    )
    print(youtube_advice)

if __name__ == "__main__":
    main()
