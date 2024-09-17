
# Discord License Key Bot

This bot generates and verifies license keys within a Discord channel. Administrators can generate license keys using the `!genkey` command, and users or applications can verify keys using the `!verifykey <key>` command.

## Features

- Generates 16-character alphanumeric license keys
- Verifies license keys
- Offers to generate a license key for a user if the key is invalid

## Setup

1. Clone the repository.
2. Install dependencies:

   ```
   pip install discord.py python-dotenv
   ```

3. Create a `.env` file and add your Discord bot token:

   ```
   DISCORD_TOKEN=your_discord_bot_token
   ```

4. Run the bot:

   ```
   python bot.py
   ```

## Commands

- `!genkey`: Generates a new license key (Admin only).
- `!verifykey <key>`: Verifies if a given key is valid.

## Application-side Key Verification

To integrate this with your application:

1. Upon launch, the application asks for a license key.
2. The application sends a message to a specific Discord channel (through the bot or an API) with the key:
   ```
   !verifykey YOUR_LICENSE_KEY
   ```

3. If the key is valid, the application proceeds. If not, the bot will ask:
   - "Would you like to generate a key for this user?"
   - Admins can choose to create or deny the request.

Example in your app:

```python
import requests

def verify_license_in_discord(key):
    # This function sends a message to the Discord bot to verify the license
    discord_webhook_url = 'YOUR_DISCORD_WEBHOOK_URL'
    message = f'!verifykey {key}'
    data = {"content": message}

    response = requests.post(discord_webhook_url, json=data)

    if response.status_code == 204:  # Webhook executed successfully
        print("License verification request sent.")
    else:
        print("Failed to send license verification request.")

def launch_application():
    license_key = input("Enter your license key: ")
    verify_license_in_discord(license_key)

launch_application()
```

## Requirements

- Python 3.6 or higher
- discord.py
- python-dotenv
