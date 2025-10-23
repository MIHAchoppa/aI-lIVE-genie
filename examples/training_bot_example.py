#!/usr/bin/env python3
"""
Example of using the Host Training Bot.
"""

from ai_live_genie import HostTrainingBot

def main():
    # Initialize training bot for Twitch
    print("Initializing Host Training Bot for Twitch...")
    bot = HostTrainingBot(platform="twitch")
    
    # Create a training plan
    print("\n=== Creating Training Plan ===")
    plan = bot.create_training_plan(
        experience_level="beginner",
        content_type="gaming",
        goals=[
            "Reach Twitch Affiliate",
            "Build a community of 100 regulars",
            "Stream consistently 3x per week"
        ]
    )
    print(plan["plan"])
    
    # Get real-time tips
    print("\n=== Getting Real-Time Tips ===")
    tips = bot.get_streaming_tips(
        "My chat is very quiet today with only 5 viewers. How do I keep them engaged?"
    )
    print(tips)
    
    # Analyze performance
    print("\n=== Analyzing Performance ===")
    metrics = {
        "average_viewers": 12,
        "peak_viewers": 25,
        "chat_messages": 150,
        "new_followers": 3,
        "stream_duration_minutes": 180
    }
    
    analysis = bot.analyze_performance(metrics)
    print(analysis["analysis"])
    
    # Get content ideas
    print("\n=== Content Ideas ===")
    ideas = bot.suggest_content_ideas(
        trending_topics=["Cozy gaming", "Speedruns", "Community events"],
        target_audience="18-35 gaming enthusiasts"
    )
    print("\n".join(ideas[:5]))  # Show first 5 ideas
    
    # Prepare for stream
    print("\n=== Stream Preparation ===")
    prep = bot.prepare_stream_session(
        stream_title="Chill Gaming Night - Let's Chat!",
        duration_minutes=120,
        special_events=["Follower milestone celebration", "Q&A segment"]
    )
    print(prep["preparation_plan"])

if __name__ == "__main__":
    main()
