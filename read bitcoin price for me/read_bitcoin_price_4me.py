from json import loads
from requests import get
import pyttsx3

def main():
    """getting data using api"""
    try:
        r = get("https://api.coindesk.com/v1/bpi/currentprice.json")
        if r.status_code != 200:
            return web_scrap_error()
    except:
        web_scrap_error()
    
    """get intended data"""
    data = loads(r.text)
    btc_price = int(data["bpi"]["USD"]["rate_float"])
    result = f"Bitcoin current price is {btc_price}"

    """read it by tts"""
    engine = pyttsx3.init()
    engine.say(result)
    print(result)
    engine.runAndWait()

def web_scrap_error():
    print("Program failed to get data from requested link")
    return 1

if __name__  ==  "__main__":
    main()