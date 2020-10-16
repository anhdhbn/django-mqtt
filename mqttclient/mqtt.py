import paho.mqtt.client as mqtt
import channels.layers
from asgiref.sync import async_to_sync

topic = "uet/iot"

def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    import json
    from .websocket_client import send_mess_client
    from .models import MqttTest
    if(msg.topic == topic):
        data = json.loads(msg.payload.decode("utf-8"))
        # send_mess_client("device1", msg.payload.decode("utf-8"))
        # print(f'{data["object"]} {data["ambient"]} {data["distance"]}')
        # tmp = MqttTest.objects.create(env_temp=data["object"], obj_tmp=data["ambient"], distance=data["distance"])
        # tmp.save()
        

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)