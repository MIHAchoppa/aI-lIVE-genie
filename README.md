# aI-lIVE-genie

An AI bot with Poe API integration that allows users to interact with Poe's AI models.

## Features

- Easy integration with Poe API
- Support for custom API keys
- Simple chat interface
- Support for conversation history
- Environment variable configuration

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MIHAchoppa/aI-lIVE-genie.git
cd aI-lIVE-genie
```

2. Install dependencies:
```bash
npm install
```

3. Set up your API key:
   - Copy `.env.example` to `.env`
   - Get your Poe API key from [https://poe.com/api_key](https://poe.com/api_key)
   - Add your API key to `.env`:
   ```
   POE_API_KEY=your_poe_api_key_here
   ```

## Usage

### Option 1: Run the example

```bash
npm start
```

### Option 2: Use as a module

```javascript
const PoeBot = require('./index');

// Using environment variable (from .env file)
const bot = new PoeBot();

// Or pass API key directly
const botWithKey = new PoeBot("YOUR_POE_API_KEY");

// Send a simple message
const response = await bot.chat("Hello world");
console.log(response);

// Send a message with conversation history
const messages = [
    { role: "user", content: "Hello" },
    { role: "assistant", content: "Hi! How can I help you?" },
    { role: "user", content: "Tell me a joke" }
];
const response2 = await bot.chatWithHistory(messages);
console.log(response2);
```

### Option 3: Custom model

```javascript
const bot = new PoeBot();

// Use a different Poe model
const response = await bot.chat("Hello", "Cease-And-Desist-pro");
console.log(response);
```

## API Reference

### `PoeBot` Class

#### Constructor
```javascript
new PoeBot(apiKey)
```
- `apiKey` (optional): Your Poe API key. If not provided, will use `POE_API_KEY` from environment variables.

#### Methods

##### `chat(message, model)`
Send a single message to the Poe API.

- `message` (string): The message to send
- `model` (string, optional): The model to use. Default: "Cease-And-Desist-pro"
- Returns: Promise<string> - The bot's response

##### `chatWithHistory(messages, model)`
Send a conversation with multiple messages to the Poe API.

- `messages` (Array): Array of message objects with `role` and `content` properties
- `model` (string, optional): The model to use. Default: "Cease-And-Desist-pro"
- Returns: Promise<string> - The bot's response

## Configuration

The bot can be configured using:

1. **Environment variables**: Create a `.env` file with your `POE_API_KEY`
2. **Direct API key**: Pass the API key directly to the constructor
3. **User login**: If integrated with a web application, you can retrieve the API key after user authentication

## License

ISC
