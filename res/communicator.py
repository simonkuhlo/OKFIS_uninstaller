

class Listener():
    def on_message(self, message:str):
        pass

listeners:list[Listener] = []

def register_listener(listener:Listener):
    listeners.append(listener)

def broadcast(message:str):
    for listener in listeners:
        listener.on_message(message)