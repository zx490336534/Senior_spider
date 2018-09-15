# -*- coding: utf-8 -*-
import scrapy


class Renren1Spider(scrapy.Spider):
    name = 'renren1'
    allowed_domains = ['renren.com']
    start_urls = ['http://zhibo.renren.com/top']
    cookies = {'anonymid':'jfqsk1uc-famihu',
            'depovince':'ZJ',
            '_r01_':'1',
            'JSESSIONID':'abcht5IfFB-mVb0MtqLkw',
            'ick_login':'a774ae54-e47f-4303-bd8f-1d38419e069f',
        'first_login_flag':'1' ,'ln_uact':'15168230644',
        'ln_hurl':'http://hdn.xnimg.cn/photos/hdn321/20131229/1845/h_main_008K_52920001c7f1113e.jpg',
        'loginfrom':'syshome' ,
        'ch_id':'10016',
        'wp_fold':'0' ,
        'wp':'0',
    'jebecookies':'98db98f7-a6e5-48aa-8d79-daf35740eddc|||||',
    '_de':'9D0F4C3FC3E49879570A84C70CA844DE',
    'p':'7fa69f107eadd2ffc6c3b1b447c5c67e1',
    't':'abff6d06c284fb9d79064ca9cc689ea21',
    'societyguester':'abff6d06c284fb9d79064ca9cc689ea21',
                    'id':'576586461',
                         'xnsid':'5aba5a77'}

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url=url,cookies=self.cookies,callback=self.parse)

    def parse(self, response):
        print(response.body.decode())
