from textwrap import dedent

import requests

from TwitchChannelPointsMiner.classes.Settings import Events


class Discord(object):
    __slots__ = ["webhook_api", "events", "username", "avatar_url"]

    def __init__(self, webhook_api: str, events: list):
        self.webhook_api = webhook_api
        self.events = [str(e) for e in events]
        self.username = "Twitch Channel Points Miner"
        self.avatar_url = "https://i.imgur.com/X9fEkhT.png"

    def __init__(self, webhook_api: str, events: list, username: str, avatar_url: str):
        self.webhook_api = webhook_api
        self.events = [str(e) for e in events]
        self.username = username
        self.avatar_url = avatar_url

    def send(self, message: str, event: Events) -> None:
        if str(event) in self.events:
            requests.post(
                url=self.webhook_api,
                data={
                    "content": dedent(message),
                    "username": self.username,
                    "avatar_url": self.avatar_url,
                },
            )
