#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import scrapy


#解析多页面
class CnBlogScrapy(scrapy.Spider):
    name = 'cnblog'
    start_urls = ['https://www.cnblogs.com/pick/#p{}'.format(str(i)) for i in range(1, 21)]

    def parse(self, response):
        for blog in response.xpath('//div[@class="post_item"]'):
            title = blog.xpath('div[2]/h3/a/text()').extract_first()
            nums = blog.xpath('div[@class="digg"]/div/span/text()').extract_first()
            # info = julyedu_class.xpath('a/p[1]').extract_first()
            print('{}:{}'.format(title, nums))
            # print title.encode('utf-8')
            yield {
                'title': title,
                'nums' : nums
            }