#!/usr/bin/env python
# -*- coding: utf8 -*-

import scrapy


#解析多页面,通过下一页连接
class JokeScrapy(scrapy.Spider):
    name = 'joke'
    start_urls = ['http://quotes.toscrape.com/tag/humor/']

    def parse(self, response):
        for joke in response.xpath('//div[@class="quote"]'):
            title = joke.xpath('span[1]/text()').extract_first()
            yield {
                'title': title
            }

        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)