#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from myApp.__init__ import *
from myApp.main_code import main_function, commands, review
import os
import sys
import concurrent.futures

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

def run_functions_concurrently():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(main_function)
        executor.submit(commands)
        executor.submit(review)

if __name__ == "__main__":
    main()  # Run administrative tasks
    run_functions_concurrently()  # Run functions concurrently
