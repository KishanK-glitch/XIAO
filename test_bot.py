import requests
import sys


url = "http://127.0.0.1:8000/chat"


payload = {
    "messages": [
        {"role": "user", "content": "Who are you and what do you know about me?"}
    ]
}


try:
    print(f"Connecting to XIAO at {url}...")
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print("\n SUCCESS. Bot Response:")
        print("--------------------------------------------------")
        print(response.json()["response"])
        print("--------------------------------------------------")
    else:
        print(f"\nERROR {response.status_code}:")
        print(response.text)

except Exception as e:
    print(f"\n FAILED TO CONNECT: {e}")
    print("Is the server running? (Run 'uvicorn app.main:app --reload')")