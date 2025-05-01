from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



def test_login():
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  driver.get("https://editor-staging.storydoc.com/login")

  login_page = LoginPage(driver)
  login_page.enter_username("team@qa.com")
  login_page.enter_password("team_account")
  login_page.click_submit()

  assert login_page.is_login_successful(), "Login failed"

  # Additional assertions for other elements or page content
  # ...

  driver.quit()


if __name__ == "__main__":
  test_login()