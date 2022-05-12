sudo crontab -l > cron_bkp
sudo echo "1 1-23/2 * * * nohup python3 app.py & >/dev/null 2>&1" >> cron_bkp
sudo crontab cron_bkp
sudo rm cron_bkp