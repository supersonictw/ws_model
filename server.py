#!/usr/bin/python3
# (c) 2020 SuperSonic (https://github.com/supersonictw)

import json
from abc import ABC

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from tornado.websocket import WebSocketHandler

class WSHandler(WebSocketHandler, ABC):
    def check_origin(self, origin):
        return True

    def open(self):
        result = {"status": 201}
        self.write_message(json.dumps(result))

    def on_message(self, message):
        result = {"status": 202}
        self.write_message(json.dumps(result))
        for i in range(15):
            self.write_message(str(i))

    def on_close(self):
        pass

if __name__ == "__main__":
    port = 8085
    thread = 4

    app = Application([
        ('/ws', WSHandler)
    ])
    server = HTTPServer(app)
    server.listen(port)
    server.start(thread)
    IOLoop.current().start()
