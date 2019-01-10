import scrapy


class ProfSpider(scrapy.Spider):
    name = "prof"

    def start_requests(self):
        url = 'https://engineering.stanford.edu/people/faculty/grid'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        """Parse index page."""
        prof_urls = response.xpath('//*[contains(@class, "field-content")]//a/@href').extract()
        for prof_url in prof_urls:
            yield response.follow(prof_url, self.parse_prof)

        # yield response.follow(prof_urls[0], self.parse_prof)

        # with open('.\\data\\data.jl', 'w') as f:
        #     f.write(str(prof_urls))

    def parse_prof(self, response):
        """Parse detail page."""
        name = response.xpath('//h1/text()').extract()
        yield {'name': name[0].strip()}
