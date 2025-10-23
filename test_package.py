#!/usr/bin/env python3
"""
Test script to verify package structure without requiring Groq API.
"""

def test_imports():
    """Test that all modules can be imported."""
    print("Testing module imports...")
    
    # Test config
    try:
        from ai_live_genie import config
        print("✓ Config module imported")
    except ImportError as e:
        print(f"✗ Config import failed: {e}")
        return False
    
    # Test utils
    try:
        from ai_live_genie.utils import helpers
        print("✓ Utils module imported")
    except ImportError as e:
        print(f"✗ Utils import failed: {e}")
        return False
    
    # Test platforms
    try:
        from ai_live_genie.platforms import platform_manager
        print("✓ Platform manager module imported")
    except ImportError as e:
        print(f"✗ Platform manager import failed: {e}")
        return False
    
    # Test fine-tuning
    try:
        from ai_live_genie.fine_tuning import training_data_generator, model_fine_tuner
        print("✓ Fine-tuning modules imported")
    except ImportError as e:
        print(f"✗ Fine-tuning import failed: {e}")
        return False
    
    # Test integrations
    try:
        from ai_live_genie.integrations import base_integration
        print("✓ Integration modules imported")
    except ImportError as e:
        print(f"✗ Integration import failed: {e}")
        return False
    
    return True


def test_config():
    """Test configuration."""
    print("\nTesting configuration...")
    
    from ai_live_genie.config import TRAINING_TEMPLATES, PLATFORM_STRATEGIES
    
    platforms = list(TRAINING_TEMPLATES.keys())
    print(f"✓ Training templates for {len(platforms)} platforms")
    print(f"  Platforms: {', '.join(platforms)}")
    
    levels = list(PLATFORM_STRATEGIES.keys())
    print(f"✓ Strategies for {len(levels)} experience levels")
    print(f"  Levels: {', '.join(levels)}")


def test_platform_manager():
    """Test platform manager without API."""
    print("\nTesting platform manager...")
    
    from ai_live_genie.platforms.platform_manager import PlatformManager
    
    manager = PlatformManager()
    platforms = manager.get_all_platforms()
    print(f"✓ Platform manager initialized")
    print(f"  Supported platforms: {', '.join(platforms)}")
    
    # Test platform info
    info = manager.get_platform_info("twitch")
    print(f"✓ Platform info retrieved for Twitch")
    print(f"  Name: {info['name']}")
    print(f"  Monetization: {info['monetization']}")
    
    # Test platform support check
    assert manager.is_platform_supported("twitch")
    assert not manager.is_platform_supported("invalid_platform")
    print(f"✓ Platform support checks working")
    
    # Note: Skipping model creation test as it requires Groq API
    print(f"  (Model creation tests skipped - requires Groq API)")


def test_fine_tuning():
    """Test fine-tuning utilities."""
    print("\nTesting fine-tuning utilities...")
    
    from ai_live_genie.fine_tuning import TrainingDataGenerator, ModelFineTuner
    
    # Test data generator
    generator = TrainingDataGenerator(platform="twitch")
    examples = generator.generate_training_examples(num_examples=5)
    print(f"✓ Training data generator created {len(examples)} examples")
    
    # Validate data
    is_valid = TrainingDataGenerator.validate_training_data(examples)
    print(f"✓ Training data validation: {'passed' if is_valid else 'failed'}")
    
    # Test fine-tuner
    tuner = ModelFineTuner(platform="youtube")
    estimates = tuner.estimate_training_time(num_examples=100)
    print(f"✓ Fine-tuning estimates calculated")
    print(f"  Estimated time: {estimates['estimated_hours']} hours")


def test_integration_base():
    """Test integration base classes."""
    print("\nTesting integration base classes...")
    
    from ai_live_genie.integrations.base_integration import MockPlatformIntegration
    import asyncio
    
    async def run_integration_test():
        integration = MockPlatformIntegration(platform="twitch")
        
        # Test connection
        connected = await integration.connect()
        print(f"✓ Mock integration connected: {connected}")
        
        # Test stream info
        info = await integration.get_stream_info()
        print(f"✓ Stream info retrieved: {info['title']}")
        
        # Test viewer count
        viewers = await integration.get_viewer_count()
        print(f"✓ Viewer count: {viewers}")
        
        # Test analytics
        analytics = await integration.get_analytics()
        print(f"✓ Analytics retrieved: {len(analytics)} metrics")
        
        await integration.disconnect()
    
    asyncio.run(run_integration_test())


def test_helpers():
    """Test utility helpers."""
    print("\nTesting utility helpers...")
    
    from ai_live_genie.utils.helpers import (
        calculate_engagement_rate,
        parse_metrics_summary,
        format_conversation_history
    )
    
    # Test engagement rate
    rate = calculate_engagement_rate(interactions=100, viewers=50)
    print(f"✓ Engagement rate calculation: {rate}%")
    
    # Test metrics summary
    metrics = {"viewers": 50, "followers": 10, "messages": 150}
    summary = parse_metrics_summary(metrics)
    print(f"✓ Metrics summary generated")
    
    # Test conversation formatting
    messages = [{"role": "user", "content": f"Message {i}"} for i in range(20)]
    formatted = format_conversation_history(messages, max_messages=5)
    print(f"✓ Conversation history formatted: {len(formatted)} messages")


def main():
    """Run all tests."""
    print("=" * 60)
    print("AI Live Genie - Package Structure Tests")
    print("=" * 60)
    
    tests = [
        ("Module Imports", test_imports),
        ("Configuration", test_config),
        ("Platform Manager", test_platform_manager),
        ("Fine-Tuning", test_fine_tuning),
        ("Integration Base", test_integration_base),
        ("Utility Helpers", test_helpers),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            if result is False:
                print(f"\n✗ {test_name} FAILED")
                failed += 1
            else:
                passed += 1
        except Exception as e:
            print(f"\n✗ {test_name} FAILED with exception: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    if failed == 0:
        print("\n✓ All tests passed!")
        return 0
    else:
        print(f"\n✗ {failed} test(s) failed")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
