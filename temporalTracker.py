#!/usr/bin/python3
import os

class temporalTracker:
    attunement = 0

    #list of past attunements, no I will not optimize this it's free work.
    __changelog = []
    __firstChild = None

    def incrementer(self, frequency):
        self.__changelog.append(self.attunement)
        self.attunement = self.attunement + frequency

    #I don't remember any of this algorithms shit but I have plenty of memory lmao.
    def getFirstMatch(self, inputs):
        for frequency in inputs:
            self.incrementer(int(frequency))
            if self.attunement in self.__changelog:
                return self.attunement
        return 0
        #We've failed to find a match, we must continue to grow the list of frequencies.
        
    
    def getFirstChild(self):
        return self.__changelog
            

tt = temporalTracker()
fh = open("inputs/day1", 'r')
#inputs = fh.readlines()
inputs = [3, 3, 4, -2, -4]
for line in inputs:
    tt.incrementer(int(line))
print(tt.attunement)

first = 0
iter = 0
while not first:
    first = tt.getFirstMatch(inputs)
    iter = iter + 1
    if iter > 200:
        break
#print(tt.getFirstChild())

print(len(tt.getFirstChild()))
print(first)