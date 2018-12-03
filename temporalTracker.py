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
        if self.attunement in self.__changelog:
            self.__firstChild = self.attunement

    #I don't remember any of this algorithms shit but I have plenty of memory lmao.
    def getFirstMatch(self):
        popList = []
        pushList = self.__changelog
        #Whoops
        pushList.append(self.attunement)
        for attunement in pushList:
            if attunement in popList:
                return attunement
            else:
                popList.append(attunement)
                pushList = pushList[1:]
        #We've failed to find a match, we must continue to grow the list of frequencies.
        
    
    def getFirstChild(self):
        return self.__firstChild
            

tt = temporalTracker()
fh = open("inputs/day1", 'r')
testarr = []
for line in fh.readlines():
    tt.incrementer(int(line))
for line in fh.readlines():
    tt.incrementer(int(line))
for line in fh.readlines():
    tt.incrementer(int(line))
for line in fh.readlines():
    tt.incrementer(int(line))
for line in fh.readlines():
    tt.incrementer(int(line))
for line in fh.readlines():
    tt.incrementer(int(line))
for line in fh.readlines():
    tt.incrementer(int(line))
for line in fh.readlines():
    tt.incrementer(int(line))
for line in fh.readlines():
    tt.incrementer(int(line))
for line in fh.readlines():
    tt.incrementer(int(line))
for line in fh.readlines():
    tt.incrementer(int(line))
for line in fh.readlines():
    tt.incrementer(int(line))

print(tt.attunement)
print(tt.getFirstMatch())
print(tt.getFirstChild())