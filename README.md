# Sites Monitoring Utility

This module checks urls in file with links wich you prefer

# File example
Your file must contain only urls without commas, just followed 1 by 1.
Each Url must be at new line

for example:
```bash
https://vk.com/
https://devman.org/
https://ya.ru/
```

# Usage example
put your urls to links.txt (just line by line)

```bash
$ python3 check_sites_health.py --filepath path_to_file_with_urls

--------------------------------------------------
Информация по сайту - https://vk.com/

Сайт отвечает по на запрос статусом: 200
Сайт проплачен более чем на месяц
--------------------------------------------------
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
