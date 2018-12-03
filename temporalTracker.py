#!/usr/bin/python3
import os

class temporalTracker:
    attunement = 0

    #list of past attunements, no I will not optimize this it's free work.
    __changelog = []

    def incrementer(self, frequency):
        self.__changelog.append(self.attunement)
        self.attunement = self.attunement + frequency

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
        return popList
            

tt = temporalTracker()
fh = open("inputs/day1", 'r')

for line in fh.readlines():
    tt.incrementer(int(line))

print(tt.attunement)
print(tt.getFirstMatch())