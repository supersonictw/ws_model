#!/usr/bin/python3
# (c) 2020 SuperSonic (https://github.com/supersonictw)

import sys
import asyncio

from tornado.ioloop import IOLoop, PeriodicCallback
from tornado import gen
from tornado.websocket import websocket_connect

callback_url = "ws://localhost:8085/ws"

class Client:
    def __init__(self):
        self.ws = None

    async def connect(self):
        self.ws = await websocket_connect(callback_url)
        await self.run()

    async def run(self):
        while True:
            msg = await self.ws.read_message()
            if msg is None: break
            self.ws.write_message("Hi Hi")
            print(msg)

if __name__ == "__main__":
    client = Client()
    loop = asyncio.get_event_loop()
    asyncio.run(client.connect())
    loop.run_forever()
