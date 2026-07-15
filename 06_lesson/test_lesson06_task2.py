from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()

    cookie_user1 = {
        "name": "SESSION",
        "value": "OWVmZmYyZmYtNThlZi00MjVmLTkwNWMtN2ViNTJkNWVhODhk",
        "domain": ".gitflic.ru",
        "path": "/",
    }

    cookie_user2 = {
        "name": "SESSION",
        "value": "ZTE5NzZmNDItZmU5Mi00NmE2LTg2NzUtMDFlN2EzZjU0ZWFi",
        "domain": ".gitflic.ru",
        "path": "/",
    }

    driver.get("https://gitflic.ru")

    driver.add_cookie(cookie_user1)
    driver.refresh()

    driver.get("https://gitflic.ru/user/test_lesson_06")
    url_user1 = driver.current_url

    driver.delete_all_cookies()

    driver.get("https://gitflic.ru")

    driver.add_cookie(cookie_user2)
    driver.refresh()

    driver.get("https://gitflic.ru/user/test_lesson_06_2")
    url_user2 = driver.current_url

    assert url_user1 != url_user2

    driver.quit()
