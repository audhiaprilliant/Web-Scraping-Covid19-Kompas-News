#!/bin/bash
date_run=$(date +%c)
# Directory
dir_covid=/home/audhi/github/Web-Scraping-Covid19-Kompas-News
# Run the python program
cd $dir_covid && /usr/bin/python3 'Web Scraping Covid-19 Kompas News.py' >> test.out

# Sleep 5 seconds
sleep 5
current_date=$(tail -n 1 ${dir_covid}/Datasets/summary_covid19.txt | cut -d, -f1)
# Git add commit change
echo $date_run
cd $dir_covid && /usr/bin/git add --all &&
/usr/bin/git commit ${dir_covid}/test.out -m Update monitoring data $current_date" &&
/usr/bin/git commit ${dir_covid}/Datasets/summary_covid19.txt -m Update summary data $current_date" &&
/usr/bin/git commit ${dir_covid}/Datasets/daily_update_covid.csv -m Update provinces data $current_date"
# Git commit
cd $dir_covid && /usr/bin/git push origin master
echo ""
