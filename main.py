from scrapy import cmdline

cmdline.execute("scrapy crawl gitblogspider -o output/gitblogspider.csv".split())
