import scrapy
from scrapy.crawler import CrawlerProcess

class ContentSpider(scrapy.Spider):
    name = 'content'

    def start_requests(self):
        urls = getattr(self, 'start_urls', [])
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Extract the entire HTML body content
        html_content = response.body
        yield {
            'html_content': html_content.decode('utf-8')  # Decoding bytes to a string
        }

def run_spider(url):
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output.json'  # Output file for scraped data
    })
    process.crawl(ContentSpider, start_urls=[url])
    process.start()