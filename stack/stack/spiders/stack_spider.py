import re

from scrapy import Spider
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector

from stack.items import StackItem


class StackSpider(Spider):
    name = 'stack'
    allowed_domains = ['stackoverflow.com']
    start_urls = [
        'http://stackoverflow.com/questions?pagesize=50&sort=newest'
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        for i, question in enumerate(questions):
            link = question.xpath(
                'a[@class="question-hyperlink"]/@href'
            ).extract()[0]

            id = re.search('/questions/[0-9]+/', link).group(0)[11:-1]
            author = question.xpath(
                '//div[@class="user-details"]/a/text()'
            ).extract()[i]
            title = question.xpath(
                'a[@class="question-hyperlink"]/text()'
            ).extract()[0]
            published = question.xpath(
                '//span[@class="relativetime"]/@title'
            ).extract()[i]

            yield StackItem(
                _id=id,
                author=author,
                title=title,
                url=link,
                published=published
            )


if __name__ == '__main__':
    spider = CrawlerProcess()
    spider.crawl(StackSpider)
    spider.start()
