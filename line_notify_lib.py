# line notify lib
import requests
import os

"""
發送 Line Notify 訊息
"""
#testToken = 'pGzPihOReza5lCn3toR5mQeUHC76rpR3f9N4OyNDwIJ'
token = '7tz0YZGqvneIWeOFHbOzfbVpvUUbeLaCuJSVaNEixRV'


def lineNotify(msg, picURI=None):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token
    }

    payload = {'message': msg}
    if picURI != None:
        files = {'imageFile': open(picURI, 'rb')}
        result = requests.post(url, headers=headers,
                               params=payload, files=files)
        # return result.status_code
    else:
        result = requests.post(url, headers=headers, params=payload)


#msg = "Hello Python"
#picURI = "C:/Users/SV/Pictures/Saved Pictures/下載.jpg"
#lineNotify(token, msg, picURI)
