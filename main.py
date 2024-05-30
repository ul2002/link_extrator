import scrapy
from scrapy.crawler import CrawlerProcess
from urllib.parse import urljoin, urlparse
import json
import argparse
import logging
import time


# Configure logging to suppress lower level messages
logging.getLogger('scrapy').setLevel(logging.ERROR)

class LinkSpider(scrapy.Spider):
    name = "link_spider"  # Name of the spider

    def __init__(self, urls, output_format, *args, **kwargs):
        super(LinkSpider, self).__init__(*args, **kwargs)
        self.start_urls = urls  # List of URLs to start scraping from
        self.output_format = output_format  # Output format (stdout or json)
        self.all_links = {}  # Dictionary to store extracted links for JSON output

    def parse(self, response):
        base_url = response.url  # The URL of the current response
        # Extract all href links using CSS selectors
        links = response.css('a::attr(href)').getall()
        # Convert relative links to absolute URLs
        abs_links = [urljoin(base_url, link) for link in links]
        
        if self.output_format == 'stdout':
            # Print each absolute URL if output format is stdout
            for link in abs_links:
                print(link)
        elif self.output_format == 'json':
            # For JSON output, store links by base domain
            base_domain = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(base_url))
            if base_domain not in self.all_links:
                self.all_links[base_domain] = set()
            self.all_links[base_domain].update([urlparse(link).path for link in abs_links])
        
    def close(self, reason):
        # This method is called when the spider is closed
        if self.output_format == 'json':
            # Convert sets to lists for JSON serialization
            for domain in self.all_links:
                self.all_links[domain] = list(self.all_links[domain])
            print(json.dumps(self.all_links, indent=4))

def extract_links(urls, output_format):
    # Create a CrawlerProcess with the default Scrapy settings
    process = CrawlerProcess({
        'LOG_LEVEL': 'ERROR'  # Set log level to ERROR to suppress other messages
    })
    # Schedule the spider with the provided URLs and output format
    process.crawl(LinkSpider, urls=urls, output_format=output_format)
    # Start the crawling process
    process.start()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract links from URLs using Scrapy')
    parser.add_argument('-u', '--url', action='append', required=True, help='URL to extract links from')
    parser.add_argument('-o', '--output', choices=['stdout', 'json'], required=True, help='Output format')
    args = parser.parse_args()

    extract_links(args.url, args.output)

    # Sleep forever to keep the container running
    while True:
        time.sleep(86400)  # Sleep for 24 hours

