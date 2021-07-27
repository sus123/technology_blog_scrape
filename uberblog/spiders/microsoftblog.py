import scrapy
from scrapy.loader import ItemLoader

from uberblog.items import UberblogItem


class MicrosoftBlogSpider(scrapy.Spider):
    name = 'microsoftblogspider'
    allowed_domains = ['microsoft.com']
    start_urls = ['https://blogs.microsoft.com/page/2/']

    def parse(self, response, **kwargs):
        for title_selector in response.css('.c-heading-4'):  # [div:first , div:second]
            title_item = ItemLoader(item=UberblogItem(), selector=title_selector)
            title_item.add_css('title', '::text')
            yield title_item.load_item()

        for next_page in response.css('a[aria-label="Next Page"]'):  # [a:first]
            yield response.follow(next_page, self.parse)
