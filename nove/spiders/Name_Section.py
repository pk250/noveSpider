from scrapy.http import Request
import scrapy
from nove.items import Name,Sec

class RequestNaSe(scrapy.Spider):
    name="requestName"
    allowed_domains=["biquge5200.com"]
    url="http://www.biquge5200.com/"
    def start_requests(self):
        for i in range(100):
            for n in range(3000):
                url=self.url+str(i)+"_"+str(n).zfill(3)
                yield Request(url,self.getNaSe)
    def getNaSe(self,response):
        Item=Name()
        Item['Name']=response.xpath("//*[@property='og:novel:book_name']//@content").extract()[0]
        Item['Nurl']=response.xpath("//*[@property='og:novel:read_url']//@content").extract()[0]
        # yield Item
        Selist=response.xpath("//dd/a")
        for i in range(len(Selist)):
            SeItem=Sec()
            SeItem['Title'] =Selist.xpath('text()').extract()[i]
            SeItem['Surl'] =Selist.xpath('@href').extract()[i]
            yield SeItem
            print SeItem
        print response.text
        print Item