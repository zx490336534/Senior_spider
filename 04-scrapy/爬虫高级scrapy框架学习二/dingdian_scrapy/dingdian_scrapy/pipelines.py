# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DingdianScrapyPipeline(object):
    def process_item(self, item, spider):
        with open('dingdian.txt', 'a', encoding='utf-8') as f:
            f.write(item.get('book_name', ''))
            f.write('  |  ')
            f.write(item.get('auth', ''))
            f.write('  |  ')
            f.write(item.get('words', ''))
            f.write('  |  ')
            f.write(item.get('status', ''))
            f.write('  |  ')
            f.write(item.get('last_time', ''))
            f.write('  |  ')
            f.write(item.get('new_chapter', ''))

            f.write('\n')
        return item
