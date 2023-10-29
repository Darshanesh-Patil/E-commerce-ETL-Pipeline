import csv
import time
import random
import string

# Define the fieldnames for the CSV file
fieldnames = ['user_id', 'session_id', 'category', 'brand', 'cost_price','selling_price', 'discount', 'timestamp',
              'referrer', 'device_type', 'os', 'browser', 'ip_address', 'payment_method']

brands = [
    "Nike", "Adidas", "Apple", "Samsung", "Sony", "LG", "Dell", "HP", "Coca-Cola", "Pepsi",
    "Toyota", "Honda", "Ford", "Mercedes-Benz", "BMW", "Mitsubishi", "Nestle", "Microsoft",
    "Amazon", "Google", "Canon", "Panasonic", "Lenovo", "Acer", "ASUS", "LG", "Philips", "Toshiba",
    "Vizio", "Fujifilm", "Nikon", "GoPro", "Sony", "Audi", "Volkswagen", "Hyundai", "Kia",
    "General Electric", "Siemens", "Bosch", "Vodafone", "Verizon", "AT&T", "McDonald's", "Burger King",
    "Pizza Hut", "Domino's", "Zara", "H&M", "Gap", "Forever 21", "Levi's", "Puma", "Reebok",
    "Converse", "Under Armour", "Rolex", "Casio", "Swatch", "Timex", "Lacoste", "Calvin Klein", "Tommy Hilfiger",
    "Diesel", "Hugo Boss", "Giorgio Armani", "Prada", "Gucci", "Louis Vuitton", "Chanel", "Dior", "Fendi",
    "Versace", "Ralph Lauren", "Burberry", "Hermes", "Coach", "Michael Kors", "Tiffany & Co.", "Pandora", "Swarovski",
    "Sony", "Bose", "Beats by Dre", "Bowers & Wilkins", "Harman Kardon", "JBL", "Sony", "Bose", "Sennheiser",
    "Logitech", "Corsair", "SteelSeries", "Razer", "Nvidia", "AMD", "Intel", "Western Digital", "Seagate", "SanDisk",
    "Crucial", "Kingston", "Lexar", "Corsair", "G.SKILL", "Ballistix", "Acer", "ASUS", "Dell", "Lenovo", "HP",
    "Apple", "Samsung", "LG", "Sony", "Philips", "Panasonic", "Toshiba", "Fujitsu", "Microsoft", "Intel", "AMD",
    "Nvidia", "ASRock", "Gigabyte", "MSI", "EVGA", "Sapphire", "XFX", "PowerColor", "ASUS", "Corsair", "Cooler Master",
    "NZXT", "Fractal Design", "Phanteks", "Thermaltake", "Antec", "Cooler Master", "Kingston", "Samsung", "Crucial",
    "Corsair", "Western Digital", "Seagate", "Logitech", "Razer", "SteelSeries", "HyperX", "BenQ", "ASUS", "Acer",
    "Dell", "HP", "Lenovo", "Microsoft", "Intel", "AMD", "Nvidia", "Sony", "Samsung", "LG", "Panasonic", "Toshiba",
    "Philips", "Dell", "HP", "Acer", "ASUS", "Lenovo", "Microsoft", "Sony", "Apple", "Samsung", "LG", "Nokia",
    "Xiaomi", "OnePlus", "Motorola", "Google", "Huawei", "HTC", "Blackberry", "Sony Ericsson", "ZTE", "Alcatel",
    "Western Digital", "Seagate", "Kingston", "SanDisk", "Crucial", "Logitech", "Razer", "SteelSeries", "Corsair", "Sony",
    "Samsung", "Panasonic", "Toshiba", "LG", "Philips", "Dell", "HP", "Acer", "ASUS", "Lenovo", "Microsoft", "Apple",
    "Samsung", "Sony", "Xiaomi", "OnePlus", "Nokia", "LG", "Motorola", "Google", "Blackberry", "HTC", "Sony Ericsson",
]

os = [
    "Windows",
    "Linux",
    "macOS",
    "iOS",
    "Android",
    "Chrome OS",
    "Ubuntu"
]

browsers = [
    'Chrome',
    'Firefox',
    'Safari',
    'Edge',
    'Microsoft Edge',
    'Opera',
    'Brave',
    'Vivaldi',
    'Yandex Browser'
]



payment_methods = [
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Mobile Wallets",
    "UPI",
    "IMPS",
    "NEFT",
    "RTGS",
    "Cash on Delivery (COD)",
    "EMI"
]

categories = [
    "Smartphones",
    "Laptops",
    "Tablets",
    "Desktop Computers",
    "Televisions",
    "Audio Equipment",
    "Digital Cameras",
    "Wearable Technology",
    "Gaming Consoles",
    "Home Appliances",
    "Accessories",
    "Networking Equipment",
]

devices = ["Smartphones", "Tablets", "Laptops", "Desktop Computers", "Smart TVs", "Gaming Consoles"]



# Define a function to generate a row of fake data
def generate_row():
    row = {}
    row['user_id'] = "USI_"+str(random.randint(1, 1000))
    row['session_id'] = ''.join(random.choice(string.hexdigits) for _ in range(32))
    row['category'] = random.choice(categories)
    row['brand'] = random.choice(brands)
    row['cost_price'] = random.randint(4000, 100000)
    
    # Generate a selling price between 5% to 10% of the price
    price = row['cost_price']
    selling_price = price + (random.uniform(0.05, 0.20) * price)
    row['selling_price'] = round(selling_price, 0)
    
    
    row['discount'] = random.randint(100, 2000)
    row['timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    row['referrer'] = random.choice([''.join(random.choice(string.ascii_lowercase) for _ in range(3)) + str(random.randint(1, 1000)),0])
    row['device_type'] = random.choice(devices)
    row['os'] = random.choice(os)
    row['browser'] = random.choice(browsers)
    row['ip_address'] = '.'.join(str(random.randint(0, 255)) for _ in range(4))
    row['payment_method'] = random.choice(payment_methods)
    return row

# Define a function to write the rows to a CSV file
def write_to_csv(rows):
    with open('D:\Project\E-commerce-ETL-Pipeline-Project\dynamic_data\purchase_online_log.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if the file is empty and write the header row
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerows(rows)

# Generate and write the rows to a CSV file with a 
while True:  # Infinite loop
    rows = []
    num_rows = random.randint(1, 10)
    for i in range(num_rows):
        rows.append(generate_row())
    write_to_csv(rows)
    time_interval = random.randint(5, 30) # random time interval between 5 to 30 seconds
    time.sleep(time_interval)
