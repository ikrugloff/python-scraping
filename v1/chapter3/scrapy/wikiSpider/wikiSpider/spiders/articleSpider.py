from scrapy.spiders import CrawlSpider, Rule
from wikiSpider.items import Article
from scrapy.linkextractors import LinkExtractor


class ArticleSpider(CrawlSpider):
    """p.67"""
    name = "article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
    rules = [
        Rule(LinkExtractor(allow=('(/wiki/)((?!:).)*$'),), callback="parse_item", follow=True)
    ]

    def parse_item(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is: "+title)
        item['title'] = title
        return item


# # from scrapy.selector import Selector
# from scrapy import Spider
#
#
# class ArticleSpider(Spider):
#     """p.66"""
#     name = "article"
#     allowed_domains = ["en.wikipedia.org"]
#     start_urls = ["http://en.wikipedia.org/wiki/Main_Page",
#                   "http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
#
#     def parse(self, response):
#         item = Article()
#         title = response.xpath('//h1/text()')[0].extract()
#         print("Title is: " + title)
#         item['title'] = title
#         return item
