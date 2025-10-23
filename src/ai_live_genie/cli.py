#!/usr/bin/env python3
"""
Command-line interface for AI Live Genie.
"""

import sys
import argparse
from .memory_manager import MemoryManager
from .streaming_data import StreamingPlatformData


def serve_api(args):
    """Start the API server."""
    from .api_server import app
    import os
    
    # Set API key if provided
    if args.api_key:
        os.environ['AI_GENIE_API_KEY'] = args.api_key
    
    print(f"🧞 Starting AI Live Genie API Server on {args.host}:{args.port}")
    print(f"   API Key: {os.environ.get('AI_GENIE_API_KEY', 'dev-key-change-in-production')}")
    print(f"   Debug mode: {args.debug}")
    print()
    
    app.run(host=args.host, port=args.port, debug=args.debug)


def calculate_earnings(args):
    """Calculate earnings for a platform."""
    streaming = StreamingPlatformData()
    
    result = streaming.calculate_earnings(args.platform, args.views)
    
    print(f"\n💰 Earnings for {result['platform'].upper()}")
    print(f"   Views: {result['views']:,}")
    print(f"   Estimated Earnings:")
    print(f"     Min:     ${result['estimated_earnings']['min']:.2f}")
    print(f"     Average: ${result['estimated_earnings']['average']:.2f}")
    print(f"     Max:     ${result['estimated_earnings']['max']:.2f}")
    print()


def compare_platforms(args):
    """Compare earnings across all platforms."""
    streaming = StreamingPlatformData()
    
    comparison = streaming.compare_platforms(args.views)
    
    print(f"\n📊 Platform Comparison for {args.views:,} views")
    print("=" * 60)
    
    for i, result in enumerate(comparison, 1):
        print(f"{i}. {result['platform'].upper():20} ${result['estimated_earnings']['average']:8.2f}")
    print()


def list_platforms(args):
    """List all supported platforms."""
    streaming = StreamingPlatformData()
    platforms = streaming.get_all_platforms()
    
    print("\n🌐 Supported Platforms:")
    print("=" * 60)
    
    for platform in sorted(platforms):
        data = streaming.get_platform_data(platform)
        # Some platforms use "streams" instead of "views"
        payout_key = 'payout_per_1000_streams' if 'payout_per_1000_streams' in data else 'payout_per_1000_views'
        payout = data[payout_key]
        unit = 'streams' if 'streams' in payout_key else 'views'
        print(f"  • {data['name']:20} ${payout['average']:.2f}/1K {unit}")
    print()


def create_goal(args):
    """Create a new goal."""
    memory = MemoryManager()
    
    goal = memory.goals.add_goal(
        title=args.title,
        description=args.description or "",
        priority=args.priority
    )
    
    print(f"\n🎯 Goal Created!")
    print(f"   ID: {goal['id']}")
    print(f"   Title: {goal['title']}")
    print(f"   Priority: {goal['priority']}")
    print()


def list_goals(args):
    """List all active goals."""
    memory = MemoryManager()
    goals = memory.goals.get_active_goals()
    
    if not goals:
        print("\n📋 No active goals found.")
        return
    
    print(f"\n📋 Active Goals ({len(goals)}):")
    print("=" * 60)
    
    for goal in goals:
        print(f"  [{goal['priority'].upper()}] {goal['title']}")
        print(f"     Progress: {goal['progress']}%")
        if goal.get('description'):
            print(f"     {goal['description']}")
        print()


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="AI Live Genie - Memory Management and Streaming Analytics",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Start API server
  ai-live-genie serve --port 5000

  # Calculate earnings
  ai-live-genie earnings youtube 50000

  # Compare platforms
  ai-live-genie compare 100000

  # List platforms
  ai-live-genie platforms

  # Create a goal
  ai-live-genie goal create "Reach 10k subs" --priority high

  # List goals
  ai-live-genie goal list
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to run')
    
    # Serve command
    serve_parser = subparsers.add_parser('serve', help='Start the API server')
    serve_parser.add_argument('--host', default='127.0.0.1', help='Host to bind to')
    serve_parser.add_argument('--port', type=int, default=5000, help='Port to bind to')
    serve_parser.add_argument('--api-key', help='API key for authentication')
    serve_parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    serve_parser.set_defaults(func=serve_api)
    
    # Earnings command
    earnings_parser = subparsers.add_parser('earnings', help='Calculate earnings for a platform')
    earnings_parser.add_argument('platform', help='Platform name (e.g., youtube, twitch)')
    earnings_parser.add_argument('views', type=int, help='Number of views/streams')
    earnings_parser.set_defaults(func=calculate_earnings)
    
    # Compare command
    compare_parser = subparsers.add_parser('compare', help='Compare earnings across platforms')
    compare_parser.add_argument('views', type=int, help='Number of views to compare')
    compare_parser.set_defaults(func=compare_platforms)
    
    # Platforms command
    platforms_parser = subparsers.add_parser('platforms', help='List all supported platforms')
    platforms_parser.set_defaults(func=list_platforms)
    
    # Goal commands
    goal_parser = subparsers.add_parser('goal', help='Manage goals')
    goal_subparsers = goal_parser.add_subparsers(dest='goal_command')
    
    goal_create = goal_subparsers.add_parser('create', help='Create a new goal')
    goal_create.add_argument('title', help='Goal title')
    goal_create.add_argument('--description', help='Goal description')
    goal_create.add_argument('--priority', default='medium', choices=['low', 'medium', 'high'])
    goal_create.set_defaults(func=create_goal)
    
    goal_list = goal_subparsers.add_parser('list', help='List all active goals')
    goal_list.set_defaults(func=list_goals)
    
    # Parse args
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Execute command
    if hasattr(args, 'func'):
        try:
            args.func(args)
            return 0
        except KeyboardInterrupt:
            print("\n\nInterrupted by user.")
            return 130
        except Exception as e:
            print(f"\n❌ Error: {e}", file=sys.stderr)
            return 1
    else:
        parser.print_help()
        return 1


if __name__ == '__main__':
    sys.exit(main())
