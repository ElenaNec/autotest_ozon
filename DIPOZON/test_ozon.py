import yaml
import time
from selenium.webdriver.common.keys import Keys

with open(r"C:\Users\user\Desktop\pythonProject1\DIPOZON\config.yaml", encoding="utf-8") as f:
    testdata = yaml.safe_load(f)


def test_step1(site, field_xpath, result1_xpath):
    # поиск по ключевому слову keyword1
    input_keyword = site.find_field("xpath", field_xpath)
    input_keyword.send_keys(testdata['keyword1'])
    time.sleep(testdata['sleep_time'])
    input_keyword.send_keys(Keys.ENTER)
    time.sleep(5)
    site.find_field("xpath", """/html/body""").click()
    time.sleep(10)

    result = site.find_field("xpath", result1_xpath)
    assert result.text == "Кофе"


def test_step2(site, category_xpath, subcategory_xpath, subsubcategory_xpath, result2_xpath):
    # поиск по категории "Одежда и обувь", "Рубашки
    click_cloth = site.find_field("xpath", category_xpath)
    click_cloth.click()
    time.sleep(testdata['sleep_time'])

    click_cloth1 = site.find_field("xpath", subcategory_xpath)
    click_cloth1.click()
    time.sleep(testdata['sleep_time'])

    click_cloth2 = site.find_field("xpath", subsubcategory_xpath)
    click_cloth2.click()
    time.sleep(testdata['sleep_time'])

    result = site.find_field("xpath", result2_xpath)
    assert result.text == "Блузы и рубашки"


def test_step3(site, field_xpath, result3_xpath):
    # поиск по ключевому слову keyword2
    input_keyword = site.find_field("xpath", field_xpath)
    input_keyword.send_keys(testdata['keyword2'])
    time.sleep(testdata['sleep_time'])
    input_keyword.send_keys(Keys.ENTER)
    time.sleep(100)
    site.find_field("xpath", """/html/body""").click()
    time.sleep(10)

    result = site.find_field("xpath", result3_xpath)
    assert "кофе" in result.text