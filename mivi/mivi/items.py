# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MiviItem(scrapy.Item):
    # define the fields for your item here like:
    product_name  = scrapy.Field()
    price_price  = scrapy.Field()
    desc_name  = scrapy.Field()
    pass
