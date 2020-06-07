import pandas as pd
url = 'https://raw.githubusercontent.com/AlanTurist/covid19_worldometers_scraping_and_analysis/master/today_worldwide_covid19_data.csv'
df = pd.read_csv(url)

language = str(input("\nΓια Ελληνικά πατήστε GR\n\nFor English press EN: "))

if language == "GR":
    import country_def
    count = str(input("\nΕισάγετε χώρα ή περιοχή: "))
    x = df[df["country"] == count]
    country_def.country(x)

elif language == "EN":
    import country_def_en
    count1 = str(input("\nInsert area or country: "))
    y = df[df["country"] == count1]
    country_def_en.country_en(y)
else:
    print("Wrong language..")

import os
import sys

restart = input("\n\nIf you want to try another area, press 'Y' and 'enter'.\n\nTo exit press 'enter': ")

if restart == "Y":
    os.execl(sys.executable, sys.executable, * sys.argv) 
else:
    print("\nExit..")
    sys.exit(0)