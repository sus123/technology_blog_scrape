import scrapy
from scrapy.loader import ItemLoader

from uberblog.items import UberblogItem


class UberBlogSpider(scrapy.Spider):
    name = 'uberblogspider'
    allowed_domains = ['www.uber.com']
    start_urls = ['https://www.uber.com/en-AU/blog/']

    def parse(self, response, **kwargs):
        for title_selector in response.css('._FeedCardMeta_feed-title_2fL'):  # [h5:first, h5:second]
            title_item = ItemLoader(item=UberblogItem(), selector=title_selector)
            title_item.add_css('title', '::text')
            yield title_item.load_item()

        for next_page in response.css("a.more-stories"):    #[a:first]
            yield response.follow(next_page, self.parse)
