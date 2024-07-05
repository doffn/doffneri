from django.shortcuts import render
import requests
import json
import os
import csv


def home(request):
    return render(request, 'myApp/index.html')

def about(request):
    return render(request, 'myApp/about.html')

def contact(request):
    if request.method == 'POST':
        # Handle form submission
        form = MyForm(request.POST)
        if form.is_valid():
            # Process valid form data
            name = form.cleaned_data['Name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['Message']
            # (Your logic to send data to Google Sheet or database)
            return render(request, 'success.html')  # Redirect to success page
        else:
            # Handle invalid form data (e.g., display errors)
            return render(request, 'contact.html', {'form': form})  # Render form with errors
    else:
        # Initial GET request (display blank form)
        form = MyForm()
        return render(request, 'contact.html', {'form': form})

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
