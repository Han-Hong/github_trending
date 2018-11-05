# -*- coding: utf-8 -*-
import scrapy

from github_trending.items import GithubTrendingItem


class TrendingSpider(scrapy.Spider):
    name = 'trending'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/trending']

    def parse(self, response):
        repo_list = response.xpath('//ol[@class="repo-list"]/li')
        for each_item in repo_list:
            try:
                item = GithubTrendingItem()
                author = each_item.xpath('./div/h3/a/span[@class="text-normal"]/text()').extract_first().replace('/','').strip()
                projectName = each_item.xpath('./div/h3/a/text()').extract()[1].replace('\n','')
                language = each_item.xpath("./div[@class='f6 text-gray mt-2']/span[@class='d-inline-block mr-3'][1]/span[2]/text()").extract_first().replace('\n','').strip()
                intro = each_item.xpath("./div[@class='py-1']/p[@class='col-9 d-inline-block text-gray m-0 pr-4']/text()").extract_first().replace('\n','').strip()
                link = each_item.xpath('./div/h3/a/@href').extract()[0]

                item['author'] = author
                item['projectName'] = projectName
                item['language'] = language
                item['intro'] = intro
                item['link'] = "https://github.com{}".format(link)
                yield item
            except Exception:
                continue


