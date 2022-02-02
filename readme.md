# Stack Spider

## Description

App allows to scrap StackOverflow website and store questions data from the site at MongoDB database.

## Install

Clone the repo and change directory to the cloned repo:

```bash
git clone https://github.com/hardkoro/stack_spider.git
```

```bash
cd stack_spider
```

Create and activate virtual environment:

```bash
python3 -m venv venv
```

```bash
. venv/bin/activate
```

Install requirements from file requirements.txt:

```bash
pip3 install -r requirements.txt
```

Install local MongoDB database with name stackoverflow and add collection questions there. Run scraper as follows:

```bash
cd stack/
scrapy crawl stack
```
