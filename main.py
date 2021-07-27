from scrapy import cmdline

cmdline.execute("scrapy crawl microsoftblogspider -o output/microsoftblogspider.csv".split())
