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
    
    
tester1 = sensor(uuid.uuid4(), 'Sink', 'Water', 12345, 1, 'Notareal St', 'Notareal City', 'Atlantis', 'A1A1A1')
random.seed()

while True: 
  #avg sink uses 4 - 8 L/min, which we will avg to 6. Thus a sink uses no more than 360 L/min, but realistically no one runs their sink non stop, so we will pick a cap of 
  #~5 minutes of use per hour, aka 30 L
  waterused = random.randint(0, 30)
  powerused = 0
  time.sleep(3600)