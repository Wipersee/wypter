import requests
import json


class TelegramBot:
    def __init__(self, token):
        self.url = f"https://api.telegram.org/bot{token}/"
    
    def get_url(self, url):
        response = requests.get(url)
        content = response.content.decode("utf8")
        return content

    def get_json_from_url(self, url):
        content = self.get_url(url)
        js = json.loads(content)
        return js

    def get_updates(self):
        url = self.url + "getUpdates"
        js = self.get_json_from_url(url)
        return js

    def get_last_chat_id_and_text(self, updates):
        try:
            username = updates["message"]["from"]["username"]
            text = updates["message"]["text"]
            chat_id = updates["message"]["chat"]["id"]
            return {"text":text, "chat_id":chat_id, "username":username}
        except IndexError:
            return 0

    def send_message(self , dictionary):
        url = self.url + "sendMessage?text={}&chat_id={}".format(dictionary["text"], dictionary["chat_id"])
        self.get_url(url)
