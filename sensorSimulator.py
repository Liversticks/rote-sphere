import uuid
import random
import time

class sensor():  
  def __init__(self, uid, type_, resource, address, unit, street, city, country, zippostcode):
    self.uid = uid
    self.type = type_
    self.resource = resource
    self.address = address
    self.unit = unit
    self.street = street
    self.city = city
    self.country = country 
    self.zippostcode = zippostcode
    
class sensorData():
  def __init__(self, uid, datetime, water, power)
  self.uid = uid
  self.datetime = datetime
  self.water = water
  self.power = power
    
tester1 = sensor(uuid.uuid4(), 'Appliance', 'Resource', 12345, 1, 'Notareal St', 'Notareal City', 'Atlantis', 'H0H0H0')
random.seed()

while True: 
    powerused = random.randint(0, 10)
    waterused = random.randint(0, 10)
    time.sleep(3600)
