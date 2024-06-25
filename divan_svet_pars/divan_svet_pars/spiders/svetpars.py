#import scrapy

#class SvetparsSpider(scrapy.Spider):
#   name = "svetpars"
#   allowed_domains = ["https://svedivan.ru"]
#   start_urls = ["https://www.divan.ru/category/svet"]

#   def parse(self, response):
#       svets = response.css('div._Ud0k')
#       for svet in svets:
#           yield {
#               'name': svet.css('div.lsooF span::text').get(),
#               'price': svet.css('div.pY3d2 span::text').get(),
#               'url': svet.css('a').attrib['href']

#           }
#       next_page = response.css('li.next a::attr(href)').get()
#       if next_page is not None:
#           yield response.follow(next_page, self.parse)

import scrapy

class SvetparsSpider(scrapy.Spider):
    name = "svetpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    custom_settings = {
        'DOWNLOAD_DELAY': 2,
    }

    visited_pages = set()
    visited_urls = set()

    def parse(self, response):
        self.logger.info(f"Parsing page: {response.url}")

        self.visited_pages.add(response.url)

        svets = response.css('div._Ud0k')

        self.logger.info(f"Found {len(svets)} items on this page")

        for svet in svets:
            url = svet.css('a::attr(href)').get()
            if url:
                full_url = response.urljoin(url)
                self.logger.info(f"URL found: {full_url}")  # Debugging line
                if full_url not in self.visited_urls:
                    self.visited_urls.add(full_url)
                    name = svet.css('div.lsooF span::text').get()
                    price = svet.css('div.pY3d2 span::text').get()
                    self.logger.info(f"Item: {name}, Price: {price}, URL: {full_url}")  # Debugging line
                    yield {
                        'name': name,
                        'price': price,
                        'url': full_url
                    }
                else:
                    self.logger.info(f"Duplicate URL skipped: {full_url}")

        self.logger.info(f"Checking for next page links...")
        next_pages = response.css('a[class*="PaginationLink"]::attr(href)').getall()
        self.logger.info(f"Found next page links: {next_pages}")

        for next_page in next_pages:
            next_page_url = response.urljoin(next_page)
            if next_page_url not in self.visited_pages and next_page_url != response.url:
                self.visited_pages.add(next_page_url)
                self.logger.info(f"Next page URL: {next_page_url}")
                yield scrapy.Request(next_page_url, callback=self.parse_next_page)

        if not next_pages:
            self.logger.info("No more pages to load.")

    def parse_next_page(self, response):
        self.logger.info(f"Parsing next page: {response.url}")

        svets = response.css('div._Ud0k')

        self.logger.info(f"Found {len(svets)} items on this page")

        for svet in svets:
            url = svet.css('a::attr(href)').get()
            if url:
                full_url = response.urljoin(url)
                self.logger.info(f"URL found: {full_url}")  # Debugging line
                if full_url not in self.visited_urls:
                    self.visited_urls.add(full_url)
                    name = svet.css('div.lsooF span::text').get()
                    price = svet.css('div.pY3d2 span::text').get()
                    self.logger.info(f"Item: {name}, Price: {price}, URL: {full_url}")  # Debugging line
                    yield {
                        'name': name,
                        'price': price,
                        'url': full_url
                    }
                else:
                    self.logger.info(f"Duplicate URL skipped: {full_url}")

        next_pages = response.css('a[class*="PaginationLink"]::attr(href)').getall()
        self.logger.info(f"Found next page links: {next_pages}")

        for next_page in next_pages:
            next_page_url = response.urljoin(next_page)
            if next_page_url not in self.visited_pages and next_page_url != response.url:
                self.visited_pages.add(next_page_url)
                self.logger.info(f"Next page URL: {next_page_url}")
                yield scrapy.Request(next_page_url, callback=self.parse_next_page)

        if not next_pages:
            self.logger.info("No more pages to load.")









