#!/usr/bin/env python3
"""
Example of using the Platform Manager for multi-platform support.
"""

from ai_live_genie import PlatformManager

def main():
    # Initialize platform manager
    print("Initializing Platform Manager...")
    manager = PlatformManager()
    
    # List all supported platforms
    print("\n=== Supported Platforms ===")
    platforms = manager.get_all_platforms()
    for platform in platforms:
        print(f"  - {platform}")
    
    # Get platform information
    print("\n=== Platform Information ===")
    for platform in ["twitch", "youtube", "kick"]:
        info = manager.get_platform_info(platform)
        print(f"\n{info['name']}:")
        print(f"  Description: {info['description']}")
        print(f"  Monetization: {info['monetization']}")
        print(f"  Features: {info['features']}")
    
    # Get models for different platforms
    print("\n=== Testing Different Platform Models ===")
    
    twitch_model = manager.get_model("twitch")
    print("\nTwitch advice:")
    print(twitch_model.get_streaming_advice("Best time to stream on weekdays?"))
    
    youtube_model = manager.get_model("youtube")
    print("\nYouTube advice:")
    print(youtube_model.get_streaming_advice("How to get more concurrent viewers?"))
    
    # Compare platforms
    print("\n=== Platform Comparison ===")
    comparison = manager.compare_platforms(
        platforms=["twitch", "youtube", "kick"],
        criteria="revenue potential and growth opportunities for new streamers"
    )
    print(comparison)
    
    # Check platform support
    print("\n=== Platform Support Check ===")
    test_platforms = ["twitch", "mixer", "tiktok"]
    for platform in test_platforms:
        supported = manager.is_platform_supported(platform)
        print(f"{platform}: {'✓ Supported' if supported else '✗ Not Supported'}")

if __name__ == "__main__":
    main()
