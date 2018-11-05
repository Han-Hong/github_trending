# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GithubTrendingPipeline(object):
    def process_item(self, item, spider):
        with open('github_trending.txt', 'a') as f:
            str = '作者：{0},项目：{1},简介：{2},语言：{3},链接：{4}\n'.format(
                item['author'],
                item['projectName'],
                item['intro'],
                item['language'],
                item['link']
            )
            f.write(str)
