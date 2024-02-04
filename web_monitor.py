import time
import requests
import datetime

interval = 300
num_iterations = 5


def check_status(url):
    try:
        for i in range(num_iterations):
            time_now = datetime.datetime.now()
            response = requests.get(url)
            status = response.status_code
            if response.status_code == 200:
                print(f'Website is UP ({status}) - ', time_now.strftime("%X"))
            elif response.status_code == 404 or response.status_code == 500:
                print(f'Website is DOWN ({status})')
            time.sleep(interval)
    except requests.exceptions.InvalidURL as e:
        print("Invalid URL: ", e)
    except requests.exceptions.RequestException as e:
        print("Error making request: ", e)

print('Monitoring website status...')
check_status(input('Enter the URL of the website to monitor: '))
