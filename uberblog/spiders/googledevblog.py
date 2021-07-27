import scrapy
from scrapy.loader import ItemLoader

from uberblog.items import UberblogItem


class GoogleDevBlogSpider(scrapy.Spider):
    name = 'googledevblogspider'
    allowed_domains = ['googleblog.com']
    start_urls = ['https://developers.googleblog.com/']
    custom_settings = {'ROBOTSTXT_OBEY': False}

    def parse(self, response, **kwargs):
        for title_selector in response.css('.title > a'):  # [a:first , a:second]
            title_item = ItemLoader(item=UberblogItem(), selector=title_selector)
            title_item.add_css('title', '::text')
            yield title_item.load_item()

        for next_page in response.css('a.blog-pager-older-link'):  # [a:first]
            yield response.follow(next_page, self.parse)
