# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from reddit.items import RedditItem #The item class that we made in items.py

class MildSpider(CrawlSpider):
    name = "mild"
    allowed_domains = ["www.reddit.com"]
    start_urls = ['http://www.reddit.com/r/mildlyinteresting/']
    rules = [Rule(LinkExtractor(allow=("/\?count=\d*&after=\w*")),
    callback='parse_item',
    follow=True),]

    def parse_item(self, response):

            item = RedditItem()
            item['title'] = response.xpath('//p[@class="title"]/a/text()').extract()[0]
            item['image_url'] = response.xpath('//p[@class="title"]/a/@href').extract()[0]
            yield item