# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XimalayaItem(scrapy.Item):
    # define the fields for your item here like:
    # 一级标题
    title = scrapy.Field()
    # 二级标题
    intro_1 = scrapy.Field()
    # 详情
    intro_2 = scrapy.Field()
    # 封面图
    img = scrapy.Field()
    pass