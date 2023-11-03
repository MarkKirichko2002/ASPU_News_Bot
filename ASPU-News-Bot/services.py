import json
import requests

host = "merqury.fun"
def get_news():
    url = f"http://{host}/api/news"
    try:
        response = requests.get(url)
    except:
        return "error"
    response = json.loads(response.text)
    res = response["articles"]
    return res

