# Dextools Telegram Message Listener

The __dextools_tg_message_listener.py__ module is one of crucial components of Telegram bot application, designed to process messages containing Dextools URLs. It extracts relevant cryptocurrency token addresses from these URLs and utilizes the telegram_alerts.py module to send formatted alerts to a specified Telegram chat or channel.

## Features

- __URL Processing:__ Efficiently extracts token addresses from Dextools pair explorer URLs shared in messages.
- __Integration with Telegram Alerts:__ Sends alerts with token address details using the telegram_alerts.py module.
- __Flexible Configuration:__ Works dynamically with various Dextools pair explorer links.

## Getting Started

__Prerequisites__

- Python 3.6 or newer.
- Access to the Telegram API through a registered Telegram bot.
- The Telethon library for interacting with the Telegram API.
- The __telegram_alerts.py__ module properly set up in the same project.

## Installation

__1. Ensure Python and Pip are Installed:__

Ensure that Python 3.6+ is installed on your system and that you can run python and pip commands in your terminal.

__2. Install Required Python Packages:__

If not already installed, install Telethon and any other required packages:

```bash
pip install telethon
```

__3. Configure Your Bot Credentials:__

Make sure your __credentials_telegram.json__ is correctly set up with your __api_id__, __api_hash__, and __bot_token__ for Telethon authentication.

## Usage

The __dextools_tg_message_listener.py__ module is intended to be used as part of the larger Telegram bot application. It is triggered when messages containing Dextools URLs are detected:

__Integration with Main Listener Script:__

__1. Ensure that__ _tg_message_listener_main.py_ properly imports and invokes the __handle_dextools_message__ function when appropriate messages are identified.

__2. Running Your Bot:__

Start your bot by running the main script. __dextools_tg_message_listener.py__ will automatically process relevant messages.

```bash
python tg_message_listener_main.py
```

## Contributing

Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, feel free to fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## Support

For issues, questions, or contributions, please open an issue in the GitHub repository.

Feedback and contributions are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
