import requests
import Services

__all__ = ['send_get']

def send_get(url, headers):
    response = requests.get(url=url, headers=headers)
    Services.Log.info(msg=f"request to {url} status: {response.status_code}")

    try:
        json = response.json()
    except:
        json = {}
    return json
