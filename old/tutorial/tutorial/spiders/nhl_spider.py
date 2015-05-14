from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
#from tutorial.items import TorrentItem
from tutorial.items import ArticleItem

class NHLSpider(CrawlSpider):
 
    name = 'nhl'
    allowed_domains = ['nhl.com']
    #allowed_domains = ['tsn.ca']
    start_urls = ['http://www.nhl.com/ice/newsindex.htm', 'http://www.nhl.com/ice/newsindex.htm?pg=209']
    #start_urls = ['http://www.tsn.ca']
    rules = [Rule(LinkExtractor(allow=['news']), 'parse_article')]
    #rules = [Rule(LinkExtractor(allow=['tsn']), 'parse_article')]
 
    def parse_article(self, response):
        article = ArticleItem()
        article['url'] = response.url
        article['name'] = response.xpath("//h1/text()").extract()
        article['text'] = response.xpath("//div[@class='articleText']/text()").extract()
        return article
    
# class MininovaSpider(CrawlSpider):
# 
#     name = 'mininova'
#     allowed_domains = ['mininova.org']
#     start_urls = ['http://www.mininova.org/today']
#     rules = [Rule(LinkExtractor(allow=['/tor/\d+']), 'parse_torrent')]
# 
#     def parse_torrent(self, response):
#         torrent = TorrentItem()
#         torrent['url'] = response.url
#         torrent['name'] = response.xpath("//h1/text()").extract()
#         torrent['description'] = response.xpath("//div[@id='description']").extract()
#         torrent['size'] = response.xpath("//div[@id='info-left']/p[2]/text()[2]").extract()
#         return torrent
