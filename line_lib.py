# line-bot lib

from linebot import LineBotApi
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)
from linebot.exceptions import LineBotApiError
lineAPI_key = 'nyxp1IADvO5OqLewq6IAX8j/hoqFXv1JgxCKdLdGBT2HNfMMKR2AnHQilfrmGdcgogJzHqTk2DnnrAUtyBWL7Cyl4HpiTs9jsQcQau84Pddyw4VtUXXKAAL0YUttowb4HZ7KPYy8fDwZ2LUjQCnsIgdB04t89/1O/w1cDnyilFU='#'<Channel access token>'
''' Line API KEY
Api key is "Channel access token" of your line bot.
# 小幫手's: A34ueZBL76277O+nUaELNqO/EWJ2QpqkimobSrwhNLTwZKtylmbE+8OBLQwWPyusq4h6kqzRZMSIJzXxkEK4pBPfoYJH3BDzAmWq77DfmRZY6kLkOHcbDl7XkfsPx7dgcnIdHS9R3i9fK91U0qishgdB04t89/1O/w1cDnyilFU=

'''
line_bot_api = LineBotApi(lineAPI_key)
user_ID = 'U19dcf7c21e18e80d2d22131a65b2fd03'#'<usr/group/room ID>'
''' USER ID
You can use ID to decided sending message to whom.
# 小幫手(虎科群組) C3e319ef3ef6bae6edd1b22db43dc6e1b
# 測試機器人(安迪) U19dcf7c21e18e80d2d22131a65b2fd03
'''


# 傳送訊息至line上，並透過 message_type 來辨別要傳送的訊息格式
def send2LINE(message, message_type):
    if message_type is "text":
        send2LINE_text(message)
    elif message_type is "image":
        send2LINE_image(message)
    elif message_type is "video":
        pass
    elif message_type is "audio":
        pass
    elif message_type is "location":
        pass
    elif message_type is "sticker":
        pass
    else:
        print("Error: error message type")


def send2LINE_text(message):
    try:
        # push_message(<ID>, TextSendMessage(text=""))
        line_bot_api.push_message(user_ID, TextSendMessage(text=message))
    except LineBotApiError as e:
        raise e


def send2LINE_image(url):
    try:
        line_bot_api.push_message(user_ID, ImageSendMessage(url, url, None))
    except LineBotApiError as e:
        raise e
