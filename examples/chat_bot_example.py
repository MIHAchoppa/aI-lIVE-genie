#!/usr/bin/env python3
"""
Example of using the Stream Chat Bot with platform integration.
"""

import asyncio
from ai_live_genie.integrations import StreamChatBot, MockPlatformIntegration

async def main():
    print("=== Stream Chat Bot Example ===\n")
    
    # Initialize chat bot with mock integration
    print("Initializing chat bot for Twitch...")
    integration = MockPlatformIntegration(platform="twitch")
    chat_bot = StreamChatBot(
        platform="twitch",
        integration=integration
    )
    
    # Start the bot
    await chat_bot.start()
    
    # Get stream insights
    print("\n=== Current Stream Insights ===")
    insights = await chat_bot.get_stream_insights()
    
    print(f"Platform: {insights['platform']}")
    print(f"Stream Title: {insights['stream_info']['title']}")
    print(f"Viewer Count: {insights['stream_info']['viewer_count']}")
    print(f"Is Live: {insights['stream_info']['is_live']}")
    
    print("\nStream Analytics:")
    for key, value in insights['analytics'].items():
        if key != 'platform':
            print(f"  {key}: {value}")
    
    print("\nAI Insights:")
    print(insights['ai_insights'])
    
    # Test message processing
    print("\n=== Testing Message Processing ===")
    
    test_messages = [
        {
            "id": "1",
            "user": "TestViewer1",
            "message": "Hey bot, can you give me some streaming advice?",
            "timestamp": "2024-01-01T00:00:00Z"
        },
        {
            "id": "2",
            "user": "TestViewer2",
            "message": "What's the best way to grow on Twitch?",
            "timestamp": "2024-01-01T00:01:00Z"
        },
        {
            "id": "3",
            "user": "TestViewer3",
            "message": "Just here to watch!",  # Won't trigger bot
            "timestamp": "2024-01-01T00:02:00Z"
        }
    ]
    
    for message in test_messages:
        print(f"\nProcessing: '{message['message']}' from {message['user']}")
        response = await chat_bot.process_message(message)
        
        if response:
            print(f"Bot Response: {response[:200]}...")
        else:
            print("Bot Response: (No response needed)")
    
    # Suggest chat responses
    print("\n=== Chat Response Suggestions ===")
    
    scenarios = [
        "Someone is asking about my stream schedule",
        "A viewer just followed and wants to know about the community",
        "Chat is asking about my gaming setup"
    ]
    
    for scenario in scenarios:
        print(f"\nScenario: {scenario}")
        suggestion = await chat_bot.suggest_chat_response(scenario)
        print(f"Suggested Response: {suggestion[:150]}...")
    
    # Add custom message handler
    print("\n=== Testing Custom Message Handler ===")
    
    def custom_handler(message: dict) -> str:
        """Example custom handler for specific keywords."""
        text = message.get("message", "").lower()
        if "discord" in text:
            return "Join our Discord community at discord.gg/example!"
        return None
    
    chat_bot.add_message_handler(custom_handler)
    
    discord_message = {
        "id": "4",
        "user": "TestViewer4",
        "message": "Do you have a Discord server?",
        "timestamp": "2024-01-01T00:03:00Z"
    }
    
    response = await chat_bot.process_message(discord_message)
    print(f"Custom Handler Response: {response}")
    
    # Stop the bot
    print("\n=== Stopping Chat Bot ===")
    await chat_bot.stop()
    
    print("\nDemo completed!")

def run_async_demo():
    """Run the async demo."""
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nDemo interrupted by user")

if __name__ == "__main__":
    run_async_demo()
