from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import csv
import time
import utils

def get_unordered_list(driver, list_no):
    return driver.find_element(By.XPATH, "//*[@id=\"mw-content-text\"]/div/ul[{}]".format(list_no)).find_elements(
        By.TAG_NAME, "li")

def fill_history_and_filter(driver):
    history = []
    for unordered_list_no in range(2, 9):
        try:
            curr_unordered_list = get_unordered_list(driver, unordered_list_no)
            for list_item in curr_unordered_list:
                try:
                    item_text = list_item.text
                    item_date = item_text[3:item_text.find(',')]
                    item_date = utils.convert_date_with_digits(item_date)
                    if item_text in utils.skipped_updates or utils.keyword_contained_in(item_text):
                        continue
                    if (item_text.startswith("On") or item_text.startswith("In")) and utils.is_valid_date(item_date):
                        history.append(list_item)
                except:
                    continue
        except:
            break
    return history

options = Options()
options.add_argument('-headless')
driver = webdriver.Chrome(options=options,
                          executable_path="/Users/mabuhassira/PycharmProjects/pythonProject/chromedriver")

list_of_cards = []
file_all_cards_json = open("all_cards.json")
for card_name in json.load(file_all_cards_json):
    list_of_cards.append(card_name["name"])

excel_file = open("cards_balance_changes_history.csv", "a", newline="")

try:
    accept_cookies_closed = False
    card_count = 1
    for card_name in list_of_cards:
        url_card_info = "https://clashroyale.fandom.com/wiki/{}".format(card_name)
        driver.get(url_card_info)
        if not accept_cookies_closed:
            time.sleep(3)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/div/div/div[2]/div[2]"))).click()
            accept_cookies_closed = True

        print("{}: ".format(card_name))
        history_items = fill_history_and_filter(driver)

        when_released = driver.find_element(By.XPATH, "//*[@id=\"mw-content-text\"]/div/aside/div[5]/div")
        if card_name == "Mega Knight":
            when_released_date_converted = "08/09/2017"
        else:
            when_released_date_converted = utils.convert_date_with_alphabets(when_released.text)

        history_of_card = ""
        saw_first_info = False
        count_changes = 0
        for item in history_items:
            item_text = item.text
            if '\n' in item_text:
                item_text = item_text[0:item_text.index('\n')]
            date_of_info = item_text[3: item_text.find(",")]
            history_of_card += utils.convert_date_with_digits(date_of_info) + "|" + item_text + "\n"
            count_changes += 1
            print(item.text)
        csv.writer(excel_file).writerow((card_count, card_name, when_released.text, when_released_date_converted, history_of_card[:-1], count_changes))
        print()
        card_count += 1

except Exception as e:
    print(e)

finally:
    driver.close()
    file_all_cards_json.close()
    excel_file.close()