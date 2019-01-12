# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 22:00:52 2019

@author: Nidhi
"""

import pydicom as dicom
file1=dicom.read_file("bmode.dcm")
file2=dicom.read_file("ttfm.dcm")
ttfm_tags=[]
bmode_tags=[]

for line in file1:
    bmode_tags.append(line.tag)
    
for line in file2:
    ttfm_tags.append(line.tag)

with open('output.txt', 'w') as f:
    for item in bmode_tags:
        f.write("%s\n" % item)
with open('output.txt', 'w') as f:
    for item in ttfm_tags:
        f.write("%s\n" % item)