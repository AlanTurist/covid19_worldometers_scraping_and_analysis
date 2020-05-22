import pandas as pd
url = 'https://raw.githubusercontent.com/AlanTurist/covid19_worldometers_scraping_and_analysis/master/today_worldwide_covid19_data.csv'
df = pd.read_csv(url)

import country_def

count = str(input("\nΕισάγετε χώρα ή περιοχής: "))
x = df[df["country"] == count]

country_def.country(x)

import os
import sys

restart = input("\n\nIf you want to try another area, press 'Y' and 'enter'.\n\nTo exit press 'enter': ")

if restart == "Y":
    os.execl(sys.executable, sys.executable, * sys.argv) 
else:
    print("\nExit..")
    sys.exit(0)