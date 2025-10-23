const { OpenAI } = require("openai");
require('dotenv').config();

/**
 * Poe API Bot
 * 
 * This bot allows users to interact with Poe's AI models via the API.
 * Users can provide their own API key via environment variable or pass it directly.
 */
class PoeBot {
    constructor(apiKey = null) {
        // Use provided API key or get from environment variable
        this.apiKey = apiKey || process.env.POE_API_KEY;
        
        if (!this.apiKey) {
            throw new Error('POE_API_KEY is required. Set it in .env file or pass it to the constructor.');
        }

        this.client = new OpenAI({
            apiKey: this.apiKey,
            baseURL: "https://api.poe.com/v1",
        });
    }

    /**
     * Send a message to the Poe API and get a response
     * @param {string} message - The message to send
     * @param {string} model - The model to use (default: "Cease-And-Desist-pro")
     * @returns {Promise<string>} - The bot's response
     */
    async chat(message, model = "Cease-And-Desist-pro") {
        try {
            const chat = await this.client.chat.completions.create({
                model: model,
                messages: [{ role: "user", content: message }],
            });

            return chat.choices[0].message.content;
        } catch (error) {
            console.error('Error communicating with Poe API:', error.message);
            throw error;
        }
    }

    /**
     * Send a conversation with multiple messages to the Poe API
     * @param {Array<{role: string, content: string}>} messages - Array of messages
     * @param {string} model - The model to use (default: "Cease-And-Desist-pro")
     * @returns {Promise<string>} - The bot's response
     */
    async chatWithHistory(messages, model = "Cease-And-Desist-pro") {
        try {
            const chat = await this.client.chat.completions.create({
                model: model,
                messages: messages,
            });

            return chat.choices[0].message.content;
        } catch (error) {
            console.error('Error communicating with Poe API:', error.message);
            throw error;
        }
    }
}

// Example usage when run directly
async function main() {
    try {
        // Option 1: Use API key from environment variable
        const bot = new PoeBot();
        
        // Option 2: Pass API key directly (uncomment to use)
        // const bot = new PoeBot("YOUR_POE_API_KEY");

        console.log('Sending message to Poe API...');
        const response = await bot.chat("Hello world");
        console.log('Response:', response);
    } catch (error) {
        console.error('Error:', error.message);
        process.exit(1);
    }
}

// Run example if this file is executed directly
if (require.main === module) {
    main();
}

module.exports = PoeBot;
