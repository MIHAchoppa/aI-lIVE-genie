# API Reference

## Core Classes

### GroqModel

Platform-specific AI model powered by Groq.

```python
from ai_live_genie import GroqModel

model = GroqModel(
    platform="twitch",          # Required: Platform name
    model_name=None,            # Optional: Groq model (default: mixtral-8x7b-32768)
    api_key=None,               # Optional: API key (default: from env)
    temperature=0.7,            # Optional: Sampling temperature
    max_tokens=1024             # Optional: Max tokens to generate
)
```

#### Methods

##### `generate_response(user_message, conversation_history=None, **kwargs)`
Generate AI response.
- **user_message** (str): User's query
- **conversation_history** (list, optional): Previous messages
- **Returns**: Generated response text

##### `get_streaming_advice(query)`
Get platform-specific streaming advice.
- **query** (str): Streamer's question
- **Returns**: Advice text

##### `get_engagement_strategy(audience_size, goals)`
Get engagement strategy.
- **audience_size** (str): "small", "medium", or "large"
- **goals** (str): Streamer's goals
- **Returns**: Strategy recommendations

##### `get_monetization_advice(current_status)`
Get monetization advice.
- **current_status** (str): Current status description
- **Returns**: Monetization recommendations

---

### HostTrainingBot

AI-powered training bot for streamers.

```python
from ai_live_genie import HostTrainingBot

bot = HostTrainingBot(
    platform="youtube",         # Required: Platform name
    model=None                  # Optional: Custom GroqModel
)
```

#### Methods

##### `create_training_plan(experience_level, content_type, goals)`
Create personalized training plan.
- **experience_level** (str): "beginner", "intermediate", or "advanced"
- **content_type** (str): Type of content
- **goals** (list): List of goals
- **Returns**: Training plan dictionary

##### `get_streaming_tips(situation)`
Get real-time streaming tips.
- **situation** (str): Current situation
- **Returns**: Tips and advice

##### `analyze_performance(metrics)`
Analyze streaming performance.
- **metrics** (dict): Performance metrics
- **Returns**: Analysis dictionary

##### `suggest_content_ideas(trending_topics=None, target_audience=None)`
Generate content ideas.
- **trending_topics** (list, optional): Trending topics
- **target_audience** (str, optional): Target audience
- **Returns**: List of content ideas

##### `get_engagement_tactics(viewer_count, chat_activity)`
Get engagement tactics.
- **viewer_count** (int): Current viewers
- **chat_activity** (str): Chat activity level
- **Returns**: Engagement tactics

##### `prepare_stream_session(stream_title, duration_minutes, special_events=None)`
Prepare for stream session.
- **stream_title** (str): Stream title
- **duration_minutes** (int): Stream duration
- **special_events** (list, optional): Special events
- **Returns**: Preparation plan

##### `get_training_history()`
Get training history.
- **Returns**: List of training actions

---

### PlatformManager

Manage multiple platform integrations.

```python
from ai_live_genie import PlatformManager

manager = PlatformManager()
```

#### Methods

##### `get_model(platform)`
Get or create model for platform.
- **platform** (str): Platform name
- **Returns**: GroqModel instance
- **Raises**: ValueError if platform not supported

##### `get_all_platforms()`
Get list of supported platforms.
- **Returns**: List of platform names

##### `is_platform_supported(platform)`
Check if platform is supported.
- **platform** (str): Platform name
- **Returns**: Boolean

##### `get_platform_info(platform)`
Get platform information.
- **platform** (str): Platform name
- **Returns**: Platform info dictionary

##### `compare_platforms(platforms, criteria=None)`
Compare multiple platforms.
- **platforms** (list): List of platforms
- **criteria** (str, optional): Comparison criteria
- **Returns**: Comparison analysis

---

## Integration Classes

### StreamChatBot

AI-powered chat bot for live streams.

```python
from ai_live_genie.integrations import StreamChatBot

bot = StreamChatBot(
    platform="twitch",          # Required: Platform name
    model=None,                 # Optional: Custom GroqModel
    integration=None            # Optional: Platform integration
)
```

#### Methods

##### `async start()`
Start the chat bot.

##### `async stop()`
Stop the chat bot.

##### `add_message_handler(handler)`
Add custom message handler.
- **handler** (callable): Function to handle messages

##### `async process_message(message)`
Process chat message.
- **message** (dict): Chat message
- **Returns**: Response or None

##### `async monitor_chat(response_callback=None)`
Monitor chat continuously.
- **response_callback** (callable, optional): Response callback

##### `async get_stream_insights()`
Get AI-powered stream insights.
- **Returns**: Insights dictionary

##### `async suggest_chat_response(context)`
Suggest response to situation.
- **context** (str): Chat situation
- **Returns**: Suggested response

---

## Fine-Tuning Classes

### TrainingDataGenerator

Generate training data for fine-tuning.

```python
from ai_live_genie.fine_tuning import TrainingDataGenerator

generator = TrainingDataGenerator(platform="twitch")
```

#### Methods

##### `generate_training_examples(num_examples=100)`
Generate training examples.
- **num_examples** (int): Number of examples
- **Returns**: List of training examples

##### `export_jsonl(examples, filepath)`
Export to JSONL format.
- **examples** (list): Training examples
- **filepath** (str): Output file path

##### `create_fine_tuning_dataset(additional_examples=None)`
Create complete dataset.
- **additional_examples** (list, optional): Additional examples
- **Returns**: Complete dataset dictionary

##### `validate_training_data(data)` (static)
Validate training data format.
- **data** (list): Training data
- **Returns**: Boolean

---

### ModelFineTuner

Fine-tune models for platforms.

```python
from ai_live_genie.fine_tuning import ModelFineTuner

tuner = ModelFineTuner(
    platform="youtube",
    base_model="mixtral-8x7b-32768"
)
```

#### Methods

##### `prepare_training_data(training_examples)`
Prepare training data.
- **training_examples** (list): Raw examples
- **Returns**: Prepared data dictionary

##### `create_fine_tuning_job(training_file, validation_file=None)`
Create fine-tuning job config.
- **training_file** (str): Training file path
- **validation_file** (str, optional): Validation file path
- **Returns**: Job configuration

##### `estimate_training_time(num_examples)`
Estimate training time.
- **num_examples** (int): Number of examples
- **Returns**: Time estimates dictionary

##### `validate_model_output(model_response, expected_characteristics)`
Validate model output.
- **model_response** (str): Model's response
- **expected_characteristics** (list): Expected features
- **Returns**: Validation results

##### `generate_model_card()`
Generate model card.
- **Returns**: Model card as markdown

---

## Utility Functions

### helpers module

```python
from ai_live_genie.utils import (
    save_training_data,
    load_training_data,
    format_conversation_history,
    calculate_engagement_rate,
    parse_metrics_summary
)
```

#### Functions

##### `save_training_data(data, filepath)`
Save training data to YAML.

##### `load_training_data(filepath)`
Load training data from YAML.

##### `format_conversation_history(messages, max_messages=10)`
Format conversation history.

##### `calculate_engagement_rate(interactions, viewers)`
Calculate engagement rate.

##### `parse_metrics_summary(metrics)`
Parse metrics to summary string.

---

## Configuration

### Environment Variables

Required:
- `GROQ_API_KEY` - Your Groq API key

Optional:
- `DEFAULT_MODEL` - Default model name (default: mixtral-8x7b-32768)
- `TEMPERATURE` - Default temperature (default: 0.7)
- `MAX_TOKENS` - Default max tokens (default: 1024)

### Platform-Specific Config

Access via `ai_live_genie.config`:

```python
from ai_live_genie.config import (
    TRAINING_TEMPLATES,
    FINE_TUNING_CONFIG,
    PLATFORM_STRATEGIES
)
```

---

## Supported Platforms

- **twitch** - Twitch streaming
- **youtube** - YouTube Live
- **facebook** - Facebook Gaming
- **tiktok** - TikTok LIVE
- **kick** - Kick streaming
- **trovo** - Trovo streaming

---

## Error Handling

### Common Exceptions

- `ValueError` - Invalid platform or configuration
- `KeyError` - Missing required configuration
- `ConnectionError` - API connection issues

### Example Error Handling

```python
from ai_live_genie import GroqModel, PlatformManager

try:
    model = GroqModel(platform="invalid_platform")
except ValueError as e:
    print(f"Invalid platform: {e}")

try:
    manager = PlatformManager()
    model = manager.get_model("unsupported")
except ValueError as e:
    print(f"Platform not supported: {e}")
```

---

## Best Practices

### API Key Management
- Always use environment variables for API keys
- Never commit `.env` files to version control
- Use different keys for development and production

### Rate Limiting
- Be mindful of API rate limits
- Implement exponential backoff for retries
- Cache responses when appropriate

### Context Management
- Keep conversation history reasonable (5-10 messages)
- Clear history periodically for long sessions
- Provide relevant context in queries

### Platform-Specific Usage
- Use the correct platform name (lowercase)
- Leverage platform-specific features
- Understand each platform's culture and norms
