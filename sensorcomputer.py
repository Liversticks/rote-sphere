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
    
    
tester1 = sensor(uuid.uuid4(), 'Computer', 'Power', 12345, 1, 'Notareal St', 'Notareal City', 'Atlantis', 'A1A1A1')
random.seed()

while True: 
  #avg computer wattage is 60 - 250 watts, so ill pick 200 as a rounder number, meaning it uses at most 0.2 kWh per hour. unfortunate choice of value. 
  hoursused = random.randint(0, 16) / 2
  powerused = hoursused * 0.2
  waterused = 0
  time.sleep(28800) #8 hours
