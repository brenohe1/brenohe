import time
import requests
import threading

def send_request():
    url = 'http://194.61.28.243:8000/2/mensagem?text=Ol%C3%A1,%20esta%20%C3%A9%20uma%20mensagem%20de%20teste%20para%20o%20grupo!'
    while True:
        try:
            response = requests.get(url)
            print(f"Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(30)

# Run the send_request function in a separate thread
thread = threading.Thread(target=send_request)
thread.daemon = True
thread.start()

# Keep the main thread alive to allow the background thread to run
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Process interrupted")
