from tornado.websocket import WebSocketHandler as ws


class WSEcho(ws):
    def open(self):
        print("WebSocket open")

    def on_message(self, message):  # 客户端向服务端发送msg后触发
        self.write_message(message)  # 广播回复msg

    def on_pong(self, data):
        print(data)

    def on_close(self):
        print("WebSocket closed")
