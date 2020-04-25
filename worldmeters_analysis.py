#!/usr/bin/env python
# coding: utf-8

import datetime
data = datetime.datetime.now()
data1 = data.strftime("%d-%m-%Y %H:%M:%S")
import pandas as pd
url = 'https://raw.githubusercontent.com/AlanTurist/covid19_worldometers_scraping_and_analysis/master/today_worldwide_covid19_data.csv'
df = pd.read_csv(url,index_col=0, sep=",")

count = str(input("\nΕισάγετε χώρα ή ήπειρο: "))

def country(count, x, y):
    country1 = df.iloc[x]
    D1 = country1['confirmed']
    D2 = country1['new_cases']
    D3 = country1['deaths']
    D4 = country1['recovered']
    D5 = country1['active']
    D6 = country1['critical']
    D7 = country1['new_deaths']
    D8 = country1['total_tests']
    
    print('\n\t~ Ανάλυση δεδομένων του SARS-CoV2 - ',count,'~')
    print('\n\t@Author: Γεώργιος Κολιού, georgios.koliou@gmail.com')
    print('\n****************************************************************************************')
    print("\n\tΣήμερα έχουμε",data1)
    print('\n****************************************************************************************')
    
    print("\n\t1 Ο συνολικός αριθμός κρουσμάτων",count,"είναι:",D1)
    a = (100*D1)/y
    print('\n\t\t1.1 Μολύνθηκε το','{0:.3f}'.format(a),'% του πληθυσμού.')
    
    print("\n\t2. Ο αριθμός των νέων κρουσμάτων είναι:",D2)
    b = (D1 - D2)
    c = (100*D2)/b
    print('\n\t\t2.1 Σε σχέση με χθες, ο αριθμός των κρουσμάτων αυξήθηκε κατά','{0:.2f}'.format(c),'%')
    
    print('\n\t3. Ο συνολικός αριθμός θανάτων είναι:',D3)
    d = (D3 - D7)
    e = (100*D7)/d
    print('\n\t\t3.1 Σε σχέση με χθες, ο αριθμός των θανάτων αυξήθηκε κατά','{0:.2f}'.format(e),'%')
    f = (100*D3)/D1
    print("\n\t\t3.2 Η θνητότητα είναι:",'{0:.2f}'.format(f),'%')
    g = (100*D3)/y
    print("\n\t\t3.3 Η θνησιμότητα είναι:",'{0:.3f}'.format(g),'%')
    
    print('\n\t4. Ο αριθμός όσων ανάρρωσαν είναι:',D4)
    h = (100*D4)/D1
    print('\n\t\t4.1 Ανάρρωσε το','{0:.2f}'.format(h),'%')
    
    print('\n\t5. Ο αριθμός των σοβαρών περιστατικών είναι:',D6)
    i = (100*D6)/D1
    print('\n\t\t5.1 Σοβαρά είναι το','{0:.2f}'.format(i),'%')
    
    print('\n\t6. Ο αριθμός των ενεργών κρουσμάτων είναι:',D5)
    k = (100*D5)/D1
    print('\n\t\t6.1 Τα ενεργά κρούσματα είναι','{0:.1f}'.format(k),'%')
    
    l = ((10000*a)/100)
    print("\n\t7. Τα κρούσματα ανά 10 χιλιάδες πληθυσμού είναι:",'{0:.1f}'.format(l))
    
    j = ((1000000*a)/100)
    print("\n\t8. Τα κρούσματα ανά 1 εκατομμύριο πληθυσμού είναι:",'{0:.1f}'.format(j))

    m = (100*D1)/D8
    print('\n\t9. Χρησιμοποιήθηκαν',D8,'συνολικά τεστ, από τα οποία το','{0:.2f}'.format(m),"% βγήκε θετικό")

    print('\n****************************************************************************************\n\n')
    
    import matplotlib.pyplot as plt
    labels = 'DEATHS','RECOVERED','ACTIVE'
    sizes = [D3, D4, D5]
    explode = (0, 0.1, 0.1)
    fig1, ax1 = plt.subplots(figsize = (24,12))
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    plt.title(count, fontsize = 24) 
    ax1.legend(labels, loc = "upper right") 
    ax1.axis('equal')
    plt.show()

if count == "WORLD":
    country(count,7,7800000000)

elif count == "ITALY":
    country(count,10,60243406)

elif count == "SPAIN":
    country(count,9,47100400)
    
elif count == "GERMANY":
    country(count,12,83149300)
    
elif count == 'NETHERLANDS':
    country(count,20,17414806)

elif count == 'BELGIUM':
    country(count,18,11524454)

elif count == "GREECE":
    country(count,67,10742599)

elif count == "FRANCE":
    country(count,11,64903000)
    
elif count == "NORWAY":
    country(count,46,5367580)
    
elif count == "PORTUGAL":
    country(count,23,10276617)
    
elif count == "SWEDEN":
    country(count,27,10333456)
    
elif count == "DENMARK":
    country(count,43,5822763)
    
elif count == "LUXEMBOURG":
    country(count,59,613894)
    
elif count == "FINLAND":
    country(count,55,5528442)
		
elif count == "AUSTRIA":
    country(count,29,8902600)
	
elif count == "CZECHIA":
    country(count,48,10693939)
	
elif count == "IRELAND":
    country(count,26,6399115)
	
elif count == "ICELAND":
    country(count,72,364260)
	
elif count == "CYPRUS":
    country(count,95,875900)
	
elif count == "SWITZERLAND":
    country(count,21,8570146)
	
elif count == "UK":
    country(count,13,66436000)

elif count == 'NORTH AMERICA':
    country(count,0,579000000)

elif count == 'EUROPE':
    country(count,1,741400000)

elif count == 'ASIA':
    country(count,2,4463000000)

elif count == 'SOUTH AMERICA':
    country(count,3,422500000)

elif count == 'OCEANIA':
    country(count,4,41570842)

elif count == 'AFRICA':
    country(count,5,1216000000)

elif count == 'USA':
    country(count,8,328200000)
    
else:
    print("\nThe country does not exist..\n")

input("Press enter to exit")