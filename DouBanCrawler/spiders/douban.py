import scrapy
from bs4 import BeautifulSoup
from DouBanCrawler.items import DoubancrawlerItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/chart']

    def parse(self, response, **kwargs):
        soup = BeautifulSoup(response.text, "lxml")
        item_array = soup.select("div [class='indent'] div table")
        for item in item_array:
            try:
                name = item.find('a', class_="").text.strip().replace('\n', '').replace(' ', '')
                score = item.find('span', class_="rating_nums").text
                desc = item.find('p', class_="pl").text
                image = item.find('img', class_="")["src"]
                result = DoubancrawlerItem()
                result['name'] = name
                result['score'] = score
                result['desc'] = desc
                result['img'] = image
                yield result
            except Exception as e:
                print(e.args)
