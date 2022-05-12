# [My]Twitter screaper

![](/img/twitter.png)

# Idea
Python script for connecting to Twitter stream, gather tweets that match a particular keyword, hashtag or mention and save them on a CSV file.

# Getting started
It is possible to run this project inside a container or as a simple script.

## 1) Container
Get a Bearer Token from [Twitter Developer Portal](https://developer.twitter.com/)
**Run Through image**
- Modify `Dockerfile` setting `TWITTER_BEARER` to equal the obtained token
- Build image: ```docker build -v data:data/app my-screaper .```
- Run image: ```docker run -v ${PWD}/data:/app/data simopatu/my-screaper```

**Run Through docker-compose**
- Modify `docker-compose.yml` setting `TWITTER_BEARER` to equal the obtained token
- Run image: ```docker-compose run my-screaper```

## 2) Shell script
- Get a Bearer Token from [Twitter Developer Portal](https://developer.twitter.com/)
- Modify `app.py` line 7 setting token to equal the obtained token
- Run run.sh to generate a cronjob which runs every odd hour

## Requirements

To run this script, you'll need python 3.7 and the following libraries:
- [Tweepy](https://www.tweepy.org) - An easy-to-use Python library for accessing the Twitter API..
- [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api) - The Twitter API enables programmatic access to Twitter in unique and advanced ways. 
# Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/yourFeature`)
3. Commit your Changes (`git commit -m 'Add some yourFeature'`)
4. Push to the Branch (`git push origin feature/yourFeature`)
5. Open a Pull Request

# Authors

* **Simone Patuelli** - [@simo955](https://github.com/simo955)
* **Giacomo Masi** - [@GiacomoMasi](https://github.com/GiacomoMasi)

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details