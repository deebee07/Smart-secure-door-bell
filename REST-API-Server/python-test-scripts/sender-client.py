import paho.mqtt.client as mqtt #import the client1
import time
############
########################################
broker_address="iot.eclipse.org"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client() #create new instance
print("connecting to broker")
client.connect(broker_address) #connect to broker




client.loop_start() #start the loop
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("vhouse/bulbs/bulb1","OFF")
#time.sleep(10) # wait
client.loop_stop() #start the loop

time.sleep(10)
client.loop_start() #start the loop
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("vhouse/bulbs/bulb1","ON")
#time.sleep(10) # wait
client.loop_stop()

time.sleep(10)
client.loop_start() #start the loop
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("vhouse/bulbs/bulb1","STRANGER")
#time.sleep(10) # wait
client.loop_stop() 