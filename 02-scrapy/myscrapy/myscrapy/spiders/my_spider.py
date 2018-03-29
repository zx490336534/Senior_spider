import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first_spider'
    start_url = ['https://www.baidu.com']

    # def start_requests(self):
    #     pass

    def parse(self, response):
        pass

class SecondSpider(scrapy.Spider):
    name = 'second_spider'