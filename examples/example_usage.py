"""
Example usage of the AI Live Genie Memory and Streaming Data systems.
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ai_live_genie import MemoryManager, StreamingPlatformData


def demo_conversational_memory():
    """Demonstrate conversational memory usage."""
    print("=" * 60)
    print("CONVERSATIONAL MEMORY DEMO")
    print("=" * 60)
    
    memory = MemoryManager()
    
    # Simulate a conversation
    print("\n1. Starting a conversation...")
    memory.process_interaction(
        "Hi! I'm a new streamer on YouTube.",
        "Hello! Welcome! I'd be happy to help you with your streaming journey."
    )
    
    memory.process_interaction(
        "How much can I earn per 1000 views?",
        "On YouTube, you can typically earn between $0.25 to $4.00 per 1000 views, with an average of $1.50."
    )
    
    memory.process_interaction(
        "What about Twitch?",
        "Twitch typically pays $2.00 to $10.00 per 1000 views, averaging $3.50, plus subscriptions and bits."
    )
    
    # Retrieve conversation history
    history = memory.conversational.get_history(last_n=3)
    print(f"\nConversation history ({len(history)} messages):")
    for msg in history:
        print(f"  [{msg['role']}]: {msg['content']}")
    
    print("\n" + memory.conversational.get_context_summary())


def demo_long_term_memory():
    """Demonstrate long-term memory usage."""
    print("\n" + "=" * 60)
    print("LONG-TERM MEMORY DEMO")
    print("=" * 60)
    
    memory = MemoryManager()
    
    # Store facts
    print("\n1. Storing facts...")
    memory.long_term.store_fact(
        "User is a gaming streamer focusing on Minecraft and Fortnite",
        category="user_profile"
    )
    memory.long_term.store_fact(
        "User streams 3 times per week on average",
        category="streaming_schedule"
    )
    
    # Store preferences
    print("2. Storing preferences...")
    memory.long_term.store_preference("preferred_platform", "YouTube")
    memory.long_term.store_preference("streaming_days", ["Monday", "Wednesday", "Friday"])
    memory.long_term.store_preference("target_monthly_income", 1000)
    
    # Store entities
    print("3. Storing entity information...")
    memory.long_term.store_entity("main_channel", {
        "platform": "YouTube",
        "name": "GamerPro123",
        "subscribers": 5000,
        "avg_views_per_video": 2000
    })
    
    # Retrieve information
    print("\n4. Retrieving stored information:")
    facts = memory.long_term.retrieve_facts(category="user_profile")
    print(f"   User profile facts: {len(facts)} found")
    for fact in facts:
        print(f"     - {fact['content']}")
    
    preferred_platform = memory.long_term.retrieve_preference("preferred_platform")
    print(f"   Preferred platform: {preferred_platform}")
    
    channel_info = memory.long_term.retrieve_entity("main_channel")
    print(f"   Main channel: {channel_info['name']} on {channel_info['platform']}")
    print(f"     Subscribers: {channel_info['subscribers']}")
    print(f"     Avg views: {channel_info['avg_views_per_video']}")
    
    # Search memory
    print("\n5. Searching memory for 'streaming':")
    results = memory.long_term.search_memory("streaming")
    for result in results:
        print(f"   - Type: {result['type']}")
        if result['type'] == 'fact':
            print(f"     Content: {result['data']['content']}")


def demo_goals():
    """Demonstrate goals management."""
    print("\n" + "=" * 60)
    print("GOALS MANAGEMENT DEMO")
    print("=" * 60)
    
    memory = MemoryManager()
    
    # Add goals
    print("\n1. Creating goals...")
    goal1 = memory.goals.add_goal(
        "Reach 10,000 subscribers",
        "Grow YouTube channel to 10k subscribers to unlock better monetization",
        priority="high",
        target_date="2025-12-31"
    )
    print(f"   Created goal: {goal1['title']}")
    
    goal2 = memory.goals.add_goal(
        "Stream consistently",
        "Maintain 3 streams per week for 3 months",
        priority="high"
    )
    print(f"   Created goal: {goal2['title']}")
    
    goal3 = memory.goals.add_goal(
        "Earn $500/month",
        "Reach monthly income of $500 from streaming",
        priority="medium",
        target_date="2025-06-30"
    )
    print(f"   Created goal: {goal3['title']}")
    
    # Add milestones
    print("\n2. Adding milestones...")
    memory.goals.add_milestone(goal1['id'], "Reach 5,000 subscribers")
    memory.goals.add_milestone(goal1['id'], "Reach 7,500 subscribers")
    print(f"   Added 2 milestones to goal: {goal1['title']}")
    
    # Update progress
    print("\n3. Updating goal progress...")
    memory.goals.update_goal_progress(goal1['id'], 45)
    memory.goals.update_goal_progress(goal2['id'], 60)
    print("   Progress updated for goals")
    
    # Display active goals
    print("\n4. Active goals:")
    active_goals = memory.goals.get_active_goals()
    for goal in active_goals:
        print(f"   [{goal['priority']}] {goal['title']}")
        print(f"     Progress: {goal['progress']}%")
        print(f"     Description: {goal['description']}")
        if goal.get('milestones'):
            print(f"     Milestones: {len(goal['milestones'])}")


def demo_streaming_data():
    """Demonstrate streaming platform data."""
    print("\n" + "=" * 60)
    print("STREAMING PLATFORM DATA DEMO")
    print("=" * 60)
    
    streaming = StreamingPlatformData()
    
    # Get platform information
    print("\n1. Available platforms:")
    platforms = streaming.get_all_platforms()
    for platform in platforms:
        print(f"   - {platform}")
    
    # Get specific platform data
    print("\n2. YouTube platform details:")
    youtube_data = streaming.get_platform_data("youtube")
    print(f"   Name: {youtube_data['name']}")
    print(f"   Payout per 1000 views:")
    payout = youtube_data['payout_per_1000_views']
    print(f"     Min: ${payout['min']}")
    print(f"     Average: ${payout['average']}")
    print(f"     Max: ${payout['max']}")
    
    # Calculate earnings
    print("\n3. Calculating earnings for 50,000 views:")
    views = 50000
    for platform in ["youtube", "twitch", "spotify"]:
        earnings = streaming.calculate_earnings(platform, views)
        if "error" not in earnings:
            est = earnings['estimated_earnings']
            print(f"   {platform.capitalize()}:")
            print(f"     Min: ${est['min']}")
            print(f"     Average: ${est['average']}")
            print(f"     Max: ${est['max']}")
    
    # Compare platforms
    print("\n4. Platform comparison for 100,000 views:")
    comparison = streaming.compare_platforms(100000)
    print("   Ranked by average earnings:")
    for i, result in enumerate(comparison[:5], 1):
        est = result['estimated_earnings']
        print(f"   {i}. {result['platform']}: ${est['average']} (avg)")
    
    # Get conversion rates
    print("\n5. Conversion rates (View to Subscriber):")
    conversion = streaming.get_conversion_rates("view_to_subscriber")
    if conversion:
        for platform, rates in conversion.items():
            print(f"   {platform}:")
            print(f"     Average: {rates['average']*100}%")
            print(f"     Good: {rates['good']*100}%")
    
    # Calculate subscribers from views
    print("\n6. Expected subscribers from 10,000 views:")
    for platform in ["youtube", "twitch"]:
        subs = streaming.calculate_subscribers_from_views(platform, 10000, "average")
        print(f"   {platform}: ~{subs} subscribers")
    
    # Get monetization requirements
    print("\n7. YouTube monetization requirements:")
    requirements = streaming.get_monetization_requirements("youtube")
    if requirements:
        for key, value in requirements.items():
            print(f"   {key.replace('_', ' ').title()}: {value}")


def demo_integrated_usage():
    """Demonstrate integrated usage of all systems."""
    print("\n" + "=" * 60)
    print("INTEGRATED SYSTEM DEMO")
    print("=" * 60)
    
    memory = MemoryManager()
    streaming = StreamingPlatformData()
    
    # Simulate a comprehensive interaction
    print("\n1. User inquiry about platform choice:")
    user_msg = "I have 50,000 views per month. Which platform should I focus on?"
    print(f"   User: {user_msg}")
    
    # Calculate earnings across platforms
    comparison = streaming.compare_platforms(50000)
    top_platform = comparison[0]
    
    response = f"Based on 50,000 monthly views, {top_platform['platform']} offers the best earnings potential with an average of ${top_platform['estimated_earnings']['average']} per month."
    print(f"   Assistant: {response}")
    
    # Store in conversational memory
    memory.process_interaction(user_msg, response)
    
    # Store in long-term memory
    memory.long_term.store_preference("monthly_views", 50000)
    memory.long_term.store_preference("recommended_platform", top_platform['platform'])
    
    # Create a goal based on the interaction
    memory.goals.add_goal(
        f"Optimize {top_platform['platform']} earnings",
        f"Focus on {top_platform['platform']} to maximize revenue from current viewership",
        priority="high"
    )
    
    print("\n2. Getting full context:")
    context = memory.get_full_context()
    print(f"   Recent conversation messages: {len(context['conversation_history'])}")
    print(f"   Active goals: {len(context['active_goals'])}")
    print(f"   Stored preferences: {len(context['preferences'])}")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("AI LIVE GENIE - MEMORY & STREAMING DATA SYSTEM")
    print("Demonstration of all features")
    print("=" * 60)
    
    # Run all demos
    demo_conversational_memory()
    demo_long_term_memory()
    demo_goals()
    demo_streaming_data()
    demo_integrated_usage()
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETE")
    print("=" * 60)
    print("\nAll data has been saved to:")
    print("  - ./data/long_term_memory.json")
    print("  - ./data/goals.json")
    print("\nYou can inspect these files to see the persisted data.")
