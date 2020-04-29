import datetime
data = datetime.datetime.now()
data1 = data.strftime("%d-%m-%Y %H:%M:%S")

import pandas as pd
url = 'https://raw.githubusercontent.com/AlanTurist/covid19_worldometers_scraping_and_analysis/master/today_worldwide_covid19_data.csv'
df = pd.read_csv(url,index_col=0, sep=",")

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
    
    print('\n\t~ Ανάλυση δεδομένων του SARS-CoV2 -',count,'~')
    print('\n\t@Author: Γεώργιος Κολιού, georgios.koliou@gmail.com\n')
    print('*'*110)
    print("\n\tΣήμερα έχουμε",data1,'\n')
    print("*"*50,count,"*"*50)
    
    print("\n\t1. Ο συνολικός αριθμός κρουσμάτων είναι:",D1)
    a = (100*D1)/y
    print('\n\t\t1.1 Μολύνθηκε το','{0:.2f}'.format(a),'% της περιοχής.')
    print("\n\t\t1.2 Ο αριθμός των νέων κρουσμάτων είναι:",D2)
    b = (D1 - D2)
    c = (100*D2)/b
    print('\n\t\t1.3 Σε σχέση με χθες, ο αριθμός των κρουσμάτων αυξήθηκε κατά','{0:.2f}'.format(c),'%')
    l = ((10000*a)/100)
    print("\n\t\t1.4 Τα κρούσματα ανά 10 χιλιάδες πληθυσμού είναι:",'{0:.1f}'.format(l)) 
    if y > 1000000:
        j = ((1000000*a)/100)
        print("\n\t\t1.4 Τα κρούσματα ανά 1 εκατομμύριο πληθυσμού είναι:",'{0:.1f}'.format(j))
    else:
        print('\n\t\t1.5 Η περιοχή έχει πληθυσμό λιγότερο του ενός εκατομμυρίου..')
    
    print('\n\t2. Ο συνολικός αριθμός θανάτων είναι:',D3)
    print('\n\t\t2.1 Ο νέος αριθμός θανάτων είναι:',D7)
    d = (D3 - D7)
    e = (100*D7)/d
    print('\n\t\t2.2 Σε σχέση με χθες, ο αριθμός των θανάτων αυξήθηκε κατά','{0:.2f}'.format(e),'%')
    f = (100*D3)/D1
    print("\n\t\t2.3 Η θνητότητα είναι:",'{0:.2f}'.format(f),'%')
    g = (100*D3)/y
    print("\n\t\t2.4 Η θνησιμότητα είναι:",'{0:.3f}'.format(g),'%')
    o = ((10000*D3)/y)
    print('\n\t\t2.5 Οι θανάτοι ανά 10 χιλιάδες πληθυσμού είναι:','{0:.1f}'.format(o))
    if y > 1000000:
        n = ((1000000*D3)/y)
        print('\n\t\t2.6 Οι θανάτοι ανά 1 εκατομμύριο πληθυσμού είναι:','{0:.1f}'.format(n))
    else:
        print('\n\t\t2.6 Η περιοχή έχει πληθυσμό λιγότερο του ενός εκατομμυρίου..')
    
    if D4 != 0:
        print('\n\t3. Ο αριθμός όσων ανάρρωσαν είναι:',D4)
        h = (100*D4)/D1
        print('\n\t\t3.1 Ανάρρωσε το','{0:.2f}'.format(h),'%')
    else:
        print('\n\t3. Ο αριθμός όσων ανάρρωσαν δε διατίθεται..')
    
    print('\n\t4. Ο αριθμός των σοβαρών περιστατικών είναι:',D6)
    i = (100*D6)/D1
    print('\n\t\t4.1 Σοβαρά είναι το','{0:.2f}'.format(i),'%')
    
    print('\n\t5. Ο αριθμός των ενεργών κρουσμάτων είναι:',D5)
    k = (100*D5)/D1
    print('\n\t\t5.1 Τα ενεργά κρούσματα είναι','{0:.1f}'.format(k),'%')
    
    if D8 != 0:
        m = (100*D1)/D8
        print('\n\t6. Πραγματοποιήθηκαν συνολικά',D8,'δειγματοληψίες, από τις οποίες το','{0:.2f}'.format(m),"% ήταν θετικές\n")
    else:
        print('\n\t6. Δεν υπάρχουν δεδομένα για δειγματοληψίες..')
    
    print('\n')
    print('*'*110)
    
    import matplotlib.pyplot as plt
    labels = 'DEATHS','RECOVERED','ACTIVE'
    sizes = [D3, D4, D5]
    explode = (0, 0.1, 0.1)
    fig1,ax1 = plt.subplots(figsize = (24,12))
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    plt.title(count, fontsize = 24) 
    ax1.legend(labels, loc = "upper right") 
    ax1.axis('equal')
    plt.show()