from scrapy import cmdline
'''
    在IDE中进行调用，可以进行Debug
    其中trending为爬虫名称
'''
cmdline.execute("scrapy crawl trending".split())