import datetime
data = datetime.datetime.now()
data1 = data.strftime("%d-%m-%Y %H:%M:%S")

import pandas as pd
url = 'https://raw.githubusercontent.com/AlanTurist/covid19_worldometers_scraping_and_analysis/master/today_worldwide_covid19_data.csv'
df = pd.read_csv(url,index_col=0, sep=",")

def country(lang, chart, count, x, y):
    country1 = df.iloc[x]
    D1 = country1['confirmed']
    D2 = country1['new_cases']
    D3 = country1['deaths']
    D4 = country1['recovered']
    D5 = country1['active']
    D6 = country1['critical']
    D7 = country1['new_deaths']
    D8 = country1['total_tests']
    
    if lang == 'GR':

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
        r = ((1000*a)/100)
        print("\n\t\t1.4 Τα κρούσματα ανά 10 χιλιάδες πληθυσμού είναι:",'{0:.1f}'.format(l),'(','{0:.1f}'.format(r),'‰)') 
        if y > 1000000:
            j = ((1000000*a)/100)
            print("\n\t\t1.5 Τα κρούσματα ανά 1 εκατομμύριο πληθυσμού είναι:",'{0:.1f}'.format(j))
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
        q = ((1000*D3)/y)
        print('\n\t\t2.5 Οι θανάτοι ανά 10 χιλιάδες πληθυσμού είναι:','{0:.1f}'.format(o),'(','{0:.1f}'.format(q),'‰)')
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
            print('\n\t6. Πραγματοποιήθηκαν συνολικά',D8,'δειγματοληψίες, από τις οποίες το','{0:.2f}'.format(m),"% ήταν θετικές")
            s = ((100*D8)/y)
            print('\n\t\t6.1 Έχουν πραγματοποιηθεί δειγματοληψίες στο','{0:.2f}'.format(s),'% του πληθυσμού της περιοχής')
        else:
            print('\n\t6. Δεν υπάρχουν δεδομένα για δειγματοληψίες..')
    
        print('\n')
        print('*'*110)

        if chart == "Y":

            import matplotlib.pyplot as plt

            labels = 'ΘΑΝΑΤΟΙ','ΑΝΑΡΡΩΣΑΝ','ΕΝΕΡΓΟΙ'
            sizes = [D3, D4, D5]
            explode = (0, 0.1, 0.1)
            fig1,ax1 = plt.subplots(figsize = (24,12))
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
            plt.title(count, fontsize = 24) 
            ax1.legend(labels, loc = "upper right") 
            ax1.axis('equal')
            plt.show()

            if D8 !=0:
                labels = 'ΠΛΗΘΥΣΜΟΣ','ΔΕΙΓΜΑΤΑ'
                sizes = [y, D8]
                explode = (0, 0)
                fig1,ax1 = plt.subplots(figsize = (24,12))
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
                plt.title(count, fontsize = 24) 
                ax1.legend(labels, loc = "upper right") 
                ax1.axis('equal')
                plt.show()
            else:
                pass

            data = {'Νέοι θάνατοι': D7, 'Θάνατοι': D3}
            names = list(data.keys())
            values = list(data.values())

            fig, axs = plt.subplots(1, 3, figsize=(15, 9), sharey=True)
            axs[0].bar(names, values)
            axs[1].scatter(names, values)
            axs[2].plot(names, values)
            fig.suptitle('Σύγκριση σημερινών θανάτων - '+ count)
            plt.show()

            data = {'Νέα κρούσματα': D2, 'Κρούσματα': D1}
            names = list(data.keys())
            values = list(data.values())

            fig, axs = plt.subplots(1, 3, figsize=(15, 9), sharey=True)
            axs[0].bar(names, values)
            axs[1].scatter(names, values)
            axs[2].plot(names, values)
            fig.suptitle('Σύγκριση σημερινών κρουσμάτων - '+ count)
            plt.show()
        else:
            pass
    
    elif lang == 'IT':

        print('\n\t~ Analisi di dati per SARS-CoV2 -',count,'~')
        print('\n\t@Author: Koliou Georgios, georgios.koliou@gmail.com\n')
        print('*'*110)
        print("\n\tOggi è il",data1,'\n')
        print("*"*50,count,"*"*50)
    
        print("\n\t1. Il numero totale dei casi è:",D1)
        a = (100*D1)/y
        print("\n\t\t1.1 È stato infettato il",'{0:.2f}'.format(a),"% dell'area.")
        print("\n\t\t1.2 Il numero dei nuovi casi è:",D2)
        b = (D1 - D2)
        c = (100*D2)/b
        print('\n\t\t1.3 Rispetto a ieri, il numero di casi è aumentato di','{0:.2f}'.format(c),'%')
        l = ((10000*a)/100)
        r = ((1000*a)/100)
        print("\n\t\t1.4 I casi per 10K abitanti sono:",'{0:.1f}'.format(l),'(','{0:.1f}'.format(r),'‰)') 
        if y > 1000000:
            j = ((1000000*a)/100)
            print("\n\t\t1.5 I casi per 1M abitanti sono:",'{0:.1f}'.format(j))
        else:
            print("\n\t\t1.5 L'area ha una popolazione di meno di un milione..")
    
        print('\n\t2. Il numero totale di deceduti è:',D3)
        print('\n\t\t2.1 Il nuovo numero di deceduti è:',D7)
        d = (D3 - D7)
        e = (100*D7)/d
        print('\n\t\t2.2 Rispetto a ieri, il numero di deceduti è aumentato di','{0:.2f}'.format(e),'%')
        f = (100*D3)/D1
        print("\n\t\t2.3 La fatalità è:",'{0:.2f}'.format(f),'%')
        g = (100*D3)/y
        print("\n\t\t2.4 La mortalità è:",'{0:.3f}'.format(g),'%')
        o = ((10000*D3)/y)
        q = ((1000*D3)/y)
        print('\n\t\t2.5 I deceduti per ogni 10K di abitanti sono:','{0:.1f}'.format(o),'(','{0:.1f}'.format(q),'‰)')
        if y > 1000000:
            n = ((1000000*D3)/y)
            print('\n\t\t2.6 I deceduti per ogni 1M di abitanti sono:','{0:.1f}'.format(n))
        else:
            print("\n\t\t2.6 L'area ha una popolazione di meno di un milione.")
    
        if D4 != 0:
            print('\n\t3. Il numero dei ricoverati è:',D4)
            h = (100*D4)/D1
            print('\n\t\t3.1 Sono stati ricoverati il','{0:.2f}'.format(h),'%')
        else:
            print('\n\t3. Il numero di coloro che si sono ripresi non è disponibile.')
    
        print('\n\t4. Il numero di casi critici è:',D6)
        i = (100*D6)/D1
        print('\n\t\t4.1 I casi critici sono il','{0:.2f}'.format(i),'%')
    
        print('\n\t5. Il numero dei casi attivi è:',D5)
        k = (100*D5)/D1
        print('\n\t\t5.1 I casi attivi sono il','{0:.1f}'.format(k),'%')
    
        if D8 != 0:
            m = (100*D1)/D8
            print('\n\t6.  È stato eseguito un campionamento totale di',D8,'tamponi, di cui il','{0:.2f}'.format(m),"% sono stati positivi")
            s = ((100*D8)/y)
            print("\n\t\t6.1 I campioni sono stati prelevati dal",'{0:.2f}'.format(s),"% della popolazione dell'area")
        else:
            print('\n\t6. Non ci sono dati per tamponi..')
    
        print('\n')
        print('*'*110)

        if chart == "Y":

            import matplotlib.pyplot as plt

            labels = 'DECEDUTI','RICOVERATI','ATTIVI'
            sizes = [D3, D4, D5]
            explode = (0, 0.1, 0.1)
            fig1,ax1 = plt.subplots(figsize = (24,12))
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
            plt.title(count, fontsize = 24) 
            ax1.legend(labels, loc = "upper right") 
            ax1.axis('equal')
            plt.show()

            if D8 !=0:
                labels = 'POPOLAZIONE','TAMPONI'
                sizes = [y, D8]
                explode = (0, 0)
                fig1,ax1 = plt.subplots(figsize = (24,12))
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
                plt.title(count, fontsize = 24) 
                ax1.legend(labels, loc = "upper right") 
                ax1.axis('equal')
                plt.show()
            else:
                pass

            data = {'Nuovi deceduti': D7, 'Deceduti': D3}
            names = list(data.keys())
            values = list(data.values())

            fig, axs = plt.subplots(1, 3, figsize=(15, 9), sharey=True)
            axs[0].bar(names, values)
            axs[1].scatter(names, values)
            axs[2].plot(names, values)
            fig.suptitle('Confronto dei deceduti di oggi - '+ count)
            plt.show()

            data = {'Nuovi casi': D2, 'Casi': D1}
            names = list(data.keys())
            values = list(data.values())

            fig, axs = plt.subplots(1, 3, figsize=(15, 9), sharey=True)
            axs[0].bar(names, values)
            axs[1].scatter(names, values)
            axs[2].plot(names, values)
            fig.suptitle('Confronto dei casi di oggi - '+ count)
            plt.show()
        else:
            pass

    else:

        print('\n\t~ Data analysis for SARS-CoV2 -',count,'~')
        print('\n\t@Author: Koliou Georgios, georgios.koliou@gmail.com\n')
        print('*'*110)
        print("\n\tToday is the",data1,'\n')
        print("*"*50,count,"*"*50)
    
        print("\n\t1. The number of new cases is:",D1)
        a = (100*D1)/y
        print("\n\t\t1.1 Was infected the",'{0:.2f}'.format(a),"% of area.")
        print("\n\t\t1.2 The number of new cases is:",D2)
        b = (D1 - D2)
        c = (100*D2)/b
        print('\n\t\t1.3 Compared to yesterday, the number of cases has increased by','{0:.2f}'.format(c),'%')
        l = ((10000*a)/100)
        r = ((1000*a)/100)
        print("\n\t\t1.4 The cases for every 10K of inhabitants are:",'{0:.1f}'.format(l),'(','{0:.1f}'.format(r),'‰)') 
        if y > 1000000:
            j = ((1000000*a)/100)
            print("\n\t\t1.5 The cases for 1M inhabitants are:",'{0:.1f}'.format(j))
        else:
            print("\n\t\t1.5 The area has a population of less than a million..")
    
        print('\n\t2. The total number of deaths is:',D3)
        print('\n\t\t2.1 The new number of deaths is:',D7)
        d = (D3 - D7)
        e = (100*D7)/d
        print('\n\t\t2.2 Compared to yesterday, the number of deaths has increased by','{0:.2f}'.format(e),'%')
        f = (100*D3)/D1
        print("\n\t\t2.3 The fatality is:",'{0:.2f}'.format(f),'%')
        g = (100*D3)/y
        print("\n\t\t2.4 The mortality is:",'{0:.3f}'.format(g),'%')
        o = ((10000*D3)/y)
        q = ((1000*D3)/y)
        print('\n\t\t2.5 The deaths for every 10K of inhabitants are:','{0:.1f}'.format(o),'(','{0:.1f}'.format(q),'‰)')
        if y > 1000000:
            n = ((1000000*D3)/y)
            print('\n\t\t2.6 The deaths for every 1M of inhabitants are:','{0:.1f}'.format(n))
        else:
            print("\n\t\t2.6 The area has a population of less than a million..")
    
        if D4 != 0:
            print('\n\t3. Has been recovered:',D4)
            h = (100*D4)/D1
            print('\n\t\t3.1 Has been recovered the','{0:.2f}'.format(h),'%')
        else:
            print('\n\t3. The number of those who have recovered is not available..')
    
        print('\n\t4. The number of critical cases is:',D6)
        i = (100*D6)/D1
        print('\n\t\t4.1 The critical cases are the','{0:.2f}'.format(i),'%')
    
        print('\n\t5. The number of active cases is:',D5)
        k = (100*D5)/D1
        print('\n\t\t5.1 The active cases are the','{0:.1f}'.format(k),'%')
    
        if D8 != 0:
            m = (100*D1)/D8
            print('\n\t6. A total sampling of',D8,'tests was performed, of which the','{0:.2f}'.format(m),"% were positive")
            s = ((100*D8)/y)
            print("\n\t\t6.1 The samples were taken from the",'{0:.2f}'.format(s),"% of the population of the area")
        else:
            print('\n\t6. There are no data for tests ..')
    
        print('\n')
        print('*'*110)

        if chart == "Y":

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

            if D8 !=0:
                labels = 'POPULATION','TEST'
                sizes = [y, D8]
                explode = (0, 0)
                fig1,ax1 = plt.subplots(figsize = (24,12))
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
                plt.title(count, fontsize = 24) 
                ax1.legend(labels, loc = "upper right") 
                ax1.axis('equal')
                plt.show()
            else:
                pass

            data = {'New deaths': D7, 'Deaths': D3}
            names = list(data.keys())
            values = list(data.values())

            fig, axs = plt.subplots(1, 3, figsize=(15, 9), sharey=True)
            axs[0].bar(names, values)
            axs[1].scatter(names, values)
            axs[2].plot(names, values)
            fig.suptitle("Compared today's deaths - "+ count)
            plt.show()

            data = {'New cases': D2, 'Cases': D1}
            names = list(data.keys())
            values = list(data.values())

            fig, axs = plt.subplots(1, 3, figsize=(15, 9), sharey=True)
            axs[0].bar(names, values)
            axs[1].scatter(names, values)
            axs[2].plot(names, values)
            fig.suptitle("Compared today's cases - "+ count)
            plt.show()
        