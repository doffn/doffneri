from django.shortcuts import render, redirect
from django.contrib import messages  # For success messages
import telebot
from telebot import formatting
import json
import os
import csv

import requests

bot = telebot.TeleBot(os.getenv("TOKEN"))
ID = os.getenv("ID")

def report(message, channel_id=ID, ):

    try:
        bot.send_message(chat_id=ID, text=message, parse_mode='MarkdownV2')
    except Exception as e:
        print(f"Failed to send message: {e}")

def home(request):
    return render(request, 'myApp/index.html')

def about(request):
    return render(request, 'myApp/about.html')

def contact(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('Message')
            file = request.FILES.get('attachment')

            text_report = (
                f"New user 🎉🎉🎉🎉\n"
                f"{formatting.mbold('Name:')} {formatting.escape_markdown(name)}\n"
                f"{formatting.mbold('Email:')} {formatting.escape_markdown(email)}\n"
                f"{formatting.mbold('Message:')} {formating.escape_markdown(message)}"
            )

            # Send text message
            bot.send_message(chat_id=ID, text=text_report, parse_mode='MarkdownV2')

            # ✅ PROPER FILE HANDLING
            if file:
                file.seek(0)  # reset pointer

                # If image → send as photo
                if file.content_type.startswith('image'):
                    bot.send_photo(chat_id=ID, photo=file)

                # If video → send as video
                elif file.content_type.startswith('video'):
                    bot.send_video(chat_id=ID, video=file)

                # Otherwise → send as document
                else:
                    bot.send_document(
                        chat_id=ID,
                        document=file,
                        visible_file_name=file.name
                    )

            messages.success(request, "✅ Message sent successfully!")

        except Exception as e:
            print("UPLOAD ERROR:", e)
            messages.error(request, "❌ Something went wrong. Try again.")

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
