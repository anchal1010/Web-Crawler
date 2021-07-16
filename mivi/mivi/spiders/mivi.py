import scrapy
from ..items import MiviItem

class MiviSpider(scrapy.Spider):
    name = 'out'
 
    start_urls = ['https://www.amazon.in/s?k=coffee+beans&crid=1M3WH35UW3VSW&sprefix=coffee%2Caps%2C376&ref=nb_sb_ss_ts-doa-p_2_6/']

    def parse(self, response):
        items = MiviItem()
        product_name = response.css('.a-size-base-plus::text').extract()
        price_price = response.css('.a-price-whole::text').extract()
        desc_name = response.css('.a-color-secondary::text').extract()
        
        items["product_name"]=product_name
        items["price_price"]=price_price
        items["desc_name"]=desc_name
        yield items 