from django.shortcuts import render
import telegram
import json
import os
import csv

import requests

bot_token = os.getenv("TOKEN")
chat_id = os.getenv("ID")

def send_message_to_bot(bot_token, chat_id, message):
    """
    Sends a message to a Telegram bot.

    Args:
        bot_token (str): The API token of the Telegram bot.
        chat_id (int): The chat ID of the recipient.
        message (str): The message to be sent.
    """
    bot = telegram.Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

def home(request):
    return render(request, 'myApp/index.html')

def about(request):
    return render(request, 'myApp/about.html')

def contact(request):
    print("I am inside contact")
    print(request)
    if request.method == 'GET':
        name = request.GET.get('Name')
        email = request.GET.get('email')
        message_text = f"New message from {name} ({email}):\n{request.POST.get('Message')}"
        print(message_text)

        response = send_message_to_bot(bot_token, chat_id, "Hi there")
        print(response)
        print(request.GET)
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
