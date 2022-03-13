import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # h1_tag = response.xpath("//h1/a/text()").extract()
        # tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()

        # yield {'H1_tag': h1_tag, 'Tags':tags}

        quotes = response.xpath('//*[@class="quote"]')

        for quote in quotes:
            text = quote.xpath('./*[@class="text"]/text()').extract() 
            author = quote.xpath('.//*[@class="author"]/text()').extract()         
            tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract()

            print("/n")
            print(text)
            print(author)
            print(tags)
            print("/n")

