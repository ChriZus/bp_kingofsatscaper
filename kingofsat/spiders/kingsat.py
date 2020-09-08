# -*- coding: utf-8 -*-
import scrapy

class KingsatSpider(scrapy.Spider):
    
    name = 'kingofsat' #determine name of bot
    allowed_domains = ['https://tr.kingofsat.net/tvsat-turksat4a.php','https://tr.kingofsat.net/tvsat-turksat3a.php'] #make sure you allowed urls


    def start_requests(self): #function for urls
        urls = (
            (self.parse, 'https://tr.kingofsat.net/tvsat-turksat4a.php'),
            (self.parse, 'https://tr.kingofsat.net/tvsat-turksat3a.php'),
        )
        for callbackfunc, url in urls: #callback function for access each url in urls
            yield scrapy.Request(url, callback=callbackfunc)


    def parse(self, response):

        tables=response.xpath('//*[@class="fl"]') #Path of every tables
        bases=response.xpath('//table[@class="frq"]/tr') #Path of ever tables's header
        """
        Frequence = base.xpath('.//td[3]/text()').extract_first()
        Polarization = base.xpath('.//table[@class="frq"]/tr/td[4]/text()').extract_first()
        Area = base.xpath('.//table[@class="frq"]/tr/td[6]/a/text()').extract_first()
        SR = base.xpath('.//table[@class="frq"]/tr/td[9]/a[1]/text()').extract_first()
        FEC = base.xpath('.//table[@class="frq"]/tr/td[9]/a[2]/text()').extract_first()
        Channel=table.xpath('.//td[3]/a/text()').extract_first()
        V_PID=table.xpath('.//td[9]/text()[1]').extract_first()
        A_PID=table.xpath('.//td[10]/text()[1]').extract_first()
        Date=table.xpath('.//td[14]/a/text()[1]').extract_first()
        """

        for base, table in zip(bases[1:], tables): 
            rows = table.xpath('.//tr')
            for row in rows:
                if row.xpath('.//td[3]/a/text()').extract_first() is not None and \
                    row.xpath('.//td[10]/text()[1]').extract_first() !='Audio':
                    yield {
                        'Kanal' :       row.xpath('.//td[3]/a/text()').extract_first(),
                        'Frekans':      base.xpath('.//td[3]/text()').extract_first(),
                        'Polarizasyon': base.xpath('.//td[4]/text()').extract_first(),
                        'Kapsam':       base.xpath('.//td[6]/a/text()').extract_first(),
                        'SR':           base.xpath('.//td[9]/a[1]/text()').extract_first(),
                        'FEC':          base.xpath('.//td[9]/a[2]/text()').extract_first(),
                        'V-PID' :       row.xpath('.//td[9]/text()[1]').extract_first(),
                        'A-PID' :       row.xpath('.//td[10]/text()[1]').extract_first(),
                        #'Tarih' :       row.xpath('.//td[14]/a/text()[1]').extract_first(),
                    }