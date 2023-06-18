# scrapyrepo

## Overview
A repo for scraping test. Scraping Ximalaya-history topic pages. Using tools: Scrapy & BeautifulSoup4. Use Scrapy to scrape HTML pages & object store, and use BeautifulSoup4 for HTML tags decoding. Data includes: 1. Title 2. Subtitle 3. Introduction 4. Image.

Thanks to the [冬酒暖阳](https://www.lifepoem.cn/archives/scrapy%E5%B0%86%E6%95%B0%E6%8D%AE%E4%BF%9D%E5%AD%98%E4%B8%BA%E6%A0%87%E5%87%86json%E6%A0%BC%E5%BC%8F%E6%96%87%E4%BB%B6%E7%9A%84%E6%96%B9%E6%B3%95) who provided the scrapy object to json, which saved me some time.


爬取喜马拉雅 - 历史类
 
使用的工具：主要包括 scrapy 和 bs4

爬取包括：标题，二级标题，简介内容，图片

感谢 [冬酒暖阳](https://www.lifepoem.cn/archives/scrapy%E5%B0%86%E6%95%B0%E6%8D%AE%E4%BF%9D%E5%AD%98%E4%B8%BA%E6%A0%87%E5%87%86json%E6%A0%BC%E5%BC%8F%E6%96%87%E4%BB%B6%E7%9A%84%E6%96%B9%E6%B3%95) 提供的对象导出至json函数。

## Structure
```commandline
.
│  main.py
│  README.md
│  requirements.txt 
│
├─.idea
│
└─mySpider
    │  data.json            # 储存文件
    │  scrapy.cfg           # scrapy 配置
    │
    └─mySpider
        │  items.py         # 对象结构
        │  middlewares.py
        │  pipelines.py     # 导出设置
        │  settings.py      
        │  __init__.py
        │
        └─spiders
           │  ximalaya.py   # 爬虫
           └─__init__.py
         

```

## Install 

install the dependencies
````commandline
pip install -r requirement.txt
````
run 
```commandline
cd mySpider
scrapy crawl ximalaya
```

Reference:

