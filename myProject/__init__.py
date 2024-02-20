import os

# List of required packages 
required_packages = [
    ('django', 'django'),
    ('time', 'time'),
    ('collections', 'Counter'),
    ('beautifulsoup4==4.11.2', 'BeautifulSoup'),
    ('psutil', 'psutil'),
    ('logging', 'logging'),
    ('random', 'random'),
    ('threading', 'threading'),
    ('json', 'json'),
    ('sys', 'sys'),
    ('telebot', 'telebot'),
   # ('--force-reinstall urllib3==1.26.16', 'urllib3'),
    ('pymongo', 'pymongo'),
    ('schedule', 'schedule'),
   # ('requests', 'requests')
]

## Check if a package is installed
def package_installed(package_name):
    try:
        __import__(package_name)
    except ImportError:
        return False
    else:
        return True

# Install a package using pip
def install_package(package_name):
    os.system(f"pip install {package_name}")

# Import the necessary modules and packages
for package in required_packages:
    package_name, import_name = package
    try:
        if package_installed(package_name):
            globals()[import_name] = __import__(package_name)
            #print("Packages already installed")
        else:
            print(f"Package {package_name} is missing. Please install it.")
            install_package(package_name)
    except Exception as e:
        print(e)


