import requests
from ddt import data
from testpage import OperationsHelper
from selenium import webdriver
import logging
import yaml
import time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    name = testdata["username"]
    passwd = testdata["password"]


def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.enter_login(name)
    testpage.enter_pass(passwd)
    testpage.click_login_button()
    assert testpage.get_user_text() == f"Hello, {name}"


def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)
    testpage.click_new_post_btn()
    testpage.enter_title("testtitle")
    testpage.enter_content("testcontent")
    testpage.enter_description("testdesc")
    testpage.click_save_btn()
    time.sleep(2)
    assert testpage.get_res_text() == "testtitle"


def test_step4(browser):
    logging.info("Test4 Starting")
    testpage = OperationsHelper(browser)
    testpage.click_contact_link()
    time.sleep(2)
    testpage.enter_contact_name("testname")
    testpage.enter_contact_email("testemail@testemail.com")
    testpage.enter_contact_content("testmessage")
    time.sleep(2)
    testpage.click_contact_send_button() == "Form successfully submitted"

def test_step5(login, testtext1):
    header = {"X-Auth-Token": login}
    res = requests.get(data["address"]+"api/posts", params={"owner":"notMe"}, headers=header)
    listres = [i["title"] for i in res.json()["data"]]
    assert testtext1 in listres


def test_step6(create_post):
    post_id = create_post
    # Проверка наличия созданного поста по его описанию
    description = "Тестовое описание нового поста"
    response = requests.get("https://test-stand.gb.ru/api/posts", params={"description": description})
    assert response.status_code == 200
    posts = response.json()
    assert any(post["id"] == post_id for post in posts)