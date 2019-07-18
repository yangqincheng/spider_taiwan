# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from taiwanselect.items import TaiwanselectItem

class SelectSpider(CrawlSpider):
    name = 'taiwan'
    allowed_domains = ['news.tvbs.com.tw']
#    url = "https://www.nownews.com/contentsearch/?cx=009096219251786212246%3Akfgmzw7ve3g&cof=FORID%3A11&ie=UTF-8&q=总统大选&sa=搜尋"
   # url='https://www.nownews.com/cat/2020-2/'
    url="https://news.tvbs.com.tw/pack/packdetail/183/"
    offset = 1
    start_urls = [url+str(offset)]
    rules = (
#a=response.xpath('//div[@class="content"]/div[@class="padding20_mo"]/div[@class="pack_list_div"]/div')
        Rule(LinkExtractor(restrict_xpaths='//div[@class="content"]/div[@class="padding20_mo"]/div[@class="pack_list_div"]/div'),

             callback='parse_item', follow=True,),
    )
    def parse_item(self, response):
        item = TaiwanselectItem()
        item['title']=response.xpath('//div[@class="title margin_b20"]/h1[@class="margin_b20"]/text()').extract()
        item['time']=response.xpath('//div[@class="title margin_b20"]/div[@class="icon_time time leftBox2"]/text()').extract()
        item['content']=response.xpath('//*[@id="news_detail_div"]/text()').extract()
        yield item
        if self.offset < 445:
            self.offset += 1

        # 每次处理完一页的数据之后，重新发送下一页页面请求
        # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset)+"/", callback=self.parse)


