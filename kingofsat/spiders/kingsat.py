# -*- coding: utf-8 -*-
import scrapy

class KingsatSpider(scrapy.Spider):
    
    name = 'kingofsat' #determine name of bot
    allowed_domains = ['https://en.kingofsat.net/sat-astra1l.php',
                       'https://en.kingofsat.net/sat-astra1m.php',
                       'https://en.kingofsat.net/sat-astra1n.php',
                       'https://en.kingofsat.net/sat-astra3b.php',
                       'https://en.kingofsat.net/sat-astra3c.php',
                      ] #make sure you allowed urls


    def start_requests(self): #function for urls
        urls = (
            (self.parse, 'https://en.kingofsat.net/sat-astra1l.php', 'Astra 1L'),
            (self.parse, 'https://en.kingofsat.net/sat-astra1m.php', 'Astra 1M'),
            (self.parse, 'https://en.kingofsat.net/sat-astra1n.php', 'Astra 1N'),
            (self.parse, 'https://en.kingofsat.net/sat-astra3b.php', 'Astra 3B'),
            (self.parse, 'https://en.kingofsat.net/sat-astra3c.php', 'Astra 3C'),
        )
        for callbackfunc, url in urls: #callback function for access each url in urls
            yield scrapy.Request(url, callback=callbackfunc)


    def parse(self, response):
        '''
        TODO: include satellite name in result table

        '''
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
                        'Channel' :       row.xpath('.//td[3]/a/text()').extract_first(),
                        'Frequency':      base.xpath('.//td[3]/text()').extract_first(),
                        'Polarization': base.xpath('.//td[4]/text()').extract_first(),
                        'Area':       base.xpath('.//td[6]/a/text()').extract_first(),
                        'SR':           base.xpath('.//td[9]/a[1]/text()').extract_first(),
                        'FEC':          base.xpath('.//td[9]/a[2]/text()').extract_first(),
                        'V-PID' :       row.xpath('.//td[9]/text()[1]').extract_first(),
                        'A-PID' :       row.xpath('.//td[10]/text()[1]').extract_first(),
                        #'Tarih' :       row.xpath('.//td[14]/a/text()[1]').extract_first(),
                    }
