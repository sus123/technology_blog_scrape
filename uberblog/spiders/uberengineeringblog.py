import scrapy
from scrapy.loader import ItemLoader

from uberblog.items import UberblogItem


class UberEngineeringBlogSpider(scrapy.Spider):
    name = 'uberengblogspider'
    allowed_domains = ['eng.uber.com']
    start_urls = ['https://eng.uber.com/']

    def parse(self, response, **kwargs):
        for title_selector in response.css('.entry-title >a'):  # [a:first , a:second]
            title_item = ItemLoader(item=UberblogItem(), selector=title_selector)
            title_item.add_css('title', '::text')
            yield title_item.load_item()

        for next_page in response.css('a.page'):  # [a:first]
            yield response.follow(next_page, self.parse)
