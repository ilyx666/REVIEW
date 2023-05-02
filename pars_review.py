from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# # Настройки для запуска браузера в фоновом режиме
# options = Options()
# options.add_argument('--headless')

# Инициализация браузера
driver = webdriver.Chrome()
url = 'https://winline.ru/stavki/sport/futbol/rossiya'
driver.get(url)
# Ожидание загрузки страницы и элементов с помощью явных ожиданий
wait = WebDriverWait(driver, 10)
elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'name')))

# Извлечение названий команд из элементов
team_names = []
for element in elements:
    team_names.append(element.text.strip())

# Закрытие браузера
driver.quit()

# Вывод результата
print(team_names)
