import os
import slack
from pathlib import Path
from dotenv import load_dotenv

my_secret = os.environ['Slack']

client = slack.WebClient(my_secret)

client.chat_postMessage(channel="#random", text="Try try")