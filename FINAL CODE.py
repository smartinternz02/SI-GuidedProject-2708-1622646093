import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "3t5oej",
        "typeId": "externship",
        "deviceId":"123456"
    },
    "auth": {
        "token": "1234567890"
    }
}

def myCommandCallback(cmd):
    p=cmd.data['command']
    print()
    if(p=="motoron"):
        print(".....Manually Motor is TURNED ON.....")
    elif(p=="motoroff"):
        print(".....Manually Motor is TURNED OFF.....")
    print()
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
while True:
    temp=random.randint(-20,125)
    hum=random.randint(0,100)
    moist=random.randint(0,100)
    myData={'d':{'name':"projectiot", 'temperature':temp, 'humidity':hum, 'soilmoisture':moist}}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    print()
    print()
    if(moist<=30):
        print(".....According to Moisture levels , Motor is TURNED ON Automatically.....")
    elif(moist>30):
        print(".....According to Moisture levels, Motor is TURNED OFF Automatically.....")
    print()
    print()
    client.commandCallback = myCommandCallback
    time.sleep(3)
client.disconnect()
