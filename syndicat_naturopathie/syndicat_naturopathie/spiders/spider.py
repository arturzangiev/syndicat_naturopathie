# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver

class SyndicatNaturopathie(scrapy.Spider):
    name = "spider"
    allowed_domains = ["syndicat-naturopathie.fr"]
    start_urls = [ "http://annuaire.syndicat-naturopathie.fr/?p={}&category=0&zoom=10&is_mile=0&directory_radius=50&view=grid&sort=random".format(x) for x in range(1, 47) ]

    def __init__(self):
        self._driver = webdriver.Chrome('/Users/arturzangiev/Projects/syndicat-naturopathie/syndicat_naturopathie/chromedriver')
        # self._driver = webdriver.PhantomJS('/Users/arturzangiev/Projects/syndicat-naturopathie/syndicat_naturopathie/phantomjs')

    def parse(self, response):
        blocks = response.xpath('//div[contains(@id,"sabai-entity-content")]')
        for block in blocks:
            fields = dict()
            fields['name'] = block.xpath('.//div[@class="sabai-directory-title"]/a/@title').extract_first()
            fields['email'] = block.xpath('.//div[@class="sabai-directory-contact-email"]/a//text()').extract_first()
            yield fields