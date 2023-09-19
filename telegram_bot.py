# Github: github.com/prateekmaru
# Author: Prateek Maru
# Email: prateek@prateekspace.eu.org
# ADD TG BotFather Token Here "tg-token.txt"

import requests
from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Read the Telegram bot token from a text file
with open('tg-token.txt', 'r') as token_file:
    bot_token = token_file.read().strip()

# Fetch the list of base stations from your local server
base_station_url = 'http://127.0.0.1:5001/station/all'
response = requests.get(base_station_url)

if response.status_code == 200:
    base_stations = response.json()["result"]
else:
    print('Failed to fetch base stations. Exiting...')
    exit()

# Initialize your Telegram bot with the bot token read from the file
bot = TeleBot(bot_token)

def send_base_station_list(message):
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    for station in base_stations:
        markup.add(KeyboardButton(f'{station["jurisdiction"]} - {station["station"]}'))

    bot.send_message(message.chat.id, 'Please choose a base station:', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == '/start':
        # Send the list of base stations to the user
        send_base_station_list(message)
    else:
        # Check if the message matches any base station name
        selected_station = None
        for station in base_stations:
            if message.text == f'{station["jurisdiction"]} - {station["station"]}':
                selected_station = station
                break
        
        if selected_station:
            station_id = selected_station['stationId']
            
            # Make a request to your local server with the station ID
            response = requests.get(f'http://127.0.0.1:5001/weather/{station_id}')

            if response.status_code == 200:
                weather_data = response.json()['result']

                # Extract the relevant information from the custom JSON format
                astronomical_info = weather_data['astronomical']
                forecast = weather_data['forecast']

                # Build the entire message with Markdown formatting and emojis
                markdown_message = f"""
🌦 *IMD WEATHER FORECAST 🇮🇳 *

*Astronomical Data:*

🌞 *Sunrise:* {astronomical_info["sunrise"]}
🌅 *Sunset:* {astronomical_info["sunset"]}
🌝 *Moonrise:* {astronomical_info["moonrise"]}
🌚 *Moonset:* {astronomical_info["moonset"]}

*Weather Forecast:*
"""
                for day in forecast:
                    markdown_message += f"""
📅 *Date:* {day["date"]}
🌦 *Condition:* {day["condition"]}
🌡 *Max Temperature:* {day["max"]}°C
❄️ *Min Temperature:* {day["min"]}°C
"""

                # Send the entire message with Markdown formatting as one message
                bot.send_message(message.chat.id, markdown_message, parse_mode="Markdown")
            else:
                bot.send_message(message.chat.id, 'An error occurred while fetching the weather forecast.')
        else:
            bot.send_message(message.chat.id, 'Please choose a valid base station from the list.')

# Start the bot polling
bot.polling()
