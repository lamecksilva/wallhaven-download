## Wallhaven Download

This is the python version of my older script to random download an wallpaper from Wallhaven and set as Background Wallpaper.

> If you use windows, linux, change the function `set_wallpaper` in `wallpaper_changer.py`

### Cron

To run that script automatically with some frequency, use crontab. 

```bash
$ crontab -e
```

And i add the following line

`* * * * * /opt/homebrew/bin/python3 /Users/$USER/Projects/wallhaven-download/wallpaper_changer.py`

> Note the `* * * * *` means: Run that command every minute, every hour, every day, every month, every year
Customize your frequency changing that. I recommend use https://crontab.guru/ to better understand of cron params
