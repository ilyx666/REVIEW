import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def get_source_html(url):
    s = Service(r"C:\Users\ilyx\Desktop\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(3)

        while True:
            time.sleep(10)
            find_name = driver.find_element(By.CLASS_NAME, "footer__container")
            if driver.find_elements(By.CLASS_NAME, "footer__copyrights"):
                with open(r"C:\Users\ilyx\Desktop\source-page.html", "w", encoding="utf-8") as file:
                    file.write(driver.page_source)

                break
            else:
                actions = ActionChains(driver)
                actions.move_to_element(find_name).perform()
                time.sleep(3)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()
def main():
    get_source_html(url="https://www.wildberries.ru/catalog/elektronika/smart-chasy")

if __name__ == "__main__":
    main()
