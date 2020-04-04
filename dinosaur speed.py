'''
You will be supplied with two data files in CSV format .
The first file contains statistics about various dinosaurs. The second file contains additional data.
Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)

Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
Do not print any other information.
'''
#csv1
w1="NAME,LEG_LENGTH,DIET \n \
Hadrosaurus,1.4,herbivore \n \
Struthiomimus,0.72,omnivore \n \
Velociraptor,1.8,carnivore \n \
Triceratops,0.47,herbivore \n \
Euoplocephalus,2.6,herbivore \n \
Stegosaurus,1.50,herbivore \n \
Tyrannosaurus Rex,6.5,carnivore"

#csv2
w2 = "NAME,STRIDE_LENGTH,STANCE \n \
Euoplocephalus,1.97,quadrupedal \n \
Stegosaurus,1.70,quadrupedal \n \
Tyrannosaurus Rex,4.76,bipedal \n \
Hadrosaurus,1.3,bipedal \n \
Deinonychus,1.11,bipedal \n \
Struthiomimus,1.24,bipedal \n \
Velociraptorr,2.62,bipedal"

import math, operator
d = {}
g = 9.2
lines = w2.split("\n")
for line in lines[1:]:
    if "bipedal" not in line:
        continue
    w = line.split(",")
    d[w[0]]=float(w[1])
    
lines = w1.split("\n")
for line in lines[1:]:
    w = line.split(",")
    if d.get(w[0], False):
        stride_len = d[w[0]]
        leg_len = float(w[1])
        speed = abs((stride_len/leg_len) -1) * math.sqrt(leg_len * g)
        d[w[0]]= speed
        

d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
print([d_name for d_name, _ in d])
