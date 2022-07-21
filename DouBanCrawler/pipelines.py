# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from DouBanCrawler.items import DoubancrawlerItem
import requests
import csv


class DoubancrawlerPipeline:
    @staticmethod
    def download_img(img):
        """
        根据图片src下载图片
        :param img:
        :return:
        """
        return requests.get(img).content

    def process_item(self, item, spider):
        if isinstance(item, DoubancrawlerItem):
            # 保存图片
            with open(r'Data/images/' + item['name'].split('/')[0] + '.jpg', 'wb') as f:
                f.write(self.download_img(item['img']))
            # 保存文字
            with open(r'Data/data.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([item['name'], item['score'], item['desc']])
        return item
