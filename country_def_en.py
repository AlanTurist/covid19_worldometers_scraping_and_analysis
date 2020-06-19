import datetime
data = datetime.datetime.now()
data1 = data.strftime("%d-%m-%Y %H:%M:%S")


def country_en(y):
    D1 = y['confirmed']
    D2 = y['new_cases']
    D3 = y['deaths']
    D4 = y['recovered']
    D5 = y['active']
    D6 = y['critical']
    D7 = y['new_deaths']
    D8 = y['total_tests']
    D9 = y['population']
    D10 = y['country']
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
        print('\n\t~ Data analysis for SARS-CoV2 -',val,'~')
    print('\n\t@Author: Koliou Georgios, georgios.koliou@gmail.com\n')
    print('*'*110)
    print("\n\tToday is the",data1,'\n')
    for val in D10:
        print("*"*50,val,"*"*50)
    for val in D1:
        print("\n\t1. The total number of cases is:",val)
    
    a = (100*D1)/D9
    a.values
    for val in a:
        print('\n\t\t1.1 Was infected the','{0:.2f}'.format(val),'% of the area.')

    for val in D2:
        print("\n\t\t1.2 The number of new cases is:",val)
    b = (D1 - D2)
    b.values
    c = (100*D2)/b
    c.values
    for val in c:
        print('\n\t\t1.3  Compared to yesterday, the number of cases has increased by','{0:.2f}'.format(val),'%')
    
    l = ((10000*a)/100)
    for val in l:
        print("\n\t\t1.4 The cases in 10K of population are:",'{0:.1f}'.format(val))
        for val in D9:
            if val > 1000000:
                j = ((1000000*a)/100)
                for val in j:
                    print("\n\t\t1.5 The cases in 1M of population are:",'{0:.1f}'.format(val))
            else:
                print('\n\t\t1.5 The area has a population less than a million..')

    
    for val in D3:
        print('\n\t2. The total number of deaths is:',val)
        for val in D7:
            print('\n\t\t2.1 The new number of deaths is:',val)
            d = (D3 - D7)
            d.values
            e = (100*D7)/d
            e.values
            for val in e:
                print('\n\t\t2.2 Compared to yesterday, the number of deaths has increased by','{0:.2f}'.format(val),'%')

    f = (100*D3)/D1
    f.values
    for val in f:
        print("\n\t\t2.3 The fatality is:",'{0:.2f}'.format(val),'%')
    
    for val in D9:
        if val > 0:
            g = (100*D3)/val
            g.values
            for val in g:
                print("\n\t\t2.4 The mortality is:",'{0:.3f}'.format(val),'%')
        else:
            print("\n\t\t2.4 No data por population..")


    for val in D9:
        if val >= 10000:  
            o = ((10000*D3)/val)
            o.values
            for val in o:
                print('\n\t\t2.5 The deaths for every 10K of inhabitants are:','{0:.1f}'.format(val))
        else:
            pass

    for val in D9:
        if val >= 1000000:
            n = ((1000000*D3)/val)
            n.values
            for val in n:
                print('\n\t\t2.6 The deaths for every 1M of inhabitants are:','{0:.1f}'.format(val))
        else:
            print('\n\t\t2.6 The area has a population less than a million..')
    
    for val in D4:
        if val != 0:
            print('\n\t3. Has been recovered:',val)
            h = (100*val)/D1
            h.values
            for val in h:
                print('\n\t\t3.1 Has been recovered the','{0:.2f}'.format(val),'%')
        else:
            print('\n\t3. The number of those who have recovered is not available..')
    
    for val in D6:
        print('\n\t4. The number of critical cases is:',val)

    i = (100*D6)/D1
    i.values
    for val in i:
        print('\n\t\t4.1 The critical cases are the','{0:.2f}'.format(val),'%')
    
    for val in D5:
        print('\n\t5. The number of active cases is:',val)

    k = (100*D5)/D1
    k.values
    for val in k:
        print('\n\t\t5.1 The active cases are the','{0:.1f}'.format(val),'%')
    
    for val in D8:
        if val != 0:
            print("\n\t6. Was perfomed a total sampling of",val,"tests.")
            m = (100*D1)/val
            m.values
            for val in m:
                print('\n\t\t6.1 Which the','{0:.2f}'.format(val),"% were positive")
                s = ((100*D8)/D9)
                s.values
                for val in s:
                    print('\n\t\t6.2 The samples were taken from the','{0:.2f}'.format(val),'% of the population of the area')
        else:
            print('\n\t6. There are no data for tests..')
    
    print('\n')
    print('*'*110)