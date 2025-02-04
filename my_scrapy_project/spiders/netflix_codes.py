import scrapy


class NetflixCodesSpider(scrapy.Spider):
    name = "netflix_codes"
    start_urls = ["https://www.cloudwards.net/netflix-secret-codes/"]

    def parse(self, response):
        # Select all rows within the table body
        rows = response.xpath('//figure[@class="wp-block-table"]//table/tbody/tr')

        for row in rows:
            # Extract the category title and code from the current row
            title = row.xpath('./td[1]//text()').get()  # Get text inside the first <td>
            code = row.xpath('./td[2]/text()').get()    # Get text inside the second <td>

            yield {
                "title": title.strip() if title else None,
                "code": code.strip() if code else None,
            }
