const PoeBot = require('./index');

/**
 * Example demonstrating different ways to use the Poe API Bot
 */

async function examples() {
    try {
        console.log('=== Poe API Bot Examples ===\n');

        // Example 1: Simple chat with environment variable API key
        console.log('Example 1: Simple chat');
        console.log('Make sure you have POE_API_KEY set in your .env file');
        console.log('Uncomment the code below to test:\n');
        console.log('const bot = new PoeBot();');
        console.log('const response = await bot.chat("Hello world");');
        console.log('console.log(response);\n');

        // Example 2: Chat with API key passed directly
        console.log('Example 2: Chat with API key passed directly');
        console.log('const bot = new PoeBot("YOUR_POE_API_KEY");');
        console.log('const response = await bot.chat("Tell me a joke");');
        console.log('console.log(response);\n');

        // Example 3: Chat with conversation history
        console.log('Example 3: Chat with conversation history');
        console.log('const bot = new PoeBot();');
        console.log('const messages = [');
        console.log('    { role: "user", content: "Hello" },');
        console.log('    { role: "assistant", content: "Hi! How can I help you?" },');
        console.log('    { role: "user", content: "Tell me about AI" }');
        console.log('];');
        console.log('const response = await bot.chatWithHistory(messages);');
        console.log('console.log(response);\n');

        // Example 4: Using a different model
        console.log('Example 4: Using a different model');
        console.log('const bot = new PoeBot();');
        console.log('const response = await bot.chat("Explain quantum physics", "Cease-And-Desist-pro");');
        console.log('console.log(response);\n');

        console.log('=== To run these examples ===');
        console.log('1. Copy .env.example to .env');
        console.log('2. Add your Poe API key to .env');
        console.log('3. Uncomment the example code you want to test');
        console.log('4. Run: node example.js');

    } catch (error) {
        console.error('Error:', error.message);
    }
}

examples();
