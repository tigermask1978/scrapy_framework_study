#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import scrapy


#解析单页面
class JulyeduScrapy(scrapy.Spider):
    name = 'julyedu'
    start_urls = ['https://www.julyedu.com/category/index']

    def parse(self, response):
        for julyedu_class in response.xpath('//div[@class="course_info_box"]'):
            title = julyedu_class.xpath('a/h4/text()').extract_first()
            info = julyedu_class.xpath('a/p[1]').extract_first()
            # print info
            yield {
                'title': title,
                'info' : info
            }

