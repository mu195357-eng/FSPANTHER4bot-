# Updated main.py

import os

# Retrieve environment variable for the bot token
BOT_TOKEN = os.getenv('BOT_TOKEN')

# State tracking for signals
signals_state = {}  # Dictionary to track the state of signals

# Function to update signal state

def update_signal(signal_name, state):
    signals_state[signal_name] = state
    print(f"Signal '{signal_name}' updated to {state}")

# Example usage
# update_signal('signal1', True)
