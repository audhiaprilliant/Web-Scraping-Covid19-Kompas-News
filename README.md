## Web Scraping Covid19 Kompas News Using BeautifulSoup Python3
### Indonesia

Cite the data: http://datasets.coronawhy.org/dataset.xhtml?persistentId=doi:10.5072/FK2/FMB3QB

### Prerequisites
1. Python 3.x, of course
2. Good internet connection is recommended
3. Several python's modules
   - **pandas** for data manipulation
   - **bs4** is a Python library for pulling data out of HTML and XML files
   - **os** provides functions for interacting with the operating system
   - **re** provides regular expression matching operations similar to those found in Perl
   - **datetime** supplies classes for manipulating dates and times
   - **requests** allows you to send HTTP/1.1 requests extremely easily

### Steps
The program is easy to run by following steps:
1. Clone this repo
2. Open your terminal
3. Download the module dependencies by typing `pip install -r requirements.txt`
4. Type `python3 'Web Scraping Covid-19 Kompas News.py'`
5. Finally, the data will be in your directory

### Output
Two possibilities that we have:
1. Our program captures the up to date data. So the output must be like this one
<img src='img/Screenshot from 2020-05-10 18-35-28.png' alt='uptodate' class='center'>
2. Unluckily, our program is too early running
<img src='img/Screenshot from 2020-05-10 18-36-33.png' alt='not-uptodate' class='center'>

### Automation
We could also automate the program by using crobtab scheduler in Linux. Follow steps below to configure the crontab:
1. Type `crontab -e` in your terminal to add a new crobjob
2. Specify the scheduler. First, I suggest you to look at [**here**](https://crontab.guru/) for the detail of scheduler and also the examples
3. Open new terminal and find a directory of our **Python3** by typing `whereis python3`. It must be saved in `/usr/bin/python3` directory
4. Back to the first terminal and type `45 16 * * * cd /your path of web scraping script/ && /usr/bin/python3 'Web Scraping Covid-19 Kompas News.py' >> test.out`
   If you feel a little bit confuse with above command, let me tell you what I know
   - `45 16 * * *` is our schedule. The crontab uses our local time machine instead of UTC. So our program is going to be running at 16.45 everyday for every month
   - `/your path of web scraping script/` must be the directory where you keep the python script. In my case, it is in **'home/covid19 data'**
   - `/usr/bin/python3` is the directory of Python3 interpreter
   - `>> test.out` implies that the file `test.out`would be created and as logs for the outputs
5. Finally, save the crontab configuration

