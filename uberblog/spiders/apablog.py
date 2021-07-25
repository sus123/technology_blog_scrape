import scrapy
from itemloaders import ItemLoader

from uberblog.items import ApablogItem


class ApaBlogSpider(scrapy.Spider):
    name = 'apablogspider'
    allowed_domains = ['blog.apastyle.org']
    start_urls = ['https://blog.apastyle.org/apastyle/website/']

    def parse(self, response, **kwargs):
        for title_selector in response.css('.entry-header'):
            title_item = ItemLoader(item=ApablogItem(), selector=title_selector)
            title_item.add_css('title', 'a::text')
            yield title_item.load_item()

        for next_page in response.css('.pager-right > a'):
            yield response.follow(next_page, self.parse)
