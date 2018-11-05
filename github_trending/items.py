# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GithubTrendingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
    projectName = scrapy.Field()
    language = scrapy.Field()
    intro = scrapy.Field()
    link = scrapy.Field()
