# Getting Started with AI Live Genie

Welcome to AI Live Genie! This guide will help you get started with using AI-powered assistance for your live streaming journey.

## Prerequisites

- Python 3.8 or higher
- A Groq API key ([Get one for free](https://console.groq.com))
- Basic understanding of your streaming platform

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/MIHAchoppa/aI-lIVE-genie.git
cd aI-lIVE-genie
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install as a package:

```bash
pip install -e .
```

### 3. Configure Environment

Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env` and add your Groq API key:

```env
GROQ_API_KEY=your_actual_api_key_here
```

## Quick Start Examples

### Example 1: Get Streaming Advice

```python
from ai_live_genie import GroqModel

# Create a model for your platform
model = GroqModel(platform="twitch")

# Ask for advice
advice = model.get_streaming_advice(
    "I'm new to streaming. What equipment do I need to get started?"
)
print(advice)
```

### Example 2: Create a Training Plan

```python
from ai_live_genie import HostTrainingBot

# Initialize training bot
bot = HostTrainingBot(platform="youtube")

# Create personalized training plan
plan = bot.create_training_plan(
    experience_level="beginner",
    content_type="gaming",
    goals=[
        "Reach 1000 subscribers",
        "Get monetized",
        "Stream 3 times per week"
    ]
)

print(plan["plan"])
```

### Example 3: Analyze Your Performance

```python
from ai_live_genie import HostTrainingBot

bot = HostTrainingBot(platform="twitch")

# Your stream metrics
metrics = {
    "average_viewers": 25,
    "peak_viewers": 45,
    "chat_messages": 300,
    "new_followers": 8,
    "stream_duration_minutes": 180
}

# Get AI analysis
analysis = bot.analyze_performance(metrics)
print(analysis["analysis"])
```

### Example 4: Using the CLI

The CLI tool provides quick access without writing code:

```bash
# Get advice
python cli.py advice twitch "How do I deal with stream snipers?"

# Create training plan
python cli.py training youtube --level beginner --content gaming

# Compare platforms
python cli.py compare --platforms "twitch,youtube,kick"

# Generate content ideas
python cli.py ideas tiktok --trending "cozy gaming,speedruns"
```

## Platform-Specific Quick Starts

### For Twitch Streamers

```python
from ai_live_genie import GroqModel

twitch = GroqModel(platform="twitch")

# Get help with common Twitch topics
print(twitch.get_streaming_advice("How do I get Twitch Affiliate?"))
print(twitch.get_monetization_advice("Just started, no subs yet"))
print(twitch.get_engagement_strategy("small", "Build regular viewers"))
```

### For YouTube Streamers

```python
from ai_live_genie import GroqModel

youtube = GroqModel(platform="youtube")

# YouTube-specific advice
print(youtube.get_streaming_advice("How do I optimize my stream for search?"))
print(youtube.get_streaming_advice("Should I focus on shorts or live streams?"))
```

### For TikTok LIVE Streamers

```python
from ai_live_genie import GroqModel

tiktok = GroqModel(platform="tiktok")

# TikTok-specific advice
print(tiktok.get_streaming_advice("How do I encourage viewers to send gifts?"))
print(tiktok.get_streaming_advice("What's the best time to go LIVE?"))
```

## Common Workflows

### Weekly Streamer Workflow

```python
from ai_live_genie import HostTrainingBot

bot = HostTrainingBot(platform="twitch")

# 1. Start of week - Get content ideas
ideas = bot.suggest_content_ideas(
    trending_topics=["Current trends"],
    target_audience="Your audience description"
)

# 2. Before each stream - Prepare
prep = bot.prepare_stream_session(
    stream_title="Your stream title",
    duration_minutes=180,
    special_events=["Giveaway", "Q&A"]
)

# 3. During stream - Get tips
tips = bot.get_streaming_tips(
    "Chat is quiet, how can I engage viewers?"
)

# 4. After stream - Analyze
metrics = {
    # Your actual metrics
}
analysis = bot.analyze_performance(metrics)

# 5. End of week - Review training progress
history = bot.get_training_history()
```

### Multi-Platform Streamer

```python
from ai_live_genie import PlatformManager

manager = PlatformManager()

# Get advice for each platform
platforms = ["twitch", "youtube", "tiktok"]

for platform in platforms:
    model = manager.get_model(platform)
    advice = model.get_streaming_advice(
        "Best practices for simulcasting?"
    )
    print(f"\n{platform.upper()}:\n{advice}")

# Compare monetization
comparison = manager.compare_platforms(
    platforms=platforms,
    criteria="monetization options for small streamers"
)
print(comparison)
```

## Tips for Best Results

### 1. Be Specific in Your Questions

❌ Bad: "Help me grow"
✅ Good: "I'm a beginner Twitch streamer with 10 average viewers streaming gaming content 3x per week. What are 3 specific things I can do this month to reach 25 average viewers?"

### 2. Provide Context

Include relevant information:
- Your current metrics
- Your goals
- Your constraints (time, budget, etc.)
- Your content type
- Your target audience

### 3. Use the Right Platform

Always specify your platform or use platform-specific models:

```python
# Specify platform
model = GroqModel(platform="youtube")

# Not platform-specific (will be less accurate)
model = GroqModel(platform="generic")  # Don't do this
```

### 4. Iterate and Refine

Have conversations with the AI:

```python
model = GroqModel(platform="twitch")

# First question
response1 = model.generate_response("How do I improve chat engagement?")

# Follow-up in same conversation
conversation = [
    {"role": "user", "content": "How do I improve chat engagement?"},
    {"role": "assistant", "content": response1}
]

response2 = model.generate_response(
    "Can you give me specific examples for a gaming stream?",
    conversation_history=conversation
)
```

## Troubleshooting

### "No module named 'groq'"

Install the Groq package:
```bash
pip install groq
```

### "GROQ_API_KEY must be provided"

Make sure you have:
1. Created a `.env` file
2. Added your API key: `GROQ_API_KEY=your_key_here`
3. The `.env` file is in the project root

### "Platform not supported"

Check the list of supported platforms:
```python
from ai_live_genie import PlatformManager

manager = PlatformManager()
print(manager.get_all_platforms())
```

### Slow responses

- Groq is generally very fast
- Check your internet connection
- Reduce `max_tokens` if generating very long responses

## Next Steps

1. **Explore Examples**: Check the `examples/` directory for more code samples
2. **Read Documentation**: 
   - [API Reference](docs/API_REFERENCE.md)
   - [Platform Guide](docs/PLATFORM_GUIDE.md)
   - [Training Bot Guide](docs/TRAINING_BOT_GUIDE.md)
3. **Try the CLI**: Run `python cli.py --help` to see all options
4. **Join the Community**: Share your experience and get help

## Advanced Features

### Creating Custom Training Data

```python
from ai_live_genie.fine_tuning import TrainingDataGenerator

generator = TrainingDataGenerator(platform="twitch")
examples = generator.generate_training_examples(num_examples=100)
generator.export_jsonl(examples, "training_data.jsonl")
```

### Using Chat Bot Integration

```python
import asyncio
from ai_live_genie.integrations import StreamChatBot

async def run_bot():
    bot = StreamChatBot(platform="twitch")
    await bot.start()
    
    insights = await bot.get_stream_insights()
    print(insights)
    
    await bot.stop()

asyncio.run(run_bot())
```

## Support

- **Issues**: [GitHub Issues](https://github.com/MIHAchoppa/aI-lIVE-genie/issues)
- **Documentation**: Check the `docs/` directory
- **Examples**: Check the `examples/` directory

## License

MIT License - See [LICENSE](LICENSE) file for details.

---

Happy Streaming! 🎮🎪✨
