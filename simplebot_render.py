import os
import simplebot
from threading import Event, Thread
from flask import Flask, request

server = Flask(__name__)

@server.route("/")
def webhook():
    return "!", 200
    
def start_background_loop(bridge_initialized: Event) -> None:
    bridge_initialized.set()
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 10000)))   

server_init = Event()
Thread(
        target=start_background_loop,
        args=(server_init,),
        daemon=True,
).start()
server_init.wait()
