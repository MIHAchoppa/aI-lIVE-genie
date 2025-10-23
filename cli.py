#!/usr/bin/env python3
"""
Command-line interface for AI Live Genie.
"""

import argparse
import sys
from ai_live_genie import GroqModel, HostTrainingBot, PlatformManager


def cmd_advice(args):
    """Get streaming advice."""
    model = GroqModel(platform=args.platform)
    advice = model.get_streaming_advice(args.query)
    print(f"\n{advice}\n")


def cmd_training_plan(args):
    """Create a training plan."""
    bot = HostTrainingBot(platform=args.platform)
    
    goals = args.goals.split(',') if args.goals else [
        "Grow audience",
        "Improve engagement",
        "Consistent streaming"
    ]
    
    plan = bot.create_training_plan(
        experience_level=args.level,
        content_type=args.content_type,
        goals=goals
    )
    
    print(f"\n=== Training Plan for {args.platform.title()} ===\n")
    print(plan["plan"])
    print()


def cmd_analyze(args):
    """Analyze streaming performance."""
    bot = HostTrainingBot(platform=args.platform)
    
    # Parse metrics from command line
    metrics = {}
    if args.metrics:
        for metric in args.metrics.split(','):
            key, value = metric.split('=')
            try:
                metrics[key.strip()] = float(value.strip())
            except ValueError:
                metrics[key.strip()] = value.strip()
    
    if not metrics:
        # Use example metrics
        metrics = {
            "average_viewers": 20,
            "peak_viewers": 35,
            "chat_messages": 150,
            "new_followers": 5
        }
        print("Using example metrics (provide your own with --metrics)")
    
    analysis = bot.analyze_performance(metrics)
    
    print(f"\n=== Performance Analysis for {args.platform.title()} ===\n")
    print(analysis["analysis"])
    print()


def cmd_platforms(args):
    """List supported platforms."""
    manager = PlatformManager()
    platforms = manager.get_all_platforms()
    
    print("\n=== Supported Platforms ===\n")
    
    for platform in platforms:
        info = manager.get_platform_info(platform)
        print(f"{info['name']}:")
        print(f"  {info['description']}")
        print(f"  Monetization: {info['monetization']}")
        print()


def cmd_compare(args):
    """Compare platforms."""
    manager = PlatformManager()
    platforms = args.platforms.split(',')
    
    comparison = manager.compare_platforms(
        platforms=[p.strip() for p in platforms],
        criteria=args.criteria
    )
    
    print(f"\n=== Platform Comparison ===\n")
    print(comparison)
    print()


def cmd_content_ideas(args):
    """Generate content ideas."""
    bot = HostTrainingBot(platform=args.platform)
    
    trending = args.trending.split(',') if args.trending else None
    
    ideas = bot.suggest_content_ideas(
        trending_topics=trending,
        target_audience=args.audience
    )
    
    print(f"\n=== Content Ideas for {args.platform.title()} ===\n")
    for i, idea in enumerate(ideas[:10], 1):
        print(f"{i}. {idea}")
    print()


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="AI Live Genie - AI-powered streaming assistant",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Get streaming advice
  python cli.py advice twitch "How do I grow my audience?"
  
  # Create a training plan
  python cli.py training twitch --level beginner --content gaming
  
  # Analyze performance
  python cli.py analyze twitch --metrics "viewers=25,followers=5"
  
  # List platforms
  python cli.py platforms
  
  # Compare platforms
  python cli.py compare --platforms "twitch,youtube,kick"
  
  # Generate content ideas
  python cli.py ideas twitch --trending "cozy gaming,speedruns"
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to run')
    
    # Advice command
    advice_parser = subparsers.add_parser('advice', help='Get streaming advice')
    advice_parser.add_argument('platform', help='Streaming platform')
    advice_parser.add_argument('query', help='Your question or situation')
    advice_parser.set_defaults(func=cmd_advice)
    
    # Training plan command
    training_parser = subparsers.add_parser('training', help='Create training plan')
    training_parser.add_argument('platform', help='Streaming platform')
    training_parser.add_argument('--level', default='beginner',
                                choices=['beginner', 'intermediate', 'advanced'],
                                help='Experience level')
    training_parser.add_argument('--content', dest='content_type', default='gaming',
                                help='Content type (gaming, creative, IRL, etc.)')
    training_parser.add_argument('--goals', help='Comma-separated goals')
    training_parser.set_defaults(func=cmd_training_plan)
    
    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze performance')
    analyze_parser.add_argument('platform', help='Streaming platform')
    analyze_parser.add_argument('--metrics', help='Comma-separated metrics (key=value)')
    analyze_parser.set_defaults(func=cmd_analyze)
    
    # Platforms command
    platforms_parser = subparsers.add_parser('platforms', help='List platforms')
    platforms_parser.set_defaults(func=cmd_platforms)
    
    # Compare command
    compare_parser = subparsers.add_parser('compare', help='Compare platforms')
    compare_parser.add_argument('--platforms', required=True,
                               help='Comma-separated platforms')
    compare_parser.add_argument('--criteria', default='revenue and growth',
                               help='Comparison criteria')
    compare_parser.set_defaults(func=cmd_compare)
    
    # Content ideas command
    ideas_parser = subparsers.add_parser('ideas', help='Generate content ideas')
    ideas_parser.add_argument('platform', help='Streaming platform')
    ideas_parser.add_argument('--trending', help='Comma-separated trending topics')
    ideas_parser.add_argument('--audience', help='Target audience description')
    ideas_parser.set_defaults(func=cmd_content_ideas)
    
    # Parse arguments
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    try:
        args.func(args)
        return 0
    except Exception as e:
        print(f"\nError: {e}\n", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
