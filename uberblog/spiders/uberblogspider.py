import scrapy


class UberBlogSpider(scrapy.Spider):
    name = 'uberblogspider'
    allowed_domains = ['https://www.uber.com/en-AU/blog/']
    start_urls = ['http://https://www.uber.com/en-AU/blog//']

    def parse(self, response, **kwargs):
        for title in response.css('._FeedCardMeta_feed-title_2fL'):
            yield {'title': title.css('::text').get()}

        for next_page in response.css('.more-stories'):
            yield response.follow(next_page, self.parse)
