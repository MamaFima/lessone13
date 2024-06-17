import scrapy


class SvetparsSpider(scrapy.Spider):
    name = "svetpars"
    allowed_domains = ["https://svedivan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        svets = response.css('div._Ud0k')
        for svet in svets:
            yield {
                'name' : svet.css('div.lsooF span::text').get(),
                'price': svet.css('div.pY3d2 span::text').get(),
                'url': svet.css('a').attrib['href']

            }
