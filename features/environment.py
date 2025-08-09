from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from selenium import webdriver
from application import Application

def before_scenario(context, scenario):
    bs_user = os.getenv("BROWSERSTACK_USERNAME")
    bs_key  = os.getenv("BROWSERSTACK_ACCESS_KEY")

    if bs_user and bs_key:
        caps = {
            "browserName": os.getenv("BS_BROWSER", "Chrome"),
            "browserVersion": os.getenv("BS_BROWSER_VERSION", "latest"),
            "bstack:options": {
                "os": os.getenv("BS_OS", "Windows"),
                "osVersion": os.getenv("BS_OS_VERSION", "11"),
                "buildName": os.getenv("BS_BUILD", "HW8-Behave"),
                "sessionName": scenario.name,
                "seleniumVersion": "4.20.0",
            }
        }
        url = f"https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub"
        context.driver = webdriver.Remote(command_executor=url, options=webdriver.ChromeOptions(), desired_capabilities=caps)
    else:
        # Local fallback
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        context.driver = webdriver.Chrome(options=options)

    context.driver.implicitly_wait(0)   # prefer explicit waits
    context.app = Application(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


def after_scenario(context, scenario):
    context.driver.quit()
