import scrapy
from scrapy.loader import ItemLoader

from uberblog.items import UberblogItem


class LinkedInBlogSpider(scrapy.Spider):
    name = 'linkedinblogspider'
    allowed_domains = ['blog.linkedin.com']
    start_urls = ['https://blog.linkedin.com/']

    def parse(self, response, **kwargs):
        for title_selector in response.css('.heading > a'):  # [h2:first , h2:second]
            title_item = ItemLoader(item=UberblogItem(), selector=title_selector)
            title_item.add_css('title', '::text')
            yield title_item.load_item()

        for next_page in response.css('a.pagination-link'):  # [a:first]
            yield response.follow(next_page, self.parse)
