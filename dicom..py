# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 22:00:52 2019

@author: Nidhi
"""
import csv
import pydicom as dicom
file1=dicom.read_file("bmode.dcm")
file2=dicom.read_file("ttfm.dcm")
ttfm_tags={}
bmode_tags={}
for line in file1:
    ttfm_tags[(line.tag,line.name)]=line.value

for line in file2:
    bmode_tags[(line.tag, line.name)]=line.value
    


with open('output.txt', 'w') as f:

    for key, value in ttfm_tags.items():
        f.write('%s:%s\n' % (key, value))
        
with open('output.txt', 'a') as f:
    f.write("bmode tags")
    for keys, value in bmode_tags.items():
         f.write('%s:%s\n' % (key, value))
     