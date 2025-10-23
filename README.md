# 🎮 AI Live Genie

> A master set of AI fine-tuned Groq models for every live streaming platform with strategy and host training bot capabilities.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

AI Live Genie provides platform-specific AI assistants powered by Groq's lightning-fast LLMs, fine-tuned for live streaming platforms including Twitch, YouTube, Facebook Gaming, TikTok, Kick, and Trovo. Get expert advice, training, and strategies tailored to each platform's unique culture and features.

## ✨ Features

- 🎯 **Platform-Specific Models**: Fine-tuned AI models for each major streaming platform
- 🤖 **Host Training Bot**: AI-powered training and coaching for streamers
- 📊 **Performance Analysis**: Analyze streaming metrics and get actionable insights
- 💡 **Content Strategy**: Generate content ideas and streaming strategies
- 🎪 **Engagement Tactics**: Real-time tips for increasing viewer engagement
- 🚀 **Multi-Platform Support**: Manage multiple platforms from one interface

## 🎯 Supported Platforms

- **Twitch** - Gaming and creative content streaming
- **YouTube** - Live streaming with SEO optimization
- **Facebook Gaming** - Social media integrated streaming
- **TikTok** - Short-form live streaming with LIVE gifts
- **Kick** - Creator-first platform with 95/5 revenue split
- **Trovo** - Interactive streaming with unique features

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Groq API key ([Get one here](https://console.groq.com))

### Install from source

```bash
git clone https://github.com/MIHAchoppa/aI-lIVE-genie.git
cd aI-lIVE-genie
pip install -e .
```

### Setup environment

```bash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

## 🚀 Quick Start

### Basic Usage

```python
from ai_live_genie import GroqModel

# Initialize a Twitch-focused model
model = GroqModel(platform="twitch")

# Get streaming advice
advice = model.get_streaming_advice(
    "How can I grow my audience as a new streamer?"
)
print(advice)

# Get monetization tips
tips = model.get_monetization_advice(
    current_status="No affiliate yet, streaming for 2 months"
)
print(tips)
```

### Using the Host Training Bot

```python
from ai_live_genie import HostTrainingBot

# Initialize training bot
bot = HostTrainingBot(platform="twitch")

# Create a personalized training plan
plan = bot.create_training_plan(
    experience_level="beginner",
    content_type="gaming",
    goals=[
        "Reach Twitch Affiliate",
        "Build a community of 100 regulars",
        "Stream consistently 3x per week"
    ]
)
print(plan["plan"])

# Analyze your performance
metrics = {
    "average_viewers": 12,
    "peak_viewers": 25,
    "chat_messages": 150,
    "new_followers": 3,
    "stream_duration_minutes": 180
}

analysis = bot.analyze_performance(metrics)
print(analysis["analysis"])
```

### Multi-Platform Management

```python
from ai_live_genie import PlatformManager

# Initialize platform manager
manager = PlatformManager()

# Get models for different platforms
twitch_model = manager.get_model("twitch")
youtube_model = manager.get_model("youtube")

# Compare platforms
comparison = manager.compare_platforms(
    platforms=["twitch", "youtube", "kick"],
    criteria="revenue potential for new streamers"
)
print(comparison)
```

## 📚 Documentation

### Core Components

#### GroqModel

The base model class for platform-specific AI interactions.

**Key Methods:**
- `generate_response(message)` - Generate AI responses
- `get_streaming_advice(query)` - Get platform-specific advice
- `get_engagement_strategy(audience_size, goals)` - Get engagement strategies
- `get_monetization_advice(status)` - Get monetization tips

#### HostTrainingBot

AI-powered training bot for live stream hosts.

**Key Methods:**
- `create_training_plan(level, content_type, goals)` - Create personalized training
- `get_streaming_tips(situation)` - Get real-time streaming tips
- `analyze_performance(metrics)` - Analyze streaming performance
- `suggest_content_ideas(topics, audience)` - Generate content ideas
- `prepare_stream_session(title, duration, events)` - Prepare for streams

#### PlatformManager

Manage multiple platform integrations.

**Key Methods:**
- `get_model(platform)` - Get or create platform model
- `get_all_platforms()` - List supported platforms
- `get_platform_info(platform)` - Get platform information
- `compare_platforms(platforms, criteria)` - Compare platforms

## 🎓 Examples

Check out the `examples/` directory for complete examples:

- `basic_usage.py` - Basic model usage
- `training_bot_example.py` - Host training bot features
- `platform_manager_example.py` - Multi-platform management

## 🔧 Configuration

### Environment Variables

Create a `.env` file with:

```env
GROQ_API_KEY=your_groq_api_key_here
DEFAULT_MODEL=mixtral-8x7b-32768
TEMPERATURE=0.7
MAX_TOKENS=1024
```

### Model Configuration

Customize model behavior in your code:

```python
model = GroqModel(
    platform="twitch",
    model_name="mixtral-8x7b-32768",
    temperature=0.7,
    max_tokens=1024
)
```

## 🎯 Use Cases

### For New Streamers
- Get platform-specific setup guidance
- Learn best practices for your chosen platform
- Create a growth strategy from scratch
- Understand monetization paths

### For Growing Streamers
- Optimize content strategy
- Improve engagement tactics
- Analyze performance metrics
- Plan special events and milestones

### For Multi-Platform Streamers
- Compare platform opportunities
- Manage multiple platform strategies
- Optimize cross-platform promotion
- Understand platform-specific audiences

### For Content Creators
- Generate content ideas
- Plan streaming schedules
- Build community engagement strategies
- Develop brand identity

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Groq](https://groq.com) for lightning-fast AI inference
- Inspired by the streaming community across all platforms

## 📞 Support

For questions and support, please open an issue on GitHub.

---

**Made with ❤️ for the streaming community**