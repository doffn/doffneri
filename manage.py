#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from myApp.__init__ import *
from myApp.main_code import main_function, commands, review
import os
import sys
import threading


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

thread_main = threading.Thread(target=main)


# Create the first thread object
thread1 = threading.Thread(target=main_function)

# Create the second thread object
thread2 = threading.Thread(target=commands)
thread3 = threading.Thread(target=review)
try:
    # Start both threads
    thread_main.start()
    thread1.start()
    thread2.start()
    thread3.start()
except Exception as e:
    print(e)
    restart_program()
