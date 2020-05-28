# -*- coding: utf-8 -*-
import scrapy
from tft_tier.items import TierItem


class TierSpider(scrapy.Spider):
    name = 'tier'
    allowed_domains = ['https://lolchess.gg/leaderboards?region=br']
    start_urls = ['https://lolchess.gg/leaderboards?region=br']

    def parse(self, response):
        for item in response.css('tr'):
            imagem = item.css('td img::attr(src)').get()
            rank = item.css('td span::text').get()
            user = item.css('td a::text').get()
            link = item.css('td a::attr(href)').get()
            tierImagem = item.css('td.tier img::attr(src)').get()
            tier = item.css('td.tier span::text').get()
            ##
            if user is not None:
                user = user.strip()
                #imagem = imagem.replace('//', '')
                #tierImagem = tierImagem.replace('//', '')
                imagem = 'https:' + imagem;
                tierImagem = 'https:' + tierImagem;
                tierObj = TierItem(imagem = imagem, rank = rank, user = user, link = link, tierImagem = tierImagem, tier = tier)
                yield tierObj
