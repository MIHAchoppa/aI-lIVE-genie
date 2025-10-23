# aI-lIVE-genie

AI-powered assistant for live streamers and content creators with comprehensive memory management and streaming platform analytics.

## Features

### 🌐 REST API for External Integration

#### Web API Server
- **HTTP endpoints** for all memory and streaming data functionality
- **CORS enabled** for cross-origin requests from websites
- **API key authentication** for secure access
- **JSON responses** for easy integration
- **Comprehensive documentation** with examples

### 🧠 Memory Management System

#### 1. Conversational Memory
- **Short-term chat history** for ongoing conversations
- Maintains context across interactions
- Configurable history length (default: 50 messages)
- Automatic message timestamping
- Context summarization

#### 2. Long-term Memory
- **Persistent storage** of important information
- Store facts, preferences, and entities
- Search functionality across all stored data
- JSON-based storage for easy inspection and backup
- Categorized fact storage

#### 3. Goals Management
- Create and track personal goals
- Progress monitoring (0-100%)
- Priority levels (high, medium, low)
- Milestone tracking
- Goal completion history
- Target date tracking

### 💰 Streaming Platform Data

#### Supported Platforms
- **YouTube** - Video streaming
- **Twitch** - Live streaming and gaming
- **Spotify** - Music streaming
- **TikTok** - Short-form video
- **Facebook Gaming** - Gaming streams
- **Instagram** - Reels and posts
- **Apple Music** - Music streaming

#### Features
- **Payout rates** per 1000 views/streams for each platform
- **Conversion rates** (views to subscribers, engagement rates)
- **Earnings calculator** based on view counts
- **Platform comparison** to identify best opportunities
- **Monetization requirements** for each platform
- **Earning factors** that affect payouts
- Support for custom platform data

## Installation

```bash
# Clone the repository
git clone https://github.com/MIHAchoppa/aI-lIVE-genie.git
cd aI-lIVE-genie

# Core system uses Python standard library only - no dependencies needed!

# For REST API server (optional)
pip install Flask Flask-CORS
```

## Quick Start

### Using the REST API (Recommended for Websites)

Start the API server:

```bash
# Set your API key (optional, defaults to dev key)
export AI_GENIE_API_KEY="your-secure-api-key"

# Start the server
python api_server.py
```

Access from your website using JavaScript:

```javascript
// Calculate earnings from your website
const response = await fetch('http://localhost:5000/api/streaming/earnings?platform=youtube&views=50000');
const data = await response.json();
console.log(`Estimated earnings: $${data.estimated_earnings.average}`);

// Store a conversation with authentication
await fetch('http://localhost:5000/api/conversation/interaction', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-API-Key': 'your-api-key-here'
  },
  body: JSON.stringify({
    user_input: "What platform pays the most?",
    assistant_response: "Apple Music pays the highest..."
  })
});
```

See [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for complete API reference.

### Using Python Directly

```python
from memory_manager import MemoryManager
from streaming_data import StreamingPlatformData

# Initialize the memory system
memory = MemoryManager()

# Process a conversation
memory.process_interaction(
    "How much can I earn on YouTube?",
    "On YouTube, you can earn $0.25-$4.00 per 1000 views, averaging $1.50"
)

# Store important facts
memory.long_term.store_fact(
    "User streams gaming content 3 times per week",
    category="streaming_schedule"
)

# Create a goal
memory.goals.add_goal(
    "Reach 10,000 subscribers",
    "Grow channel to 10k subs for better monetization",
    priority="high"
)

# Calculate earnings
streaming = StreamingPlatformData()
earnings = streaming.calculate_earnings("youtube", 50000)
print(f"Estimated earnings: ${earnings['estimated_earnings']['average']}")
```

### Run the Example Demo

```bash
python example_usage.py
```

This will demonstrate all features including:
- Conversational memory management
- Long-term memory storage and retrieval
- Goal creation and tracking
- Platform payout calculations
- Conversion rate analysis

## API Documentation

For complete API documentation including all endpoints, authentication, request/response formats, and usage examples, see:

**[API_DOCUMENTATION.md](API_DOCUMENTATION.md)** - Complete REST API reference

### Quick API Examples

#### From JavaScript (Browser/Node.js)
```javascript
// Get platform earnings (no auth required)
fetch('http://localhost:5000/api/streaming/earnings?platform=youtube&views=50000')
  .then(res => res.json())
  .then(data => console.log(data));

// Create a goal (auth required)
fetch('http://localhost:5000/api/goals', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-API-Key': 'your-api-key'
  },
  body: JSON.stringify({
    title: 'Reach 10k subscribers',
    description: 'First milestone',
    priority: 'high'
  })
}).then(res => res.json()).then(data => console.log(data));
```

#### From Python
```python
import requests

# Calculate earnings
response = requests.get(
    'http://localhost:5000/api/streaming/earnings',
    params={'platform': 'youtube', 'views': 50000}
)
print(response.json())

# Store a fact (with authentication)
response = requests.post(
    'http://localhost:5000/api/memory/fact',
    headers={'X-API-Key': 'your-api-key'},
    json={'fact': 'User streams gaming content', 'category': 'profile'}
)
print(response.json())
```

#### From cURL
```bash
# Calculate earnings
curl "http://localhost:5000/api/streaming/earnings?platform=youtube&views=50000"

# Create goal with auth
curl -X POST "http://localhost:5000/api/goals" \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{"title":"Reach 10k subs","description":"Milestone","priority":"high"}'
```

### Python Library Documentation

### Memory Manager

#### ConversationalMemory

```python
memory = ConversationalMemory(max_history=50)

# Add messages
memory.add_message("user", "Hello!")
memory.add_message("assistant", "Hi there!")

# Get conversation history
history = memory.get_history(last_n=10)

# Get context summary
summary = memory.get_context_summary()

# Clear history
memory.clear()
```

#### LongTermMemory

```python
long_term = LongTermMemory(storage_path="long_term_memory.json")

# Store data
long_term.store_fact("Important information", category="general")
long_term.store_preference("theme", "dark")
long_term.store_entity("my_channel", {"platform": "YouTube", "subs": 1000})

# Retrieve data
facts = long_term.retrieve_facts(category="general")
theme = long_term.retrieve_preference("theme")
channel = long_term.retrieve_entity("my_channel")

# Search memory
results = long_term.search_memory("channel")
```

#### GoalsManager

```python
goals = GoalsManager(storage_path="goals.json")

# Create a goal
goal = goals.add_goal(
    title="Reach 1000 subs",
    description="First milestone",
    priority="high",
    target_date="2025-12-31"
)

# Update progress
goals.update_goal_progress(goal_id=1, progress=45)

# Add milestones
goals.add_milestone(goal_id=1, milestone="Reach 500 subs")

# Complete a goal
goals.complete_goal(goal_id=1)

# Get goals
active_goals = goals.get_active_goals()
specific_goal = goals.get_goal_by_id(1)
```

### Streaming Platform Data

#### StreamingPlatformData

```python
streaming = StreamingPlatformData()

# Get platform information
youtube_data = streaming.get_platform_data("youtube")
all_platforms = streaming.get_all_platforms()

# Calculate earnings
earnings = streaming.calculate_earnings("youtube", 50000)
# Returns: {
#     "platform": "youtube",
#     "views": 50000,
#     "estimated_earnings": {
#         "min": 12.50,
#         "max": 200.00,
#         "average": 75.00,
#         "currency": "USD"
#     }
# }

# Compare platforms
comparison = streaming.compare_platforms(100000)
# Returns list of platforms ranked by earnings

# Get conversion rates
conversion = streaming.get_conversion_rates("view_to_subscriber")

# Calculate expected subscribers
subs = streaming.calculate_subscribers_from_views("youtube", 10000, "average")

# Get requirements
requirements = streaming.get_monetization_requirements("youtube")

# Get earning factors
factors = streaming.get_earning_factors("youtube")
```

## Platform Payout Summary

| Platform | Per 1000 Views/Streams | Notes |
|----------|----------------------|-------|
| YouTube | $0.25 - $4.00 (avg $1.50) | Varies by CPM, category, country |
| Twitch | $2.00 - $10.00 (avg $3.50) | Plus subs and bits |
| Spotify | $3.00 - $5.00 (avg $4.00) | Per 1000 streams |
| TikTok | $0.02 - $0.04 (avg $0.03) | Creator fund only |
| Facebook Gaming | $0.01 - $0.02 (avg $0.015) | Stars are main income |
| Instagram | $0.20 - $2.00 (avg $0.50) | Reels bonus, partnerships |
| Apple Music | $6.00 - $10.00 (avg $7.50) | Highest per-stream rate |

## Conversion Rates

### View to Subscriber
- **YouTube**: 2% average, 5% good, 10% excellent
- **Twitch**: 1.5% average, 4% good, 8% excellent

### Viewer to Paid Subscriber
- **YouTube Membership**: 0.1% average
- **Twitch Subscription**: 0.5% average
- **Patreon**: 0.2% average

### Engagement Rates
- **YouTube**: 4% average, 8% good, 15% excellent
- **Instagram**: 3% average, 6% good, 12% excellent
- **TikTok**: 6% average, 12% good, 20% excellent

## Data Storage

All data is stored in JSON format in the `./data/` directory:

- `long_term_memory.json` - Facts, preferences, and entities
- `goals.json` - Active and completed goals
- `streaming_data.json` - Custom platform data (if added)

These files can be backed up, shared, or edited manually if needed.

## Use Cases

### For Content Creators
- Track goals and progress toward milestones
- Calculate potential earnings across platforms
- Understand monetization requirements
- Make data-driven platform decisions
- Remember important conversations and decisions

### For AI Assistants
- Maintain conversation context
- Provide personalized recommendations
- Track user preferences and goals
- Access accurate streaming platform data
- Offer earnings projections

### For Agencies/Managers
- Manage multiple creator profiles
- Compare platform opportunities
- Track client goals and progress
- Maintain detailed client information

## Architecture

The system is designed with modularity and simplicity in mind:

- **No external dependencies** - Uses only Python standard library
- **JSON storage** - Human-readable, easy to backup and inspect
- **Modular design** - Each component can be used independently
- **Type hints** - Clear API with type annotations
- **Comprehensive documentation** - Inline docs and examples

## Contributing

Contributions are welcome! Areas for enhancement:
- Additional streaming platforms
- More conversion rate data
- Enhanced search capabilities
- Export/import functionality
- Analytics and reporting features

## License

This project is open source. See LICENSE file for details.

## Support

For questions, issues, or feature requests, please open an issue on GitHub.

---

**Made with ❤️ for content creators and live streamers**