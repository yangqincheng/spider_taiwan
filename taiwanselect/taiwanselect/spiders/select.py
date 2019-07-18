# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from taiwanselect.items import TaiwanselectItem

#多维新闻
# class SelectSpider(CrawlSpider):
#     name = 'select'
#     allowed_domains = ['tag.dwnews.com','news.dwnews.com']
#
#    # start_urls = ['http://tag.dwnews.com/2020台灣總統大選.html']
#     start_urls = ['http://tag.dwnews.com/2020%E5%8F%B0%E7%81%A3%E7%B8%BD%E7%B5%B1%E5%A4%A7%E9%81%B8.html']
#     #response.xpath('//*[@id="aticleListUlId"]/li/div/div[2]/h3/a/@href').extract()
#     #allow='http://news.dwnews.com/taiwan/news\/.*\.html',
#     domain = ['news.dwnews.com']
#     rules = (
#         Rule(LinkExtractor(allow_domains=domain,allow='com/taiwan/news\/.*\.html',restrict_xpaths='//*[@id="aticleListUlId"]/li'),
#              callback='parse_item', follow=True,),
#     )
#     def parse_item(self, response):
#        item=TaiwanselectItem()
#
#        item['title']=response.xpath('/html/body/div[7]/div[1]/div[1]/div[2]/div[2]/div[1]/h1/text()').extract()
#        yield item
#=====================================三立======
# class SelectSpider(CrawlSpider):
#     name = 'select'
#     allowed_domains = ['www.setn.com','www.setn.com']
#     url = "https://www.setn.com/Klist.aspx?TagID=11857&p="
#
#     offset = 1
#     start_urls = [url + str(offset)]
#     rules = (
#         Rule(LinkExtractor(restrict_xpaths='//*[@id="contFix"]/div/div[2]/div/div[@class="col-lg-4 col-sm-6 animate-box"]'),
#              callback='parse_item', follow=True,),
#         Rule(LinkExtractor(restrict_xpaths='//*[@id="contFix"]/div/div[2]/div/div[32]/div/ul/li[8]/a[]'))
#     )
#     def parse_item(self, response):
#        item=TaiwanselectItem()
#        item['title']=response.xpath('//*[@id="contFix"]/div/div[2]/h1/text()').extract()
#        if response.xpath('//*[@id="Content1"]/p/text()'):
#            item['content']=response.xpath('//*[@id="Content1"]/p/text()').extract()
#        else:
#            item['content'] = response.xpath('//*[@id="Content1"]/div/text()').extract()
#        yield item
#        if self.offset < 16:
#             self.offset += 1
#        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
#================================
class SelectSpider(CrawlSpider):
    name = 'select'
    allowed_domains = ['www.nownews.com']
#    url = "https://www.nownews.com/contentsearch/?cx=009096219251786212246%3Akfgmzw7ve3g&cof=FORID%3A11&ie=UTF-8&q=总统大选&sa=搜尋"
    url='https://www.nownews.com/cat/2020-2/'
    offset = 1
    start_urls = [url+'page/'+str(offset)+"/"]
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//*[@id="td-outer-wrap"]/div[6]/div/div/div/div/div/div'),
             callback='parse_item', follow=True,),
    )
    def parse_item(self, response):
        item = TaiwanselectItem()

        item['title']=response.xpath('//article/div[1]/div/div/header/h1/text()').extract()
        if response.xpath('//*[@id="Content1"]/p/text()'):
            item['content']=response.xpath('//*[@id="innity-in-post"]/p/text()').extract()
        item['time'] = response.xpath('//*[@id="article"]/div[1]/div/div/header/div/span/time/text()')
        yield item
        if self.offset < 16:
            self.offset += 1
        yield scrapy.Request(self.url + str(self.offset)+"/", callback=self.parse)
# ===========================tvbs
# class SelectSpider(CrawlSpider):
#     name = 'select'
#     allowed_domains = ['news.tvbs.com.tw']
# #    url = "https://www.nownews.com/contentsearch/?cx=009096219251786212246%3Akfgmzw7ve3g&cof=FORID%3A11&ie=UTF-8&q=总统大选&sa=搜尋"
#    # url='https://www.nownews.com/cat/2020-2/'
#     #offset = 1
#     start_urls = ['https://news.tvbs.com.tw/eventsite/2020elections#golive']
#     rules = (
#                # a=response.xpath('//*[@id="block_pc"]/li//a/@href')
#         Rule(LinkExtractor(restrict_xpaths='//*[@id="block_pc"]/li'),
#              callback='parse_item', follow=True,),
#     )
#     def parse_item(self, response):
#         item = TaiwanselectItem()
#         item['title']=response.xpath('//div[@class="title margin_b20"]/h1[@class="margin_b20"]/text()').extract()
#         item['time']=response.xpath('//*[@class="icon_item time leftBox2"]/text()').extract()
#         item['content']=response.xpath('//*[@id="news_detail_div"]/text()').extract()
#         yield  item
