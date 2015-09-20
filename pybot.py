#!/usr/bin/python3
import requests, json

class PyBot(object):

    
    def __init__(self):
        self.__emoji = ":smiling_imp:"
        self.__bot_name = "PyBot"
        self.__default_channel = "#random"
        self.URL = "https://hooks.slack.com/services/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"

    def send_message(self, message, channel=None, bot_name=None, emoji=None):
        if channel == None:
            channel = self.__default_channel
        if bot_name == None:
            bot_name = self.__bot_name
        if emoji == None:
            emoji = self.__emoji

        payload = { 'channel': channel, 'username':bot_name, 'text': message, 'icon_emoji':emoji }

        requests.post(self.URL, json.dumps(payload))
