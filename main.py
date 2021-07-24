from scrapy import cmdline

cmdline.execute("scrapy crawl uberblogspider -o output/uberblogspider.csv".split())
