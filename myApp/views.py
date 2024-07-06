from django.shortcuts import render
import telegram
import json
import os
import csv

import requests

bot = telebot.TeleBot(os.getenv("TOKEN"))


chat_id = os.getenv("ID")

def report(message, channel_id=ID):

    try:
      bot.send_message(chat_id=chat_id, text=message, parse_mode='MarkdownV2')
    except Exception as e:
        print(f"Failed to send message: {e}")

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

        response = report("hi there")
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
