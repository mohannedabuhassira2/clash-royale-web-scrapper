from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import csv
import time
import utils

def camel_to_snake(s):
    return ''.join(['-'+c.lower() if c.isupper() else c for c in s]).lstrip('-').replace(" ", "")

def get_all_card_names():
    list_of_cards = []
    file_all_cards_json = open("all_cards.json")
    for card_name in json.load(file_all_cards_json):
        list_of_cards.append(card_name["name"])
    file_all_cards_json.close()
    return list_of_cards

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

def scrape_data(list_of_cards, excel_file):
    try:
        accept_cookies_closed = False
        card_count = 1
        for card_name in list_of_cards:
            url_card_info = "https://clashroyale.fandom.com/wiki/{}".format(card_name)
            driver.get(url_card_info)
            if not accept_cookies_closed:
                time.sleep(3)
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/div/div/div[2]/div[2]"))).click()
                accept_cookies_closed = True

            print("{}: ".format(card_name))
            history_items = fill_history_and_filter(driver)

            when_released = driver.find_element(By.XPATH, "//*[@id=\"mw-content-text\"]/div/aside/div[5]/div")
            if card_name == "Mega Knight":
                when_released_date_converted = "08/09/2017"
            else:
                when_released_date_converted = utils.convert_date_with_alphabets(when_released.text)

            history_of_card = ""
            count_changes = 0
            for item in history_items:
                item_text = item.text
                if '\n' in item_text:
                    item_text = item_text[0:item_text.index('\n')]
                date_of_info = item_text[3: item_text.find(",")]
                history_of_card += utils.convert_date_with_digits(date_of_info) + "|" + item_text + "\n"
                count_changes += 1
                print(item.text)
            csv.writer(excel_file).writerow((card_count, card_name, when_released.text, when_released_date_converted,
                                             history_of_card[:-1], count_changes))
            print()
            card_count += 1

    except Exception as e:
        print(e)

    finally:
        driver.close()

def write_history_for_all_months(list_of_cards, excel_file):
    map_card_name_to_num_changes = {}
    map_month_to_changes = {}

    for card in list_of_cards:
        map_card_name_to_num_changes[card] = -1

    months = utils.month_year_iter(1, 2016, 11, 2022)
    for month in months:
        map_month_to_changes[month] = []

    csvreader = csv.reader(excel_file)
    next(csvreader)
    for row in csvreader:
        card_name = row[1]
        card_release_date = row[3]
        all_changes = row[4].split('\n')
        all_changes.insert(0, "{}|On {},{} was released.".format(card_release_date, card_release_date, card_name))
        for change in all_changes:
            if not change:
                continue

            change_date = change[0:10]
            change_date_in_month_year = change_date[3:]
            change_text = change[25:].capitalize()
            card_count = map_card_name_to_num_changes[card_name]
            map_card_name_to_num_changes[card_name] = card_count + 1
            map_month_to_changes[change_date_in_month_year].append(
                card_name + "|" + str(card_count + 1) + "|" + change_date + "|" + change_text
            )

        month_changes_file = open("month_changes_file.csv", "r+", newline="")
        for month in months:
            month_data_changes = map_month_to_changes[month]
            month_changes = ""
            for month_data in month_data_changes:
                month_changes += month_data + "\n"
            csv.writer(month_changes_file).writerow((month, month_changes[:-1]))
        month_changes_file.close()

def fill_output_file_header(output_file):
    months = utils.month_year_iter(1, 2016, 11, 2022)
    header = ["", ""]
    for month in months:
        header.append(month)
    csv.writer(output_file).writerow(header)

def fill_cards_in_output_file(cards_changes_file):
    reader = csv.reader(cards_changes_file)
    next(reader)
    for row in reader:
        card_name = row[1]
        card_release_date = row[3]
        all_changes = row[4].split('\n')
        all_changes.insert(0, "{}|On {},{} was released.".format(card_release_date, card_release_date, card_name))
        months = utils.month_year_iter(1, 2016, 11, 2022)

        card_name_in_snake_case = ''
        if card_name == "P.E.K.K.A":
            card_name_in_snake_case = "pekka"
        elif card_name == "Mini P.E.K.K.A":
            card_name_in_snake_case = "mini-pekka"
        card_name_in_snake_case = camel_to_snake(card_name)
        card_image_url = "https://cdn.royaleapi.com/static/img/cards-150/{}.png".format(card_name_in_snake_case)

        row = [card_name, card_image_url]
        map_month_to_num_changes = {}
        for month in months:
            map_month_to_num_changes[month] = -1

        num_changes = 0
        for change in all_changes:
            if not change:
                continue

            change_date = change[0:10]
            change_date_in_month_year = change_date[3:]
            map_month_to_num_changes[change_date_in_month_year] = num_changes
            num_changes += 1

        # find the first number != -1
        first_non_negative_number = 0
        for month in months:
            if map_month_to_num_changes[month] != -1:
                first_non_negative_number = map_month_to_num_changes[month]
                break

        curr_changes = first_non_negative_number
        saw_first_non_negative = False
        for month in months:
            if curr_changes == first_non_negative_number and map_month_to_num_changes[month] == -1 and not saw_first_non_negative:
                row.append("")
            elif map_month_to_num_changes[month] != -1:
                if map_month_to_num_changes[month] == first_non_negative_number:
                    saw_first_non_negative = True
                curr_changes = map_month_to_num_changes[month]
                row.append(str(curr_changes))
            else:
                row.append(str(curr_changes))

        csv.writer(output_file).writerow(row)

'''
options = Options()
options.add_argument('-headless')
driver = webdriver.Chrome(options=options,
                          executable_path="/Users/mohannedabuhassira/Desktop/clash-royale-web-scrapper/chromedriver")
'''
cards_changes_file = open("cards_balance_changes_history.csv", "r+", newline="")
list_of_cards = get_all_card_names()
# scrape_data(list_of_cards, excel_file)
# write_history_for_all_months(list_of_cards, cards_changes_file)
output_file = open("output.csv", "r+", newline="")
fill_output_file_header(output_file)
fill_cards_in_output_file(cards_changes_file)