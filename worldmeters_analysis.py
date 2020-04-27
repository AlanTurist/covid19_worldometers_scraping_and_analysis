#!/usr/bin/env python
# coding: utf-8

import country_def

count = str(input("\nΕισάγετε χώρα ή ήπειρο: "))
    
if count == "WORLD":
    country_def.country(count,7,7800000000)

elif count == "ITALY":
    country_def.country(count,10,60461826)

elif count == "SPAIN":
    country_def.country(count,9,46754778)
    
elif count == "GERMANY":
    country_def.country(count,12,83783942)
    
elif count == 'NETHERLANDS':
    country_def.country(count,20,17134872)

elif count == 'BELGIUM':
    country_def.country(count,19,11589623)

elif count == "GREECE":
    country_def.country(count,68,10423054)

elif count == "FRANCE":
    country_def.country(count,11,65273511)
    
elif count == "NORWAY":
    country_def.country(count,47,5421241)
    
elif count == "PORTUGAL":
    country_def.country(count,24,10196709)
    
elif count == "SWEDEN":
    country_def.country(count,27,10099265)
    
elif count == "DENMARK":
    country_def.country(count,44,5792202)
    
elif count == "LUXEMBOURG":
    country_def.country(count,60,625978)
    
elif count == "FINLAND":
    country_def.country(count,56,5540720)
		
elif count == "AUSTRIA":
    country_def.country(count,30,9006398)
	
elif count == "CZECHIA":
    country_def.country(count,48,10708981)
	
elif count == "IRELAND":
    country_def.country(count,26,4937786)
	
elif count == "ICELAND":
    country_def.country(count,74,341243)
	
elif count == "CYPRUS":
    country_def.country(count,95,1207359)
	
elif count == "SWITZERLAND":
    country_def.country(count,21,8654622)
	
elif count == "UK":
    country_def.country(count,13,67886011)
    
elif count == 'NORTH AMERICA':
    country_def.country(count,0,579000000)

elif count == 'EUROPE':
    country_def.country(count,1,747636026)

elif count == 'ASIA':
    country_def.country(count,2,4641054775)

elif count == 'SOUTH AMERICA':
    country_def.country(count,3,653962331)

elif count == 'OCEANIA':
    country_def.country(count,4,42677813)

elif count == 'AFRICA':
    country_def.country(count,5,1340598147)

elif count == 'USA':
    country_def.country(count,8,330657799)

elif count == 'TURKEY':
    country_def.country(count,14,84339067)

elif count == 'RUSSIA':
    country_def.country(count,16,145934462)

elif count == 'CANADA':
    country_def.country(count,18,37742154)
    
elif count == 'SAN MARINO':
    country_def.country(count,109,33931)
    
elif count == 'NEW ZEALAND':
    country_def.country(count,81,4822233)
    
elif count == 'AUSTRALIA':
    country_def.country(count,49,25499884)
    
else:
    print("\nΗ χώρα που εισάγατε δεν υπάρχει..\n")

import os
import sys

restart = input("\n\nΑν θέλετε να δοκιμάσετε για άλλη περιοχή πατήστε 'Y' και enter.\n\nΓια να βγείτε από το πρόγραμμα πατήστε μόνο το enter: ")

if restart == "Y":
    os.execl(sys.executable, sys.executable, * sys.argv) 
else:
    print("\nΤο πρόγραμμα κλείνει..")
    sys.exit(0)