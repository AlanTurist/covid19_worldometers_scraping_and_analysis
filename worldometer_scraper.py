#!/usr/bin/env python
# coding: utf-8

from covid import Covid

covid = Covid(source = "worldometers")
records = covid.get_data()

import pandas as pd

df = pd.DataFrame(records, columns = ['country', 'confirmed', 'new_cases', 'deaths', 
'recovered', 'active', 'critical', 'new_deaths', 'total_tests', 'population'])

df.to_csv('today_worldwide_covid19_data.csv', index = False, encoding = 'utf-8')