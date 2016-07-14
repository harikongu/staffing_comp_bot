# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from staffing_comp_bot.items import StaffingCompBotItem


class ApscoSpider(CrawlSpider):
    handle_httpstatus_list = [302]
    name = "apsco"
    allowed_domains = ["apsco.org"]
    start_urls = (
        'http://www.apsco.org/directory/Advanced.aspx?streetAddress=london&country=234&page_num=1',
    )

    rules = (
        Rule(
            LinkExtractor(
                allow=(),
                restrict_xpaths=('//a[contains(., "Next")]')
            ),
            callback='parse_item', follow=True
        ),
    )

    def parse_item(self, response):
        sel = Selector(response)
        companies = sel.xpath('//div[@class="directory-search-item"]')
        items = []

        for site in companies:
            item = StaffingCompBotItem()
            item['name'] = site.xpath(
                'span[@class="directory-search-item-title"]/a/text()').extract()
            item['address'] = site.xpath(
                'span[@class="directory-search-item-address"]/text()').extract()
            item['telephone'] = site.xpath(
                'span[@class="directory-search-item-telephone"]/text()').extract()
            item['fax'] = site.xpath(
                'span[@class="directory-search-item-fax"]/text()').extract()
            item['email'] = site.xpath(
                'span[@class="directory-search-item-email"]/a/@href').extract()
            item['website'] = site.xpath(
                'span[@class="directory-search-item-website"]/a/@href').extract()
            items.append(item)

        return items
