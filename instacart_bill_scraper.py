from datetime import datetime
from bs4 import BeautifulSoup
import sys

class InstacartBillScraper:
    def __init__(self, file_path:str = 'Instacart - Same-day Grocery Delivery.html'):
        self.file_path = file_path
        self.order_time = None
        self.items = {}
        self.charges = 0
        
    def _parse_html(self):
        try:
            with open(self.file_path, 'r') as f:
                soup = BeautifulSoup(f, 'html.parser')
        
        except FileNotFoundError:
            print("No File Found")
        
        date_format = "%B %d, %Y"

        driver_delivery_schedule_text = soup.find('div', class_="DriverDeliverySchedule")
        driver_delivery_schedule_text = driver_delivery_schedule_text.get_text().split('and')[0].split('on')[1].strip().replace('th', '')
        
        order_time = datetime.strptime(driver_delivery_schedule_text, date_format)
        self.order_time = order_time.strftime("%Y-%m-%d")

        items = {}
        for tag in soup.select("div[class='item-row item-delivered'], div[class='item-row item-delivered item-actually-delivered']"):
            try:
                item_name = tag.select("div.item-name")[0].get_text(strip=True)
                item_price = tag.select("div.item-price")[0].get_text(strip=True).split('$')[1]
                items[item_name] = item_price
            except Exception as e:
                print(f'[!] Error parsing: {e}')
            
        charges = soup.select("h2[class='order-totals-title'] ~ div > table[class='charges'] > tr")
        for tr in charges:
            charge_type_elem = tr.select("td.charge-type")[0]
            amount_elem = tr.select("td.amount")[0]

            if not charge_type_elem or not amount_elem:
                continue

            charge_type = charge_type_elem.get_text(strip=True).lower()
            amount_text = amount_elem.get_text(strip=True)

            if not amount_text or charge_type in ['total', 'you saved', 'instacart+ member free delivery!']:
                continue

            try:
                amount = float(amount_text.replace('$', '').replace(',', ''))
            except ValueError:
                continue

            if 'tax' in charge_type or 'fee' in charge_type:
                self.charges += amount
            elif 'discount' in charge_type:
                self.charges += amount

        return items
    
    def generate_receipt(self):
        self.items = self._parse_html()

        with open(str(self.order_time)+'.txt', 'w') as f:
            for i in self.items:
                f.write(f'{i.replace(",", " ... ")},[People],{self.items[i]}\n')
            f.write(f'charge:{self.charges}\n')
            f.write(f'discount:0\n')

def main():
    if len(sys.argv) != 2:
        print("Usage: python instacart_bill_scraper.py <html_bill_file>")
        sys.exit(1)
    
    scraper = InstacartBillScraper(sys.argv[1])
    scraper.generate_receipt()

if __name__ == "__main__":
    main()