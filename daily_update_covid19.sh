#!/bin/bash

# Directory
dir_covid=$(pwd)
current_date=$(date +%Y-%m-%d)
# Run the python program
cd $dir_covid && /usr/bin/python3 'Web Scraping Covid-19 Kompas News.py' >> test.out

# Sleep 5 seconds
sleep 5

# Git add commit push
git add .
git commit ${dir_covid}/test.out -m "Update monitoring data $current_date"
git commit ${dir_covid}/Datasets/summary_covid19.txt -m "Update summary data $current_date"
git commit ${dir_covid}/Datasets/daily_update_covid.csv -m "Update provinces data $current_date"
git push origin master
