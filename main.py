from scrapy import cmdline

cmdline.execute("scrapy crawl googledevblogspider -o output/googledevblogspider.csv".split())
