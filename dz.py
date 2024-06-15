from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

user_input = input("Что вы хотите узнать в Википедии?")

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

assert "Википедия" in browser.title
time.sleep(5)

search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(user_input)
search_box.send_keys(Keys.RETURN)

time.sleep(5)
a = browser.find_element(By.LINK_TEXT, user_input)
a.click()
time.sleep(5)

user_action = input("Хотите просмотреть параграфы этой статьи или перейти на другую связанную статью? p/s")
if user_action == "p":
    paragraphs = browser.find_elements(By.TAG_NAME, "p")

    for paragraph in paragraphs:
        print(paragraph.text)
        input()

else:
    hatnotes = []

    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable":
            hatnotes.append(element)
    print(hatnotes)
    hatnote = random.choice(hatnotes)
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    browser.get(link)
    time.sleep(5)

    user_action = input("Хотите просмотреть параграфы этой статьи или перейти на другую связанную статью? p/s")
    if user_action == "p":
        paragraphs = browser.find_elements(By.TAG_NAME, "p")

        for paragraph in paragraphs:
            print(paragraph.text)
            input()

    else:
        hatnotes = []

        for element in browser.find_elements(By.TAG_NAME, "div"):
            cl = element.get_attribute("class")
            if cl == "hatnote navigation-not-searchable":
                hatnotes.append(element)
        print(hatnotes)
        hatnote = random.choice(hatnotes)
        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
        browser.get(link)
        time.sleep(5)








