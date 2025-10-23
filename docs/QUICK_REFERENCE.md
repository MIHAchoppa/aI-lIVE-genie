# Quick Reference Card

## Installation

```bash
# Basic installation
pip install -e .

# With API server
pip install -e ".[api]"

# With dev tools
pip install -e ".[dev]"
```

## CLI Commands

```bash
# Start API server
ai-live-genie serve [--port 5000] [--api-key KEY]

# Calculate earnings
ai-live-genie earnings <platform> <views>
# Example: ai-live-genie earnings youtube 50000

# Compare platforms
ai-live-genie compare <views>
# Example: ai-live-genie compare 100000

# List platforms
ai-live-genie platforms

# Create goal
ai-live-genie goal create "TITLE" [--priority high|medium|low]

# List goals
ai-live-genie goal list
```

## Python Library

### Import
```python
from ai_live_genie import (
    MemoryManager,
    StreamingPlatformData,
    ConversationalMemory,
    LongTermMemory,
    GoalsManager
)
```

### Memory Management
```python
# Initialize
memory = MemoryManager()

# Add conversation
memory.process_interaction(
    "User message",
    "Assistant response"
)

# Store fact
memory.long_term.store_fact("Important info", category="general")

# Store preference
memory.long_term.store_preference("theme", "dark")

# Create goal
goal = memory.goals.add_goal(
    "Reach 10k subs",
    "YouTube milestone",
    priority="high"
)

# Update progress
memory.goals.update_goal_progress(goal['id'], 50)
```

### Streaming Data
```python
streaming = StreamingPlatformData()

# Get platform info
data = streaming.get_platform_data("youtube")

# Calculate earnings
earnings = streaming.calculate_earnings("youtube", 50000)
# Returns: {platform, views, estimated_earnings: {min, max, average}}

# Compare all platforms
comparison = streaming.compare_platforms(100000)

# Calculate expected subscribers
subs = streaming.calculate_subscribers_from_views("youtube", 10000)

# Get requirements
requirements = streaming.get_monetization_requirements("youtube")
```

## REST API

### Base URL
```
http://localhost:5000
```

### Authentication
```bash
# Header (recommended)
X-API-Key: your-api-key

# Query parameter
?api_key=your-api-key
```

### Common Endpoints

#### Calculate Earnings (No Auth)
```bash
GET /api/streaming/earnings?platform=youtube&views=50000
```

#### Compare Platforms (No Auth)
```bash
GET /api/streaming/compare?views=100000
```

#### Store Conversation (Auth Required)
```bash
POST /api/conversation/interaction
Body: {
  "user_input": "Question",
  "assistant_response": "Answer"
}
```

#### Create Goal (Auth Required)
```bash
POST /api/goals
Body: {
  "title": "Goal title",
  "description": "Description",
  "priority": "high"
}
```

#### Get Goals (Auth Required)
```bash
GET /api/goals
```

## Development

### Run Tests
```bash
make test                # Run all tests
make test-coverage       # Run with coverage report
python tests/test_memory_system.py  # Specific test
```

### Code Quality
```bash
make format             # Format with Black
make lint               # Run Pylint
make format-check       # Check formatting
```

### Build
```bash
make build              # Build distribution
make clean              # Clean artifacts
```

## Platform Payout Quick Reference

| Platform | Per 1K | Best For |
|----------|--------|----------|
| Apple Music | $7.50 | Music streaming |
| Spotify | $4.00 | Music streaming |
| Twitch | $3.50 | Live gaming/streams |
| YouTube | $1.50 | Video content |
| Instagram | $0.50 | Reels/Stories |
| TikTok | $0.03 | Short videos |
| Facebook Gaming | $0.01 | Gaming streams |

## Conversion Rates

### Views to Subscribers
- YouTube: 2% avg, 5% good, 10% excellent
- Twitch: 1.5% avg, 4% good, 8% excellent

### Engagement
- TikTok: 6% avg, 12% good, 20% excellent
- YouTube: 4% avg, 8% good, 15% excellent
- Instagram: 3% avg, 6% good, 12% excellent

## Environment Variables

```bash
# API server
export AI_GENIE_API_KEY="your-key"
export API_HOST="0.0.0.0"
export API_PORT="5000"
export API_DEBUG="False"
```

## File Locations

```
./data/long_term_memory.json    # Facts, preferences, entities
./data/goals.json                # Active and completed goals
```

## Common Use Cases

### For Content Creators
```python
# Calculate potential earnings
streaming = StreamingPlatformData()
earnings = streaming.calculate_earnings("youtube", 50000)

# Set growth goal
memory = MemoryManager()
memory.goals.add_goal("Reach 10k subs", priority="high")
```

### For AI Assistants
```python
# Maintain context
memory = MemoryManager()
memory.process_interaction(user_msg, ai_response)

# Remember preferences
memory.long_term.store_preference("platform", "YouTube")
```

### For Agencies
```python
# Track client channels
memory.long_term.store_entity("client1_youtube", {
    "subscribers": 5000,
    "avg_views": 2000
})

# Compare opportunities
comparison = streaming.compare_platforms(100000)
```

## Troubleshooting

### Module not found
```bash
pip install -e .
```

### Tests failing
```bash
make clean
pip install -e ".[dev]"
make test
```

### API authentication fails
```bash
export AI_GENIE_API_KEY="your-key"
# Or use --api-key flag with CLI
```

## Resources

- 📖 [Full Documentation](../README.md)
- 🚀 [Quick Start Guide](QUICKSTART.md)
- 🔧 [API Reference](API_DOCUMENTATION.md)
- 🤝 [Contributing](../CONTRIBUTING.md)
- 🔒 [Security Policy](../SECURITY.md)

---

**Version 1.0.0** | [GitHub Repository](https://github.com/MIHAchoppa/aI-lIVE-genie)
