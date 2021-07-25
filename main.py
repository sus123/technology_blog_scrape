from scrapy import cmdline

cmdline.execute("scrapy crawl whatsappblogspider -o output/whatsappblogspider.csv".split())
