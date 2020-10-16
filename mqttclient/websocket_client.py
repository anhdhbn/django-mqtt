from websocket import create_connection
import json
def send_mess_client(device, mess):
    try:
        ws = create_connection(f"ws://localhost:8000/ws/realtimedata/{device}/")
        ws.send(json.dumps({
            "message": mess
        }))
        ws.close()
    except:
        pass