# [My]Twitter screaper

![](/img/twitter.png)

# Idea

![](/img/linode.png)
Deploy our own script to crawl tweets from Twitter in a cloud provider (Linode) to collect .csv later used for sentiment analisys.

Note: In the photo you can see Linode's dashboard showing data about the execution of our crawler in a 24h timespan.

# Getting started

It is possible to run this project inside a container or as a simple script.

## 1) Preferred way
- Get a Bearer Token from [Twitter Developer Portal](https://developer.twitter.com/)
- Set the env var `TWITTER_BEARER` to equal the obtained token
- Run run.sh to generate a cronjob which, every odd hour, runs the crawler
- Note that the number of crawled tweets depends on the env var `TOT_TWEET`.

## 2) Container

Get a Bearer Token from [Twitter Developer Portal](https://developer.twitter.com/)
**Run Through image**
- Modify `Dockerfile` setting `TWITTER_BEARER` to equal the obtained token
- Build image: ```docker build -v data:data/app twitter-screaper .```
- Run image: ```docker run -v ${PWD}/data:/app/data twitter-screaper```

**Run Through docker-compose**
- Modify `docker-compose.yml` setting `TWITTER_BEARER` to equal the obtained token
- Run image: ```docker-compose run my-screaper```

## Analyse the data

Once data have been crawled, before analysing it, you can use:
- `scripts/unpack_downloaded_data.py` to move the .csv that have been placed in different directories following the crawling timestamp, to the same directory: "destination".
- `scripts/create_compounded_csv.py` to create a dataset from multiple .csv placed in the same directory "destination".

## Requirements

To run you'll need python 3.7 and the following libraries:
- [Tweepy](https://www.tweepy.org) - An easy-to-use Python library for accessing the Twitter API..
- [Twitter API v2 token](https://developer.twitter.com/en/docs/twitter-api) - The Twitter API enables programmatic access to Twitter in unique and advanced ways. 
- [Pandas](https://pandas.pydata.org): pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.


# Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contribution you make is **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/yourFeature`)
3. Commit your Changes (`git commit -m 'your feature'`)
4. Push to the Branch (`git push origin feature/yourFeature`)
5. Open a Pull Request

# Authors

* **Simone Patuelli** - [@simo955](https://github.com/simo955)
* **Giacomo Masi** - [@GiacomoMasi](https://github.com/GiacomoMasi)

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details