import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor



class ArticleItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    size = scrapy.Field()

class NHLSpider(CrawlSpider):

    name = 'nhl'
    allowed_domains = ['nhl.com']
    start_urls = ['http://www.nhl.com/ice/newsindex.htm']
    rules = [Rule(LinkExtractor(allow=['/news.htm?id=\d+']), 'parse_article')]

    def parse_article(self, response):
        article = ArticleItem()
        article['url'] = response.url
        article['name'] = response.xpath("//h1/text()").extract()
        return article

test = NHLSpider()
hope = test.parse_article
print(hope)
