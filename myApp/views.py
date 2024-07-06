from django.shortcuts import render
import requests
import json
import os
import csv

import requests

def send_message_to_telegram_bot(bot_token, chat_id, message_text):
    """
    Sends a message to a Telegram bot.
    
    Args:
        bot_token (str): The authentication token of the Telegram bot.
        chat_id (str): The unique identifier for the chat or user to send the message to.
        message_text (str): The text of the message to be sent.
    
    Returns:
        dict: The response from the Telegram API, containing information about the sent message.
    """
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message_text
    }
    response = requests.post(url, data=data)
    return response.json()


def home(request):
    return render(request, 'myApp/index.html')

def about(request):
    return render(request, 'myApp/about.html')

def contact(request):
    print("I am inside contact")
    print(request)
    if request.method == 'GET':
        bot_token = os.getenv("TOKEN")
        chat_id = os.getenv("ID")
        name = request.POST.get('Name')
        email = request.POST.get('email')
        message_text = f"New message from {name} ({email}):\n{request.POST.get('Message')}"
        print(message_text)

        response = send_message_to_telegram_bot(bot_token, chat_id, message_text)
        print(response)
        print(request.POST)
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
    return render(request, 'myApp/work.html', context={"jsonString": jsonString})
