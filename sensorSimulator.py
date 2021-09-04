import uuid
import random
import time

class sensor():  
  def __init__(self, uid, type_, address, unit, street, city, country, zippostcode):
    self.uid = uid
    self.type = type_
    self.address = address
    self.unit = unit
    self.street = street
    self.city = city
    self.country = country 
    self.zippostcode = zippostcode
    
    
tester1 = sensor(uuid.uuid4(), 'Appliance', 12345, 1, 'Notareal St', 'Notareal City', 'Atlantis', 'H0H0H0')
random.seed()

while True: 
    gasused = random.randint(0, 10)
    waterused = random.randint(0, 10)
    time.sleep(3600)
