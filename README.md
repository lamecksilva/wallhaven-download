<!--toc:start-->

- [Wallhaven Download](#wallhaven-download)
  - [Cron](#cron)
  <!--toc:end-->

## Wallhaven Download

This is the python version of my older script to random download an wallpaper from Wallhaven and set as Background Wallpaper.

> If you use windows, linux, change the function `set_wallpaper` in `wallpaper_changer.py`

### Cron

To run that script automatically with some frequency, use crontab.

```bash
crontab -e
```

> The script `launcher.sh` need the path for the script, so change it before put in cron

And i add the following line

`*/1 * * * * /Users/lamecksantos/Projects/wallpaper_changer/launcher.sh >/tmp/stdout.log 2>/tmp/stderr.log`

> Note the `* * * * *` means: Run that command every minute, every hour, every day, every month, every year
> Customize your frequency changing that. I recommend use <https://crontab.guru/> to better understand of cron params
