import mongodb
from mongodb import *
import csv

def csvtojson(fname):
    c = Mongodb('test1')
    counties = ['Carlsbad','Chula Vista','Coronado','Del Mar','El Cajon','Encinitas','Escondido','Imperial Beach','La Mesa','Lemon Grove','National City','Oceanside','Poway','San Diego','San Marcos','Santee','Solana Beach','Vista']
      

'''c.set_collection('one')
c.insert(data = {"author": "Mike"})
c.insert(data = {"author": "Mot"})
c.insert(data = {"author": "Msss"})
print c.get_all()  
print c.get_one()
print c.get_range(0,3)
'''

