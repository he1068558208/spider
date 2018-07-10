import scrapy
from scrapy import Request

from sina import items


class MysinaSpider(scrapy.Spider):
    name = 'mysina'
    allowed_domains = ['sina.com.cn']
    start_urls = 'http://roll.news.sina.com.cn/news/gnxw/gdxw1/index_{page}.shtml'
    def start_requests(self):
        for i in range(1,6):
            yield Request(self.start_urls.format(page=i))

    def parse(self, response):
        item = items.SinaItem()
        newsList = response.xpath('//*[@id="Main"]/div[3]/ul/li')
        for news in newsList:
            newsTitle = news.xpath("./a/text()").extract()
            newsUrl = news.xpath("./a/@href").extract()
            newsTime = news.xpath("./span/text()").extract()
            item['newsTitle'] = newsTitle
            item['newsUrl'] = newsUrl
            item['newsTime'] = newsTime

            # 发起请求
            yield item
