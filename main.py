# Actively monitor internet connection every 30 seconds
import requests
import matplotlib.pyplot as plt
import time

def create_request():
    try:
        requests.head('https://google.com')
    except:
        with open("downtimes.txt", "a") as f:
            f.write("Internet down at: " + str(time.time()) + "\n")
            print("Request failed")

def start_code():
    while True:
        create_request()
        time.sleep(5)

start_code()
