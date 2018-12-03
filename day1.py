#!/usr/bin/python3
import os

class temporalTracker:
    attunement = 0

    def incrementer(self, frequency):
        self.attunement = self.attunement + frequency

tt = temporalTracker()
fh = open("inputs/day1", 'r')

for line in fh.readlines():
    tt.incrementer(int(line))

print(tt.attunement)