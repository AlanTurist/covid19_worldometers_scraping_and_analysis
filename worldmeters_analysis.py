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
    
    print('\n\t~ Ανάλυση δεδομένων του SARS-CoV2 - ',count,'~\n')
    print('*'*110)
    print('\n\t@Author: Γεώργιος Κολιού, georgios.koliou@gmail.com')
    print("\n\tΣήμερα έχουμε",data1)
    print('\n')
    print("*"*50,count,"*"*50)
    
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
    
    if D4 != 0:
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

    if D8 != 0:
        m = (100*D1)/D8
        print('\n\t9. Χρησιμοποιήθηκαν',D8,'συνολικά τεστ, από τα οποία το','{0:.2f}'.format(m),"% βγήκε θετικό\n")
    
    print('\n')
    print('*'*110)
    print('\n\n')
    
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
    country(count,10,60461826)

elif count == "SPAIN":
    country(count,9,46754778)
    
elif count == "GERMANY":
    country(count,12,83783942)
    
elif count == 'NETHERLANDS':
    country(count,20,17134872)

elif count == 'BELGIUM':
    country(count,18,11589623)

elif count == "GREECE":
    country(count,67,10423054)

elif count == "FRANCE":
    country(count,11,65273511)
    
elif count == "NORWAY":
    country(count,46,5421241)
    
elif count == "PORTUGAL":
    country(count,23,10196709)
    
elif count == "SWEDEN":
    country(count,27,10099265)
    
elif count == "DENMARK":
    country(count,43,5792202)
    
elif count == "LUXEMBOURG":
    country(count,59,625978)
    
elif count == "FINLAND":
    country(count,55,5540720)
		
elif count == "AUSTRIA":
    country(count,29,9006398)
	
elif count == "CZECHIA":
    country(count,48,10708981)
	
elif count == "IRELAND":
    country(count,26,4937786)
	
elif count == "ICELAND":
    country(count,72,341243)
	
elif count == "CYPRUS":
    country(count,95,1207359)
	
elif count == "SWITZERLAND":
    country(count,21,8654622)
	
elif count == "UK":
    country(count,13,67886011)

elif count == 'NORTH AMERICA':
    country(count,0,368869647)

elif count == 'EUROPE':
    country(count,1,747636026)

elif count == 'ASIA':
    country(count,2,4641054775)

elif count == 'SOUTH AMERICA':
    country(count,3,653962331)

elif count == 'OCEANIA':
    country(count,4,42677813)

elif count == 'AFRICA':
    country(count,5,1340598147)

elif count == 'USA':
    country(count,8,330654749)

elif count == 'RUSSIA':
    country(count,16,145923321)

elif count == 'TURKEY':
    country(count,14,84175495)
    
else:
    print("\nΗ χώρα ή η περιοχή που εισάγατε δεν υπάρχει..\n")

input("Press enter to exit")