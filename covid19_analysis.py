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

elif count == "ITALY":
    country_def.country(lang,chart,count,10,60461826)

elif count == "SPAIN":
    country_def.country(lang,chart,count,9,46754778)
    
elif count == "GERMANY":
    country_def.country(lang,chart,count,13,83783942)
    
elif count == 'NETHERLANDS':
    country_def.country(lang,chart,count,22,17134872)

elif count == 'BELGIUM':
    country_def.country(lang,chart,count,19,11589623)

elif count == "GREECE":
    country_def.country(lang,chart,count,70,10423054)

elif count == "FRANCE":
    country_def.country(lang,chart,count,12,65273511)
    
elif count == "NORWAY":
    country_def.country(lang,chart,count,49,5421241)
    
elif count == "PORTUGAL":
    country_def.country(lang,chart,count,26,10196709)
    
elif count == "SWEDEN":
    country_def.country(lang,chart,count,28,10099265)
    
elif count == "DENMARK":
    country_def.country(lang,chart,count,45,5792202)
    
elif count == "LUXEMBOURG":
    country_def.country(lang,chart,count,64,625978)
    
elif count == "FINLAND":
    country_def.country(lang,chart,count,57,5540720)
		
elif count == "AUSTRIA":
    country_def.country(lang,chart,count,36,9006398)
	
elif count == "CZECHIA":
    country_def.country(lang,chart,count,50,10708981)
	
elif count == "IRELAND":
    country_def.country(lang,chart,count,29,4937786)
	
elif count == "ICELAND":
    country_def.country(lang,chart,count,80,341243)
	
elif count == "CYPRUS":
    country_def.country(lang,chart,count,98,1207359)
	
elif count == "SWITZERLAND":
    country_def.country(lang,chart,count,23,8654622)
	
elif count == "UK":
    country_def.country(lang,chart,count,11,67886011)
    
elif count == 'NORTH AMERICA':
    country_def.country(lang,chart,count,0,579000000)

elif count == 'EUROPE':
    country_def.country(lang,chart,count,1,747636026)

elif count == 'ASIA':
    country_def.country(lang,chart,count,2,4641054775)

elif count == 'SOUTH AMERICA':
    country_def.country(lang,chart,count,3,653962331)

elif count == 'OCEANIA':
    country_def.country(lang,chart,count,4,42677813)

elif count == 'AFRICA':
    country_def.country(lang,chart,count,5,1340598147)

elif count == 'USA':
    country_def.country(lang,chart,count,8,330657799)

elif count == 'TURKEY':
    country_def.country(lang,chart,count,15,84339067)

elif count == 'RUSSIA':
    country_def.country(lang,chart,count,14,145934462)

elif count == 'CANADA':
    country_def.country(lang,chart,count,18,37742154)
    
elif count == 'SAN MARINO':
    country_def.country(lang,chart,count,115,33931)
    
elif count == 'NEW ZEALAND':
    country_def.country(lang,chart,count,87,4822233)
    
elif count == 'AUSTRALIA':
    country_def.country(lang,chart,count,53,25499884)

elif count == 'BRAZIL':
    country_def.country(lang,chart,count,16,212559417)
    
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
    