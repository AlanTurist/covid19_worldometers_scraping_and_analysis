#!/usr/bin/env python
# coding: utf-8

import country_def

lang = str(input("\nΓια Ελληνικά πληκτρολογήστε 'GR'\n\nPer Italiano digitare 'IT'\n\nFor English type 'EN': "))
print('\n')
print('*'*110)

if lang == 'GR':
    count = str(input("\nΕισάγετε τη χώρα ή την ήπειρο: "))
    chart = str(input("\nΑν θέλετε να προβληθούν τα διαγράμματα πατήστε 'Y'\n\nΑλλιώς 'enter' για να συνεχίσετε: "))

elif lang == 'IT':
    count = str(input("\nInserire il paese o il continente: "))
    chart = str(input("\nSe si desidera visualizzare i grafici, premere 'Y'\n\nAltrimenti premere 'Invio' per continuare: "))
else:
    count = str(input("\nEnter the country or the continent: "))
    chart = str(input("\nIf you want to view the graphs, press 'Y'\n\nOtherwise press 'Enter' to continue: "))
print('\n')
print('*'*110)

if count == "WORLD":
    country_def.country(lang,chart,count,7,7800000000)

elif count == "NORTH AMERICA":
    country_def.country(lang,chart,count,0,368617633)

elif count == "EUROPE":
    country_def.country(lang,chart,count,1,747585797)
    
elif count == "SOUTH AMERICA":
    country_def.country(lang,chart,count,2,653312637)
    
elif count == 'ASIA':
    country_def.country(lang,chart,count,3,4636642000)

elif count == 'AFRICA':
    country_def.country(lang,chart,count,4,1336955000)

elif count == "OCEANIA":
    country_def.country(lang,chart,count,5,42616559)

elif count == "ITALY":
    country_def.country(lang,chart,count,13,60461826)

elif count == "SPAIN":
    country_def.country(lang,chart,count,11,46754778)
    
elif count == "GERMANY":
    country_def.country(lang,chart,count,15,83783942)
    
elif count == 'NETHERLANDS':
    country_def.country(lang,chart,count,26,17134872)

elif count == 'BELGIUM':
    country_def.country(lang,chart,count,23,11589623)

elif count == "GREECE":
    country_def.country(lang,chart,count,81,10423054)

elif count == "FRANCE":
    country_def.country(lang,chart,count,14,65273511)
    
elif count == "NORWAY":
    country_def.country(lang,chart,count,57,5421241)
    
elif count == "PORTUGAL":
    country_def.country(lang,chart,count,32,10196709)
    
elif count == "SWEDEN":
    country_def.country(lang,chart,count,30,10099265)
    
elif count == "DENMARK":
    country_def.country(lang,chart,count,50,5792202)
    
elif count == "LUXEMBOURG":
    country_def.country(lang,chart,count,71,625978)
    
elif count == "FINLAND":
    country_def.country(lang,chart,count,66,5540720)
		
elif count == "AUSTRIA":
    country_def.country(lang,chart,count,45,9006398)
	
elif count == "CZECHIA":
    country_def.country(lang,chart,count,55,10708981)
	
elif count == "IRELAND":
    country_def.country(lang,chart,count,36,4937786)
	
elif count == "ICELAND":
    country_def.country(lang,chart,count,93,341243)
	
elif count == "CYPRUS":
    country_def.country(lang,chart,count,114,1207359)
	
elif count == "SWITZERLAND":
    country_def.country(lang,chart,count,31,8654622)
	
elif count == "UK":
    country_def.country(lang,chart,count,12,67886011)
    
elif count == 'USA':
    country_def.country(lang,chart,count,8,330657799)

elif count == 'TURKEY':
    country_def.country(lang,chart,count,16,84339067)

elif count == 'RUSSIA':
    country_def.country(lang,chart,count,9,145934462)

elif count == 'CANADA':
    country_def.country(lang,chart,count,20,37742154)
    
elif count == 'SAN MARINO':
    country_def.country(lang,chart,count,128,33931)
    
elif count == 'NEW ZEALAND':
    country_def.country(lang,chart,count,99,4822233)
    
elif count == 'AUSTRALIA':
    country_def.country(lang,chart,count,62,25499884)

elif count == 'BRAZIL':
    country_def.country(lang,chart,count,10,212559417)
    
else:
    print("\nArea doesn't exists..\n")

import os
import sys

restart = input("\n\nIf you want to try another area, press 'Y' and 'enter'.\n\nTo exit press 'enter': ")

if restart == "Y":
    os.execl(sys.executable, sys.executable, * sys.argv) 
else:
    print("\nExit..")
    sys.exit(0)
    