from instacart_bill_scraper import InstacartBillScraper

scraper = InstacartBillScraper()

scraper.generate_receipt()


# from bs4 import BeautifulSoup
# # from datetime import datetime

# soup = BeautifulSoup(open('Instacart - Same-day Grocery Delivery.html'), 'html.parser')
# # print(soup.find('div', class_="DriverDeliverySchedule"))

# # date_format = "%B %d, %Y"
# # driver_delivery_schedule_text = soup.find('div', class_="DriverDeliverySchedule")
# # driver_delivery_schedule_text = driver_delivery_schedule_text.get_text().split('and')[0].strip().split('on ')[1].strip().replace('th', '')

# # order_time = datetime.strptime(driver_delivery_schedule_text, date_format)
# # print(order_time)

# for tag in soup.select("div[class='item-row item-delivered'], div[class='item-row item-delivered item-actually-delivered']"):
#     try:
#         item_name = tag.select("div.item-name")[0].get_text(strip=True)
#         item_price = tag.select("div.item-price")[0].get_text(strip=True).replace('$', '')
#     except Exception as e:
#         print(f'[!] Error parsing: {e}')