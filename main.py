from scrapy import cmdline

cmdline.execute("scrapy crawl apablogspider -o output/apablogspider.csv".split())
