import scrapy


class ApaBlogSpider(scrapy.Spider):
    name = 'apablogspider'
    allowed_domains = ['https://blog.apastyle.org/apastyle/website/']
    start_urls = ['https://blog.apastyle.org/apastyle/website/']

    def parse(self, response, **kwargs):
        for title in response.css('.entry-header'):
            yield {'title': title.css('a::text').get()}

        for next_page in response.css('.pager-right > a'):
            yield response.follow(next_page, self.parse)
