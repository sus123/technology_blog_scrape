import scrapy
from scrapy.loader import ItemLoader

from uberblog.items import UberblogItem


class AmazonDevBlogSpider(scrapy.Spider):
    name = 'amazondevblogspider'
    allowed_domains = ['developer.amazon.com']
    start_urls = ['https://developer.amazon.com/blogs']

    def parse(self, response, **kwargs):
        for title_selector in response.css('.entryTitle > a'):  # [a:first , a:second]
            title_item = ItemLoader(item=UberblogItem(), selector=title_selector)
            title_item.add_css('title', '::text')
            yield title_item.load_item()

        for next_page in response.css('a[href^="/blogs/home/?page="]'):  # [a:first]
            yield response.follow(next_page, self.parse)
