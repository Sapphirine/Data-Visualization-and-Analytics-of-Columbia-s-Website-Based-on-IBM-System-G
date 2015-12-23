import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from columbia.items import ColumbiaItem
import urlparse


class Myspider(CrawlSpider):
    name = 'columbia'
    allowed_domains = ['columbia.edu']
    start_urls = ['http://www.columbia.edu/']
    rules = (
        Rule(
            LinkExtractor(
                deny=('.*login.*', '.*archivesportal.*', '.*search.*', '.*label.*', '.*archives.*', '.*clio.*',
                      'https://wikis.cuit.columbia.edu/confluence/label.*', '.*manilaclam.*', '.*oralhistoryportal.*'),
                deny_domains=(
                    'search.columbia.edu', 'cupola.columbia.edu'),
                restrict_xpaths=('//a[contains(@href, "http")]'))
        ),
        Rule(
            LinkExtractor(allow=('',), deny_domains=('search.columbia.edu',)),
            callback='parse_item'
        )

    )

    def parse_start_url(self, response):
        return self.parse_item(response)

    def parse_item(self, response):
        print('Hi, this is an item page! %s', response.url)
        for sel in response.xpath('//a[contains(@href, "http")]'):
            item = ColumbiaItem()
            item['url'] = response.url
            item['title'] = response.xpath('//head/title/text()').extract()
            item['child_url'] = urlparse.urljoin(response.url, sel.xpath('@href').extract()[0])
            request = scrapy.Request(item['child_url'],
                                     callback=self.parse_items_2, dont_filter=True)
            request.meta['item'] = item
            yield request

    def parse_items_2(self, response):
        item = response.meta['item']
        item['child_title'] = response.xpath('//head/title/text()').extract()
        yield item
