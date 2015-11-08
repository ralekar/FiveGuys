import mongodb
from mongodb import *
import csv
import collections
def csvtojson(fname):
    c = Mongodb('test1')
    counties = ['Carlsbad','Chula Vista','Coronado','Del Mar','El Cajon','Encinitas','Escondido','Imperial Beach','La Mesa','Lemon Grove','National City','Oceanside','Poway','San Diego','San Marcos','Santee','Solana Beach','Vista']
    
    with open('USCensus/EducationAttainment.csv') as csvfile:
     	reader = csv.DictReader(csvfile)
     	hashset = set(reader.fieldnames)
     	for row in reader:
         	for rw in row : 
             	    if rw == 'Geography':
                       
      

'''c.set_collection('one')
c.insert(data = {"author": "Mike"})
c.insert(data = {"author": "Mot"})
c.insert(data = {"author": "Msss"})
print c.get_all()  
print c.get_one()
print c.get_range(0,3)
'''
	     
         
