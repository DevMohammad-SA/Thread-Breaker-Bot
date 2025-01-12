# Telegram Message Splitter Bot

This is a simple Telegram bot that splits long messages into smaller parts (230 characters each) and numbers them for easy readability. It's perfect for splitting long threads or text into smaller, tweet-sized pieces.

## Features

- Splits messages longer than 230 characters into smaller chunks.
- Adds numbering to each chunk for better organization.
- Responds in Markdown formatting for clean and clear output.
- Easy-to-use `/start` command to get started.

## How It Works

1. Send a long message to the bot.
2. The bot will split it into smaller parts, each 230 characters or less.
3. Each part is sent back with a numbered label.

## Setup Instructions

### Prerequisites

- Python 3.10 or above
- A Telegram bot token (you can create one using [BotFather](https://core.telegram.org/bots#botfather))
- `python-telegram-bot` library version 20 or above
- `.env` file to store your bot token securely

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/DevMohammad-SA/Thread-Breaker-Bot.git
   cd Thread-Breaker-Bot
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your bot token:

   ```env
   BOT_TOKEN=your-telegram-bot-token
   ```

4. Run the bot:
   ```bash
   python bot.py
   ```

## Code Overview

### `break_message`

Splits a long message into chunks of 230 characters using Python's `textwrap` module.

### `/start` Command

Greets the user and explains the bot's purpose.

### Message Handler

Processes incoming text messages, splits them, and sends the parts back with numbering.

### Example Output

Input:

```
This is a very long message that needs to be split into smaller chunks because it exceeds the 230-character limit. The bot will take care of splitting it and numbering each part for you.
```

Output:

```
[1]
This is a very long message that needs to be split into smaller chunks because it exceeds the 230-character limit.
[2]
The bot will take care of splitting it and numbering each part for you.
```

## Contributing

Feel free to submit issues or pull requests. Contributions are always welcome!

## Contact

For any inquiries, reach out to me on [Telegram](https://t.me/DevMohammad_SA) or open an issue on this repository.
