from django.shortcuts import render
import requests
import telegram
import json
import os
import csv

# get envirnment
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("ID")

# Create a bot instance
bot = telegram.Bot(token=TOKEN)

def send_message_markdown(text):
    """
    Sends a text message with Markdown formatting to the specified Telegram chat.

    Args:
        text (str): The message text to be sent, with Markdown formatting.
    """
    try:
        bot.send_message(chat_id=CHAT_ID, text=text, parse_mode='Markdown')
        print(f"Message sent: {text}")
    except telegram.error.TelegramError as e:
        print(f"Error sending message: {e}")



def home(request):
    return render(request, 'myApp/index.html')

def about(request):
    return render(request, 'myApp/about.html')

def contact(request):
    return render(request, 'myApp/contact.html')

def service(request):
    return render(request, 'myApp/service.html')

def work(request):
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRTQ75ssTlfeNEXNuJ9CXV77xwdz4UAUD70chzuda7BwZhN-mZxk_FNMVmozaigGKLLPlfIbGKxTVvB/pub?output=csv"
    response = requests.get(url)
    csvData = response.text
    # parse the CSV data as a list of dictionaries using the csv module
    csvReader = csv.DictReader(csvData.splitlines())
    jsonData = [row for row in csvReader]
    # convert the list of dictionaries to JSON format
    jsonString = json.dumps(jsonData)
    #print(jsonString)
    try:
        send_message(jsonString)
    except Exception as e:
        send_message(f"There was an error while sending: {e}")
    return render(request, 'myApp/work.html', context={"jsonString": jsonString})
