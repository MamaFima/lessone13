from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


def get_paragraphs(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        input()


def get_related_links(browser):
    related_links = []

    try:
        see_also_section = browser.find_element(By.XPATH,
                                                "//span[@id='См._также']/ancestor::h2/following-sibling::ul[1]")
        links = see_also_section.find_elements(By.TAG_NAME, "a")
        for link in links:
            href = link.get_attribute("href")
            if href and "wikipedia.org/wiki/" in href:
                related_links.append(href)
    except:
        pass

    if not related_links:
        links = browser.find_elements(By.TAG_NAME, "a")
        for link in links:
            href = link.get_attribute("href")
            if href and "wikipedia.org/wiki/" in href and "redlink=1" not in href:
                related_links.append(href)

    return related_links


def main():
    user_input = input("Что вы хотите узнать в Википедии? ")

    browser = webdriver.Chrome()
    browser.get("https://ru.wikipedia.org")

    assert "Википедия" in browser.title
    time.sleep(2)

    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(user_input)
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)

    try:
        first_link = browser.find_element(By.CSS_SELECTOR, "ul.mw-search-results li a")
        first_link.click()
    except:
        print("Не удалось найти статью по запросу.")
        browser.quit()
        return

    time.sleep(2)

    while True:
        user_action = input(
            "Хотите просмотреть параграфы этой статьи или перейти на другую связанную статью? (p/s/q для выхода) ").strip().lower()
        if user_action == "p":
            get_paragraphs(browser)
        elif user_action == "s":
            related_links = get_related_links(browser)
            if not related_links:
                print("Связанных статей не найдено.")
                continue
            link = random.choice(related_links)
            print(f"Переход по ссылке: {link}")
            browser.get(link)
            time.sleep(2)
        elif user_action == "q":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Пожалуйста, введите 'p', 's' или 'q'.")

    browser.quit()


if __name__ == "__main__":
    main()
