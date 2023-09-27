# Use the official Python image with the desired version
FROM python:3.11.5

# Install curl and nano
RUN apt-get update && apt-get install -y curl

# Set the working directory in the container
WORKDIR /app

# Clone your GitHub repository
RUN git clone https://github.com/prateekmaru/india-weather-rest .

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Create an empty tg-token.txt file
RUN touch tg-token.txt

# Build argument to pass the Telegram bot token
ARG IMD_TELEGRAM_BOT_TOKEN

# Copy the Telegram bot token into the tg-token.txt file
RUN echo $IMD_TELEGRAM_BOT_TOKEN > tg-token.txt

# Run your main API server and Telegram bot sequentially
CMD ["sh", "-c", "python3 app.py & python3 telegram_bot.py"]

# For Docker Users
# docker build -t india-weather-app --build-arg IMD_TELEGRAM_BOT_TOKEN=your_bot_token .
# docker run -d -p 5001:5001 india-weather-app

# For Podman Users
# podman build -t india-weather-app --build-arg IMD_TELEGRAM_BOT_TOKEN=your_bot_token .
# podman run -d -p 5001:5001 india-weather-app