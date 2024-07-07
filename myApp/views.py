from django.shortcuts import render, redirect
from django.contrib import messages  # For success messages
import telebot
import json
import os
import csv

import requests

bot = telebot.TeleBot(os.getenv("TOKEN"))
ID = os.getenv("ID")

def report(message, channel_id=ID):

    try:
      bot.send_message(chat_id=ID, text=message)
    except Exception as e:
        print(f"Failed to send message: {e}")

def home(request):
    return render(request, 'myApp/index.html')

def about(request):
    return render(request, 'myApp/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('Message')  # Use correct name (case-sensitive)

        # Process the form data (e.g., send email or store in database)
        report(f"name: {name} email: {email} message: {message}")
        # You'll need to implement email sending logic here

        messages.success(request, 'Your message has been sent!')  # Success message


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
