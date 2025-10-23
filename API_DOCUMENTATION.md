# AI Live Genie - REST API Documentation

## Overview

The AI Live Genie REST API allows you to integrate memory management and streaming data features into your website or application. The API is built with Flask and supports CORS for cross-origin requests.

## Base URL

```
http://localhost:5000
```

When deployed, replace with your actual server URL.

## Authentication

Most endpoints require API key authentication. Include your API key in either:

**Header (Recommended):**
```
X-API-Key: your-api-key-here
```

**Query Parameter:**
```
?api_key=your-api-key-here
```

### Setting API Key

Set the `AI_GENIE_API_KEY` environment variable:

```bash
export AI_GENIE_API_KEY="your-secure-api-key"
```

Default key for development: `dev-key-change-in-production`

## API Endpoints

### Health Check

#### GET /health
Check API server health status.

**Authentication:** None required

**Response:**
```json
{
  "status": "healthy",
  "service": "AI Live Genie API"
}
```

---

## Conversational Memory Endpoints

### Add Message

#### POST /api/conversation/message
Add a single message to conversational memory.

**Authentication:** Required

**Request Body:**
```json
{
  "role": "user",
  "content": "Hello, how are you?",
  "metadata": {
    "source": "web"
  }
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Message added"
}
```

### Process Interaction

#### POST /api/conversation/interaction
Process a complete user-assistant interaction.

**Authentication:** Required

**Request Body:**
```json
{
  "user_input": "What platform pays the most?",
  "assistant_response": "Apple Music pays the highest per 1000 streams at $7.50 average."
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Interaction processed"
}
```

### Get Conversation History

#### GET /api/conversation/history
Retrieve conversation history.

**Authentication:** Required

**Query Parameters:**
- `last_n` (optional): Number of recent messages to retrieve

**Example:**
```
GET /api/conversation/history?last_n=10
```

**Response:**
```json
{
  "history": [
    {
      "role": "user",
      "content": "Hello",
      "timestamp": "2025-01-15T10:30:00",
      "metadata": {}
    },
    {
      "role": "assistant",
      "content": "Hi there!",
      "timestamp": "2025-01-15T10:30:01",
      "metadata": {}
    }
  ]
}
```

### Get Conversation Summary

#### GET /api/conversation/summary
Get a context summary of the conversation.

**Authentication:** Required

**Response:**
```json
{
  "summary": "Conversation with 5 messages:\n- [user]: Hello...\n- [assistant]: Hi there!..."
}
```

### Clear Conversation

#### POST /api/conversation/clear
Clear conversation history.

**Authentication:** Required

**Response:**
```json
{
  "status": "success",
  "message": "Conversation history cleared"
}
```

---

## Long-term Memory Endpoints

### Store Fact

#### POST /api/memory/fact
Store a fact in long-term memory.

**Authentication:** Required

**Request Body:**
```json
{
  "fact": "User streams gaming content",
  "category": "user_profile"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Fact stored"
}
```

### Retrieve Facts

#### GET /api/memory/fact
Retrieve facts from long-term memory.

**Authentication:** Required

**Query Parameters:**
- `category` (optional): Filter by category

**Example:**
```
GET /api/memory/fact?category=user_profile
```

**Response:**
```json
{
  "facts": [
    {
      "content": "User streams gaming content",
      "category": "user_profile",
      "timestamp": "2025-01-15T10:30:00"
    }
  ]
}
```

### Store Preference

#### POST /api/memory/preference
Store a user preference.

**Authentication:** Required

**Request Body:**
```json
{
  "key": "preferred_platform",
  "value": "YouTube"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Preference stored"
}
```

### Retrieve Preference

#### GET /api/memory/preference/{key}
Retrieve a specific preference.

**Authentication:** Required

**Example:**
```
GET /api/memory/preference/preferred_platform
```

**Response:**
```json
{
  "key": "preferred_platform",
  "value": "YouTube"
}
```

### Store Entity

#### POST /api/memory/entity
Store an entity in long-term memory.

**Authentication:** Required

**Request Body:**
```json
{
  "entity_name": "main_channel",
  "entity_data": {
    "platform": "YouTube",
    "subscribers": 5000,
    "avg_views": 2000
  }
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Entity stored"
}
```

### Retrieve Entity

#### GET /api/memory/entity/{entity_name}
Retrieve a specific entity.

**Authentication:** Required

**Example:**
```
GET /api/memory/entity/main_channel
```

**Response:**
```json
{
  "entity_name": "main_channel",
  "data": {
    "platform": "YouTube",
    "subscribers": 5000,
    "avg_views": 2000
  }
}
```

### Search Memory

#### GET /api/memory/search
Search through long-term memory.

**Authentication:** Required

**Query Parameters:**
- `query` (required): Search query

**Example:**
```
GET /api/memory/search?query=youtube
```

**Response:**
```json
{
  "results": [
    {
      "type": "fact",
      "data": {
        "content": "YouTube is great for beginners",
        "category": "general",
        "timestamp": "2025-01-15T10:30:00"
      }
    },
    {
      "type": "entity",
      "name": "main_channel",
      "data": {
        "data": {
          "platform": "YouTube",
          "subscribers": 5000
        },
        "timestamp": "2025-01-15T10:30:00"
      }
    }
  ]
}
```

---

## Goals Management Endpoints

### Add Goal

#### POST /api/goals
Create a new goal.

**Authentication:** Required

**Request Body:**
```json
{
  "title": "Reach 10,000 subscribers",
  "description": "First major milestone for monetization",
  "priority": "high",
  "target_date": "2025-12-31"
}
```

**Response:**
```json
{
  "status": "success",
  "goal": {
    "id": 1,
    "title": "Reach 10,000 subscribers",
    "description": "First major milestone for monetization",
    "priority": "high",
    "target_date": "2025-12-31",
    "status": "active",
    "progress": 0,
    "created_at": "2025-01-15T10:30:00",
    "milestones": []
  }
}
```

### Get All Goals

#### GET /api/goals
Retrieve all active goals.

**Authentication:** Required

**Response:**
```json
{
  "goals": [
    {
      "id": 1,
      "title": "Reach 10,000 subscribers",
      "description": "First major milestone",
      "priority": "high",
      "progress": 45,
      "status": "active"
    }
  ]
}
```

### Get Specific Goal

#### GET /api/goals/{goal_id}
Retrieve a specific goal by ID.

**Authentication:** Required

**Example:**
```
GET /api/goals/1
```

**Response:**
```json
{
  "goal": {
    "id": 1,
    "title": "Reach 10,000 subscribers",
    "progress": 45,
    "milestones": []
  }
}
```

### Update Goal Progress

#### PUT /api/goals/{goal_id}/progress
Update progress on a goal.

**Authentication:** Required

**Request Body:**
```json
{
  "progress": 75
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Progress updated"
}
```

### Complete Goal

#### POST /api/goals/{goal_id}/complete
Mark a goal as completed.

**Authentication:** Required

**Response:**
```json
{
  "status": "success",
  "message": "Goal completed"
}
```

### Add Milestone

#### POST /api/goals/{goal_id}/milestone
Add a milestone to a goal.

**Authentication:** Required

**Request Body:**
```json
{
  "milestone": "Reached 5,000 subscribers"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Milestone added"
}
```

---

## Streaming Platform Data Endpoints

### Get All Platforms

#### GET /api/streaming/platforms
Get list of all available platforms.

**Authentication:** None required

**Response:**
```json
{
  "platforms": [
    "apple_music",
    "facebook_gaming",
    "instagram",
    "spotify",
    "tiktok",
    "twitch",
    "youtube"
  ]
}
```

### Get Platform Data

#### GET /api/streaming/platform/{platform}
Get detailed data for a specific platform.

**Authentication:** None required

**Example:**
```
GET /api/streaming/platform/youtube
```

**Response:**
```json
{
  "platform": "youtube",
  "data": {
    "name": "YouTube",
    "payout_per_1000_views": {
      "min": 0.25,
      "max": 4.0,
      "average": 1.5,
      "currency": "USD"
    },
    "factors": [
      "CPM varies by country",
      "Content category affects rates"
    ],
    "monetization_requirements": {
      "subscribers": 1000,
      "watch_hours_12_months": 4000
    }
  }
}
```

### Calculate Earnings

#### GET /api/streaming/earnings
Calculate estimated earnings for a platform.

**Authentication:** None required

**Query Parameters:**
- `platform` (required): Platform name
- `views` (required): Number of views/streams

**Example:**
```
GET /api/streaming/earnings?platform=youtube&views=50000
```

**Response:**
```json
{
  "platform": "youtube",
  "views": 50000,
  "estimated_earnings": {
    "min": 12.5,
    "max": 200.0,
    "average": 75.0,
    "currency": "USD"
  }
}
```

### Compare Platforms

#### GET /api/streaming/compare
Compare earnings across all platforms.

**Authentication:** None required

**Query Parameters:**
- `views` (required): Number of views to compare

**Example:**
```
GET /api/streaming/compare?views=100000
```

**Response:**
```json
{
  "comparison": [
    {
      "platform": "apple_music",
      "views": 100000,
      "estimated_earnings": {
        "min": 600.0,
        "max": 1000.0,
        "average": 750.0,
        "currency": "USD"
      }
    },
    {
      "platform": "spotify",
      "views": 100000,
      "estimated_earnings": {
        "min": 300.0,
        "max": 500.0,
        "average": 400.0,
        "currency": "USD"
      }
    }
  ]
}
```

### Calculate Subscribers

#### GET /api/streaming/subscribers
Calculate expected subscribers from views.

**Authentication:** None required

**Query Parameters:**
- `platform` (required): Platform name
- `views` (required): Number of views
- `quality` (optional): Conversion quality (average, good, excellent)

**Example:**
```
GET /api/streaming/subscribers?platform=youtube&views=10000&quality=average
```

**Response:**
```json
{
  "platform": "youtube",
  "views": 10000,
  "quality": "average",
  "expected_subscribers": 200
}
```

### Get Conversion Rates

#### GET /api/streaming/conversion-rates
Get conversion rate data.

**Authentication:** None required

**Query Parameters:**
- `type` (required): Conversion type (view_to_subscriber, viewer_to_paid_subscriber, engagement_rate)

**Example:**
```
GET /api/streaming/conversion-rates?type=view_to_subscriber
```

**Response:**
```json
{
  "type": "view_to_subscriber",
  "rates": {
    "youtube": {
      "average": 0.02,
      "good": 0.05,
      "excellent": 0.1
    },
    "twitch": {
      "average": 0.015,
      "good": 0.04,
      "excellent": 0.08
    }
  }
}
```

### Get Monetization Requirements

#### GET /api/streaming/requirements/{platform}
Get monetization requirements for a platform.

**Authentication:** None required

**Example:**
```
GET /api/streaming/requirements/youtube
```

**Response:**
```json
{
  "platform": "youtube",
  "requirements": {
    "subscribers": 1000,
    "watch_hours_12_months": 4000
  }
}
```

### Get Earning Factors

#### GET /api/streaming/factors/{platform}
Get factors that affect earnings on a platform.

**Authentication:** None required

**Example:**
```
GET /api/streaming/factors/youtube
```

**Response:**
```json
{
  "platform": "youtube",
  "factors": [
    "CPM (Cost Per Mille) varies by country",
    "Content category affects rates",
    "Ad engagement impacts earnings",
    "YouTube Premium views pay more"
  ]
}
```

---

## Context Endpoint

### Get Full Context

#### GET /api/context
Get complete context from all memory types.

**Authentication:** Required

**Response:**
```json
{
  "conversation_history": [
    {"role": "user", "content": "Hello"}
  ],
  "recent_facts": [
    {"content": "User streams gaming", "category": "profile"}
  ],
  "active_goals": [
    {"id": 1, "title": "Reach 10k subs", "progress": 45}
  ],
  "preferences": {
    "preferred_platform": {
      "value": "YouTube",
      "timestamp": "2025-01-15T10:30:00"
    }
  }
}
```

---

## Error Responses

### 400 Bad Request
```json
{
  "error": "Missing required parameter"
}
```

### 401 Unauthorized
```json
{
  "error": "Invalid or missing API key"
}
```

### 404 Not Found
```json
{
  "error": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error"
}
```

---

## Usage Examples

### JavaScript (Fetch API)

```javascript
// Set your API key
const API_KEY = 'your-api-key-here';
const BASE_URL = 'http://localhost:5000';

// Calculate earnings
async function calculateEarnings(platform, views) {
  const response = await fetch(
    `${BASE_URL}/api/streaming/earnings?platform=${platform}&views=${views}`
  );
  const data = await response.json();
  return data;
}

// Store a conversation
async function storeInteraction(userInput, assistantResponse) {
  const response = await fetch(`${BASE_URL}/api/conversation/interaction`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-API-Key': API_KEY
    },
    body: JSON.stringify({
      user_input: userInput,
      assistant_response: assistantResponse
    })
  });
  return response.json();
}

// Create a goal
async function createGoal(title, description, priority) {
  const response = await fetch(`${BASE_URL}/api/goals`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-API-Key': API_KEY
    },
    body: JSON.stringify({
      title: title,
      description: description,
      priority: priority
    })
  });
  return response.json();
}

// Example usage
calculateEarnings('youtube', 50000).then(data => {
  console.log(`Estimated earnings: $${data.estimated_earnings.average}`);
});
```

### Python (Requests)

```python
import requests

API_KEY = 'your-api-key-here'
BASE_URL = 'http://localhost:5000'

# Calculate earnings
def calculate_earnings(platform, views):
    response = requests.get(
        f'{BASE_URL}/api/streaming/earnings',
        params={'platform': platform, 'views': views}
    )
    return response.json()

# Store interaction
def store_interaction(user_input, assistant_response):
    response = requests.post(
        f'{BASE_URL}/api/conversation/interaction',
        headers={'X-API-Key': API_KEY},
        json={
            'user_input': user_input,
            'assistant_response': assistant_response
        }
    )
    return response.json()

# Create goal
def create_goal(title, description, priority='medium'):
    response = requests.post(
        f'{BASE_URL}/api/goals',
        headers={'X-API-Key': API_KEY},
        json={
            'title': title,
            'description': description,
            'priority': priority
        }
    )
    return response.json()

# Example usage
earnings = calculate_earnings('youtube', 50000)
print(f"Estimated earnings: ${earnings['estimated_earnings']['average']}")
```

### cURL

```bash
# Calculate earnings (no auth required)
curl "http://localhost:5000/api/streaming/earnings?platform=youtube&views=50000"

# Store interaction (auth required)
curl -X POST "http://localhost:5000/api/conversation/interaction" \
  -H "X-API-Key: your-api-key-here" \
  -H "Content-Type: application/json" \
  -d '{
    "user_input": "What platform pays the most?",
    "assistant_response": "Apple Music pays the highest at $7.50 per 1000 streams."
  }'

# Create goal (auth required)
curl -X POST "http://localhost:5000/api/goals" \
  -H "X-API-Key: your-api-key-here" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Reach 10k subscribers",
    "description": "First major milestone",
    "priority": "high"
  }'
```

---

## Running the API Server

### Start the Server

```bash
# Set API key (recommended)
export AI_GENIE_API_KEY="your-secure-api-key"

# Run the server
python api_server.py
```

### Configuration via Environment Variables

```bash
export AI_GENIE_API_KEY="your-secure-api-key"
export API_HOST="0.0.0.0"
export API_PORT="5000"
export API_DEBUG="False"
```

### Production Deployment

For production, use a WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 api_server:app
```

---

## Security Considerations

1. **Change the default API key** in production
2. **Use HTTPS** for all API communications
3. **Implement rate limiting** to prevent abuse
4. **Set up proper firewall rules** to restrict access
5. **Rotate API keys** regularly
6. **Monitor API usage** for suspicious activity

---

## CORS Configuration

The API supports Cross-Origin Resource Sharing (CORS) by default, allowing requests from any origin. For production, configure specific allowed origins:

```python
from flask_cors import CORS

CORS(app, resources={
    r"/api/*": {
        "origins": ["https://yourdomain.com"]
    }
})
```

---

## Support

For questions or issues with the API:
- Check this documentation
- Review the example code
- Open an issue on GitHub

---

**Made with ❤️ for content creators and developers**
