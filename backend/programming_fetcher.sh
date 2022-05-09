#!/bin/bash

# A script to fetch programming from the digilib

#Ad Council
rsync --protect-args -a --delete kmnr@cleveland.kmnr.org:/mnt/digilib/"E-Carts & Productions"/E-Carts/"Ad Council"/* ~/automation-rework/media/programming/ad-council

#Ascertainment
rsync --protect-args -a --delete kmnr@cleveland.kmnr.org:/mnt/digilib/"E-Carts & Productions"/E-Carts/Ascertainments/* ~/automation-rework/media/programming/ascertainment

#Earth Date
rsync --protect-args -a --delete kmnr@cleveland.kmnr.org:/mnt/digilib/"E-Carts & Productions"/E-Carts/"Earth Date"/"Current Earth Dates"/* ~/automation-rework/media/programming/earth-date

#Profile America
rsync --protect-args -a --delete kmnr@cleveland.kmnr.org:/mnt/digilib/"E-Carts & Productions"/E-Carts/"Profile America"/"Current PA"/* ~/automation-rework/media/programming/profile-america

#PSA
rsync --protect-args -a --delete kmnr@cleveland.kmnr.org:/mnt/digilib/"E-Carts & Productions"/E-Carts/PSA/* ~/automation-rework/media/programming/PSA

#Science and the Sea
rsync --protect-args -a --delete kmnr@cleveland.kmnr.org:/mnt/digilib/"E-Carts & Productions"/E-Carts/"Science and the Sea"/'Current Science and the Seas'/* ~/automation-rework/media/programming/science-and-the-sea

#Concert News?
rsync --protect-args -a --delete kmnr@cleveland.kmnr.org:/mnt/digilib/lost+found/"Concert News"/* ~/automation-rework/backend/
