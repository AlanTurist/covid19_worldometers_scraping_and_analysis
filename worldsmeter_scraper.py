#!/usr/bin/env python
# coding: utf-8

import datetime
date = datetime.datetime.now()
t = date.strftime("%d-%m-%Y")

from covid import Covid

covid = Covid(source = "worldometers")
records = covid.get_data()

country = covid.get_status_by_country_name("greece")
country

import pandas as pd

df = pd.DataFrame(records, columns = ['country', 'confirmed', 'new_cases', 'deaths', 'recovered', 'active', 'critical', 'new_deaths'])

df.to_csv('worldwide_covid19.csv', index = False, encoding = 'utf-8')

input(str("Press enter to exit"))