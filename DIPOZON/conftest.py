import pytest
import yaml
from site_ozon import SiteOzon

with open(r"C:\Users\user\Desktop\pythonProject1\DIPOZON\config.yaml") as f:
    testdata = yaml.safe_load(f)

@pytest.fixture()
def field_xpath():
    return """//*[@id="stickyHeader"]/div[2]/div/div/form/div[1]/div[2]/input[1]"""


@pytest.fixture()
def category_xpath():
    return """//*[@id="layoutPage"]/div[1]/header/div[2]/div/div/ul/li[3]/a"""


@pytest.fixture()
def subcategory_xpath():
    return """//*[@id="layoutPage"]/div[1]/div[2]/div[3]/div/div[1]/nav/ul/li[1]/a"""


@pytest.fixture()
def subsubcategory_xpath():
    return """//*[@id="layoutPage"]/div[1]/div[2]/div[3]/div/div[2]/div/div[1]/div[1]/div[1]/a[3]"""


@pytest.fixture()
def result1_xpath():
    return """//*[@id="layoutPage"]/div[1]/div[2]/div[2]/div[1]/div/aside/div[1]/div/div/div[5]/a"""

@pytest.fixture()
def result2_xpath():
    return """//*[@id="layoutPage"]/div[1]/div[2]/div[2]/div[1]/div/aside/div[1]/div/div/div[4]/a"""

@pytest.fixture()
def result3_xpath():
    return """//*[@id="paginatorContent"]/div/div/div[1]/div[1]/a/div/span"""
@pytest.fixture()
def site():
    my_site = SiteOzon(testdata["address"])
    # yield my_site
    # my_site.close_browser()