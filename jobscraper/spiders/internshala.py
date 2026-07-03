import scrapy
from jobscraper.items import JobItem



class InternshalaSpider(scrapy.Spider):
    name = "internshala"
    allowed_domains = ["internshala.com"]
    start_urls = ["https://internshala.com/fresher-jobs/jobs-in-bangalore/"]

    def parse(self, response):
        for job in response.css("div.individual_internship"):
            item=JobItem()
            item["title"] = job.css("h2.job-internship-name a::text").get()
            item["company"] = (job.css("p.company-name::text").get() or "").strip()
            item["location"] = (job.css(".locations a::text").get() or "").strip()
            item["url"] = response.urljoin(job.css("a.job-title-href::attr(href)").get())
            item["source"] = "internshala"

            yield item

