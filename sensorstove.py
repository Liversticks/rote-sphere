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
    
    
tester1 = sensor(uuid.uuid4(), 'Stove', 'Power', 12345, 1, 'Notareal St', 'Notareal City', 'Atlantis', 'A1A1A1')
random.seed()

while True: 
  #avg stove wattage is 3 kW, so at most it will use 3 kWh per hour
  isused = random.randint(0,1)
  if isused: 
    powerused = random.randint(0, 24)
  else: 
    powerused = 0
  waterused = 0
  time.sleep(28800) #8 hours, or 1/3 day
