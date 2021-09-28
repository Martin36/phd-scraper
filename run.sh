#!/bin/sh

eval "$(conda shell.bash hook)"
conda activate phd-scraper
echo "`date -u`" >> /home/martin/cron.log
python /home/martin/phd-scraper/main.py >> /home/martin/cron.log

/bin/echo "cron works" >> /home/martin/cron.log
