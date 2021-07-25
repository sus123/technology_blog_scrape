import scrapy
from scrapy.loader import ItemLoader

from uberblog.items import UberblogItem


class WhatsappBlogSpider(scrapy.Spider):
    name = 'whatsappblogspider'
    allowed_domains = ['blog.whatsapp.com']
    start_urls = ['https://blog.whatsapp.com/?lang=en']

    def parse(self, response, **kwargs):
        for title_selector in response.css('._2yzk > a'):  # [div:first , div:second]
            title_item = ItemLoader(item=UberblogItem(), selector=title_selector)
            title_item.add_css('title', '::text')
            yield title_item.load_item()

        for next_page in response.css('a._2y_c'):  # [a:first]
            yield response.follow(next_page, self.parse)
