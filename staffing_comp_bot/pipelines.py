# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class StaffingCompBotPipeline(object):
    def process_item(self, item, spider):
        if item['telephone']:
            item['telephone'] = [item['telephone'][0].replace('Telephone:', '')]
        if item['fax']:
            item['fax'] = [item['fax'][0].replace('Fax:', '')]
        if item['email']:
            item['email'] = [item['email'][0].replace('mailto:', '')]
        return item
