import requests
import os 
import sys


from argparse import ArgumentParser

parser = ArgumentParser(description='get the current weather information for your zipcode')
parser.add_argument('zip', help="zip/postal code to get weather for ")
parser.add_argument('--country', default="uk", help="country zip belongs to, default is uk ")

args = parser.parse_args()

api_key = os.getenv("OWM_API_KEY")
if not api_key:
    print("Error: no apî key ")

url = f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"


res = requests.get(url)

if res.status_code != 200:
    print(f" Error talking to weather provider: {res.status_code}")
    sys.exit

print(res.json())

