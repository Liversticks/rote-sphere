import uuid
import random
import time

class sensor():  
  def __init__(self, uid, type_):
    self.uid = uid
    self.type = type_
    
tester1 = sensor(uuid.uuid4(), 'Appliance')
random.seed()

while True: 
    print random.randint(0, 10)
    time.sleep(10)
