from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройка драйвера
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# Открытие страницы формы
driver.get("https://docs.google.com/forms")

# Функция для проверки всех полей формы на одной странице
def check_form(driver):
    bugs = []

    # Пример проверки: поиск всех текстовых полей и попытка заполнить их
    try:
        text_fields = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//input[@type="text"]')))
        for idx, field in enumerate(text_fields, start=1):
            try:
                field.send_keys(f"Test input {idx}")
            except Exception as e:
                bugs.append(f"Error with text field {idx}: {e}")
    except Exception as e:
        bugs.append(f"Error finding text fields: {e}")

    # Пример проверки: поиск всех кнопок и попытка кликнуть на них
    try:
        buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[text()="Отправить"]')))
        for idx, button in enumerate(buttons, start=1):
            try:
                button.click()
                time.sleep(2)  # небольшая задержка после клика
            except Exception as e:
                bugs.append(f"Error with button {idx}: {e}")
    except Exception as e:
        bugs.append(f"Error finding buttons: {e}")

    # Дополнительные проверки можно добавить аналогичным образом

    return bugs

# Функция для перехода на следующую страницу
def go_to_next_page(driver):
    try:
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Далее"]')))
        next_button.click()
        time.sleep(2)  # небольшая задержка после перехода
    except Exception as e:
        print(f"Error clicking 'Next' button: {e}")

# Проверка всех страниц формы и вывод списка багов
try:
    all_bugs = []

    # Проверка первой страницы
    all_bugs.extend(check_form(driver))
    go_to_next_page(driver)

    # Проверка второй страницы
    all_bugs.extend(check_form(driver))
    go_to_next_page(driver)

    # Проверка третьей страницы
    all_bugs.extend(check_form(driver))
    go_to_next_page(driver)
    # Проверка четвертой страницы
    all_bugs.extend(check_form(driver))
    
    if all_bugs:
        print("Bugs found:")
        for bug in all_bugs:
            print(bug)
    else:
        print("No bugs found.")
except Exception as e:
    print(f"An error occurred during the test: {e}")
finally:
    driver.quit()
