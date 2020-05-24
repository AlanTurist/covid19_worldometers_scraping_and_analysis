import datetime
data = datetime.datetime.now()
data1 = data.strftime("%d-%m-%Y %H:%M:%S")

def country(x):
    D1 = x['confirmed']
    D2 = x['new_cases']
    D3 = x['deaths']
    D4 = x['recovered']
    D5 = x['active']
    D6 = x['critical']
    D7 = x['new_deaths']
    D8 = x['total_tests']
    D9 = x['population']
    D10 = x['country']
    D1.values
    D2.values
    D3.values
    D4.values
    D5.values
    D6.values
    D7.values
    D8.values
    D9.values
    D10.values

    for val in D10:
        print('\n\t~ Ανάλυση δεδομένων του SARS-CoV2 -',val,'~')
    print('\n\t@Author: Γεώργιος Κολιού, georgios.koliou@gmail.com\n')
    print('*'*110)
    print("\n\tΣήμερα έχουμε",data1,'\n')
    for val in D10:
        print("*"*50,val,"*"*50)
    for val in D1:
        print("\n\t1. Ο συνολικός αριθμός κρουσμάτων είναι:",val)
    
    a = (100*D1)/D9
    a.values
    for val in a:
        print('\n\t\t1.1 Μολύνθηκε το','{0:.2f}'.format(val),'% της περιοχής.')

    for val in D2:
        print("\n\t\t1.2 Ο αριθμός των νέων κρουσμάτων είναι:",val)
    b = (D1 - D2)
    b.values
    c = (100*D2)/b
    c.values
    for val in c:
        print('\n\t\t1.3 Σε σχέση με χθες, ο αριθμός των κρουσμάτων αυξήθηκε κατά','{0:.2f}'.format(val),'%')

    l = ((10000*a)/100)
    for val in l:
        print("\n\t\t1.4 Τα κρούσματα ανά 10 χιλιάδες πληθυσμού είναι:",'{0:.1f}'.format(val))
        for val in D9:
            if val > 1000000:
                j = ((1000000*a)/100)
                for val in j:
                    print("\n\t\t1.5 Τα κρούσματα ανά 1 εκατομμύριο πληθυσμού είναι:",'{0:.1f}'.format(val))
            else:
                print('\n\t\t1.5 Η περιοχή έχει πληθυσμό λιγότερο του ενός εκατομμυρίου..')

    l = ((10000*a)/100)
    l.values
    r = ((1000*a)/100)
    r.values
    
    for val in D3:
        print('\n\t2. Ο συνολικός αριθμός θανάτων είναι:',val)
        for val in D7:
            print('\n\t\t2.1 Ο νέος αριθμός θανάτων είναι:',val)
            d = (D3 - D7)
            d.values
            e = (100*D7)/d
            e.values
            for val in e:
                print('\n\t\t2.2 Σε σχέση με χθες, ο αριθμός των θανάτων αυξήθηκε κατά','{0:.2f}'.format(val),'%')

    f = (100*D3)/D1
    f.values
    for val in f:
        print("\n\t\t2.3 Η θνητότητα είναι:",'{0:.2f}'.format(val),'%')
    
    for val in D9:
        if val > 0:
            g = (100*D3)/val
            g.values
            for val in g:
                print("\n\t\t2.4 Η θνησιμότητα είναι:",'{0:.3f}'.format(val),'%')
        else:
            print("\n\t\t2.4 Δεν υπάρχουν δεδομένα για τον πληθυσμό")


    for val in D9:
        if val >= 10000:  
            o = ((10000*D3)/val)
            o.values
            for val in o:
                print('\n\t\t2.5 Οι θανάτοι ανά 10 χιλιάδες πληθυσμού είναι:','{0:.1f}'.format(val))
        else:
            pass

    for val in D9:
        if val >= 1000000:
            n = ((1000000*D3)/val)
            n.values
            for val in n:
                print('\n\t\t2.6 Οι θανάτοι ανά 1 εκατομμύριο πληθυσμού είναι:','{0:.1f}'.format(val))
        else:
            print('\n\t\t2.6 Η περιοχή έχει πληθυσμό λιγότερο του ενός εκατομμυρίου..')
    
    for val in D4:
        if val != 0:
            print('\n\t3. Ο αριθμός όσων ανάρρωσαν είναι:',val)
            h = (100*val)/D1
            h.values
            for val in h:
                print('\n\t\t3.1 Ανάρρωσε το','{0:.2f}'.format(val),'%')
        else:
            print('\n\t3. Ο αριθμός όσων ανάρρωσαν δε διατίθεται..')
    
    for val in D6:
        print('\n\t4. Ο αριθμός των σοβαρών περιστατικών είναι:',val)

    i = (100*D6)/D1
    i.values
    for val in i:
        print('\n\t\t4.1 Σοβαρά είναι το','{0:.2f}'.format(val),'%')
    
    for val in D5:
        print('\n\t5. Ο αριθμός των ενεργών κρουσμάτων είναι:',val)

    k = (100*D5)/D1
    k.values
    for val in k:
        print('\n\t\t5.1 Τα ενεργά κρούσματα είναι','{0:.1f}'.format(val),'%')
    
    for val in D8:
        if val != 0:
            print("\n\t6. Πραγματοποιήθηκαν συνολικά",val,"δειγματοληψίες.")
            m = (100*D1)/val
            m.values
            for val in m:
                print('\n\t\t6.1 Από το σύνολο των δειγματοληψιών, το','{0:.2f}'.format(val),"% ήταν θετικές")
                s = ((100*D8)/D9)
                s.values
                for val in s:
                    print('\n\t\t6.2 Έχουν πραγματοποιηθεί δειγματοληψίες στο','{0:.2f}'.format(val),'% του πληθυσμού της περιοχής')
        else:
            print('\n\t6. Δεν υπάρχουν δεδομένα για δειγματοληψίες..')
    
    print('\n')
    print('*'*110)