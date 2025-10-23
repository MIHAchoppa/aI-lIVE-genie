# Quick Start Guide - AI Live Genie

## Installation
```bash
git clone https://github.com/MIHAchoppa/aI-lIVE-genie.git
cd aI-lIVE-genie
python example_usage.py  # Run the demo
```

## 5-Minute Quick Start

### 1. Basic Memory Usage
```python
from memory_manager import MemoryManager

# Initialize
memory = MemoryManager()

# Store a conversation
memory.process_interaction(
    "What's the best platform for new streamers?",
    "YouTube is great for beginners due to its large audience and lower barriers to entry."
)

# Store important info
memory.long_term.store_fact("User focuses on gaming content")
memory.long_term.store_preference("streaming_time", "evenings")
```

### 2. Track Your Goals
```python
# Create a goal
goal = memory.goals.add_goal(
    "Reach 1000 subscribers",
    "First monetization milestone",
    priority="high",
    target_date="2025-12-31"
)

# Update progress
memory.goals.update_goal_progress(goal['id'], 30)  # 30% complete
```

### 3. Calculate Earnings
```python
from streaming_data import StreamingPlatformData

streaming = StreamingPlatformData()

# Calculate for single platform
earnings = streaming.calculate_earnings("youtube", 10000)
print(f"10K views on YouTube: ${earnings['estimated_earnings']['average']}")

# Compare all platforms
comparison = streaming.compare_platforms(10000)
for result in comparison[:3]:  # Top 3
    print(f"{result['platform']}: ${result['estimated_earnings']['average']}")
```

### 4. Get Conversion Insights
```python
# How many subscribers from 10K views?
subs = streaming.calculate_subscribers_from_views("youtube", 10000)
print(f"Expected subscribers: {subs}")

# What do I need to monetize on YouTube?
requirements = streaming.get_monetization_requirements("youtube")
print(requirements)
# Output: {'subscribers': 1000, 'watch_hours_12_months': 4000}
```

## Common Use Cases

### For New Streamers
```python
# Find the best starting platform
streaming = StreamingPlatformData()
comparison = streaming.compare_platforms(5000)  # Expected monthly views
best_platform = comparison[0]
print(f"Start with: {best_platform['platform']}")
print(f"Potential earnings: ${best_platform['estimated_earnings']['average']}/month")
```

### For Multi-Platform Creators
```python
memory = MemoryManager()

# Track each platform
memory.long_term.store_entity("youtube_channel", {
    "subscribers": 5000,
    "avg_monthly_views": 50000
})
memory.long_term.store_entity("twitch_channel", {
    "followers": 2000,
    "avg_concurrent_viewers": 100
})

# Compare earnings
youtube_earnings = streaming.calculate_earnings("youtube", 50000)
# Calculate based on your actual numbers
```

### For Growth Planning
```python
memory = MemoryManager()

# Set your growth goal
memory.goals.add_goal(
    "Double monthly revenue",
    "Increase from $500 to $1000/month",
    priority="high"
)

# What views do you need?
# For YouTube at $1.50 per 1000 views to earn $1000:
needed_views = (1000 / 1.50) * 1000
print(f"Need ~{needed_views:.0f} views/month")

# Track it
memory.goals.add_milestone(1, f"Reach {needed_views:.0f} views/month")
```

## Platform Quick Reference

### Best for Music
- **Apple Music**: $7.50 per 1K streams
- **Spotify**: $4.00 per 1K streams

### Best for Video
- **Twitch**: $3.50 per 1K views + subs + bits
- **YouTube**: $1.50 per 1K views + memberships

### Easiest to Start
- **YouTube**: 1K subs + 4K watch hours
- **TikTok**: 10K followers + 100K views/30 days

### Highest Engagement
- **TikTok**: 6% average engagement
- **Instagram**: 3% average engagement

## Tips

1. **Start tracking early**: Memory helps you make better decisions over time
2. **Set realistic goals**: Use conversion rates to set achievable targets
3. **Diversify platforms**: Don't rely on just one income source
4. **Track your data**: Use the memory system to record what works
5. **Review regularly**: Check your progress weekly

## Next Steps

- Run `python example_usage.py` to see everything in action
- Read the full [README.md](README.md) for detailed API documentation
- Run `python test_memory_system.py` to verify your installation

## Support

Need help? Check the [main README](README.md) or open an issue on GitHub.
