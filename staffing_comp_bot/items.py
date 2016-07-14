# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StaffingCompBotItem(scrapy.Item):
    name = Field()
    address = Field()
    telephone = Field()
    fax = Field()
    email = Field()
    website = Field()

