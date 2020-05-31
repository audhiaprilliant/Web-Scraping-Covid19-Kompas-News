#!/usr/bin/env python
# coding: utf-8
# author: audhiaprilliant

# Modules for web scraping
import requests
from bs4 import BeautifulSoup
# Module for data manipulation
import pandas as pd
# Module for regular expression
import re
# Module for file management
import os
# Module for timing
from datetime import datetime
# URL
url = 'https://www.kompas.com/covid-19'
dir_path = os.getcwd()
startTime = datetime.now()

if __name__ == "__main__":
    # Get the url
    page = requests.get(url)

    # Wrangling HTML with BeautifulSoup
    soup = BeautifulSoup(page.content,'html.parser')
    job_elems = soup.find_all('div',class_='covid__box')

    # Get the date
    date_scrape = soup.find('span',class_='covid__date').text
    date_scrape = re.findall(r'Update terakhir: (\S+.+WIB)',date_scrape)[0].replace(', ',',')
    date = date_scrape.split(',')[0]
    time = date_scrape.split(',')[1]

    # Get summary
    # Regular expression pattern
    pattern_summary = re.compile(r'\d[^\s]+')

    for job_elem in soup.find_all('div',class_='covid__box'):
        # Each job_elem is a new BeautifulSoup object.
        terkonfirmasi_elem = job_elem.find('div',class_='covid__box2 -cases')
        dirawat_elem = job_elem.find('div',class_='covid__box2 -odp')
        meninggal_elem = job_elem.find('div',class_='covid__box2 -gone')
        sembuh_elem = job_elem.find('div',class_='covid__box2 -health')
        # Daily update
        a = pattern_summary.findall(terkonfirmasi_elem.text)[0].replace(',','')
        b = pattern_summary.findall(dirawat_elem.text)[0].replace(',','')
        c = pattern_summary.findall(meninggal_elem.text)[0].replace(',','')
        d = pattern_summary.findall(sembuh_elem.text)[0].replace(',','')
        daily_update = ','.join([date,time,a,b,c,d])

    with open(dir_path+'/'+'Datasets/summary_covid19.txt','r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        if last_line.split(',')[0] == daily_update.split(',')[0]:
            print('----- Summary Data -----')
            print('The data has not been updated yet!')
            print('Last update:',re.findall(r'^(.+?),',last_line)[0])
        else:
            with open(dir_path+'/'+'Datasets/summary_covid19.txt','a+') as ff:
                ff.write('\n{}'.format(daily_update))
                print('----- Summary Data -----')
                print('The data has been updated successfully!')
                print('Up to date data:', re.findall(r'^(.+?),',daily_update)[0])
                ff.close()

    # Get summary - provinsi
    # Regular expression pattern
    pattern_prov = re.compile(r'\d+')
    provinsi = []
    terkonfirmasi_prov = []
    meninggal_prov = []
    sembuh_prov = []

    for elem in soup.find_all('div',class_='covid__row'):
        provinsi_elem = elem.find('div',class_='covid__prov')
        terkonfirmasi_elem = elem.find('span',class_='-odp')
        meninggal_elem = elem.find('span',class_='-gone')
        sembuh_elem = elem.find('span',class_='-health')
        # Append to list    
        provinsi.append(provinsi_elem.text)
        terkonfirmasi_prov.append(pattern_prov.findall(terkonfirmasi_elem.text)[0])
        meninggal_prov.append(pattern_prov.findall(meninggal_elem.text)[0])
        sembuh_prov.append(pattern_prov.findall(sembuh_elem.text)[0])

    # Create dataframe
    dic_data = {'date':[date]*len(provinsi),'time':[time]*len(provinsi),'provinsi':provinsi,
                'terkonfirmasi':terkonfirmasi_prov,'meninggal':meninggal_prov,'sembuh':sembuh_prov}
    df = pd.DataFrame(data=dic_data)

    with open(dir_path+'/'+'Datasets/daily_update_covid.csv','r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        if re.findall(r'^(.+?),',last_line)[0] == df['date'].unique().tolist()[0]:
            print('----- Provinces Data -----')
            print('The data has not been updated yet!')
            print('Last update:',re.findall(r'^(.+?),',last_line)[0])
        else:
            with open(dir_path+'/'+'Datasets/daily_update_covid.csv','a') as ff:
                df.to_csv(ff,header=False,index=False)
                print('----- Provinces Data -----')
                print('The data has been updated successfully!')
                print('Up to date data:', df['date'].unique().tolist()[0])
                print(df.head())
                ff.close()
    # Timing
    print('Program is done in', datetime.now() - startTime,'\n')
