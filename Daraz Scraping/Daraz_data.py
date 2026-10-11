import csv
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://www.daraz.com.bd/catalog/?q=earbuds"

driver=webdriver.Chrome()

try:
    driver.get(url)
    input("If Chrome tab open press Enter: ")
    soup=BeautifulSoup(driver.page_source, "html.parser")
    products=soup.find_all("div", attrs={"data-qa-locator": "product-item"})

    if products:
        count=0

        with open(
            "earbus.csv", "w", newline="",  encoding="utf-8-sig"
        ) as file:
            writer= csv.writer(file)
            writer.writerow(["name", "price"])

            for product in products:
                name= product.find("div", class_="RfADt")
                price=product.find("span", class_="ooOxS")

                if name is not None and price is not None:
                    name=name.text.strip()
                    price=price.text.strip()

                    writer.writerow([name , price])
                    count+=1

                    print("name: ", name)
                    print("price: ", price)
                    print("----------------")
    
    
    else:
        print("Sorry There is no products")

finally:
    driver.quit()



            


