import scrapy
from bs4 import BeautifulSoup

from mySpider.items import XimalayaItem


class XimalayaSpider(scrapy.Spider):
    name = "ximalaya"
    allowed_domains = ["ximalaye.com", "www.ximalaya.com"]
    start_urls = ["https://www.ximalaya.com/category/a9/"]

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

        base_url = "https://www.ximalaya.com"  # next_page uri: /category/a9/p2/

        # decode next page url
        next_page = response.xpath('//*[@id="award"]/main/div[1]/div[3]/div[3]/nav/ul/li')[-1]
        next_page_url = BeautifulSoup(next_page.extract(), 'html.parser').find("a").get("href")

        # get title, intro_1, and request intro detail page
        for each in response.xpath('//*[@id="award"]/main/div[1]/div[3]/div[2]/ul/li'):
            item = XimalayaItem()
            title = each.xpath('div/a/@title')[0].extract()
            introhref = each.xpath('div/a/@href')[0].extract()
            intro_1 = each.xpath('div/a[2]/text()')[0].extract()

            item['title'] = title
            item['intro_1'] = intro_1
            yield scrapy.Request(introhref, callback=self.parse_detail
                                 , meta={'item': item})

        # check if have next page
        if next_page_url:
            yield scrapy.Request(base_url+str(next_page_url), callback=self.parse, headers=headers)

    # for intro_2 & item_img
    def parse_detail(self, response):
        item = response.meta['item']
        content = ''

        content_list = response.xpath('//*[@id="award"]/main/div[1]/div[2]/div[1]/div[1]/div[3]/article')
        for data in content_list:
            replace = data.extract().replace(' ', '')
            replace = BeautifulSoup(replace, 'html.parser')
            for i in replace:
                print("i.text", i.text)
                content += i.text
        item['intro_2'] = content
        item['img'] = response.xpath('//*[@id="award"]/main/div[1]/div[2]/div[1]/div[1]/div[2]/img/@src')[0].extract()

        yield item
