import scrapy
class QuotesSpider(scrapy.Spider):
    name = "JDSP"
    start_urls = ['https://www.justdial.com/Delhi/House-On-Rent/nct-10192844']
    def parse(self, response):
        names=response.css('span.lng_cont_name::text').extract()
        ratings=response.css('span.green-box::text').extract()
        addresses=response.css('span.cont_fl_addr::text').extract()
        for i in range(len(names)):
            yield {
                    'name':names[i],
                    'rating':ratings[i],                                                                                                                                                    'address':addresses[i]
                                                                                                                                                                                            }
