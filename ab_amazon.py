from behave import *
from selenium import webdriver
import time
import datetime

print("Start Timestamp: ", datetime.datetime.now())
@given(u'Launch Amazon on a browser')
def openAmazon(context):
    #context.driver = webdriver.Chrome(executable_path=r'drivers\chromedriver.exe')
    #context.driver = webdriver.Edge(executable_path=r'drivers\msedgedriver.exe')
    context.driver = webdriver.Firefox(executable_path=r'drivers\geckodriver.exe')
    context.driver.get("https://www.amazon.ca/")
    context.driver.maximize_window()
    time.sleep(2)
    print("Timestamp: ", datetime.datetime.now())
    context.driver.save_screenshot('1.png')

@when(u'Search using the keyword "Teddy bear"')
def searchKeyword(context):
    context.driver.find_element_by_id("twotabsearchtextbox").click()
    context.driver.find_element_by_id("twotabsearchtextbox").clear()
    context.driver.find_element_by_id("twotabsearchtextbox").send_keys("Teddy bear")
    context.driver.find_element_by_id("nav-search-submit-button").click()
    time.sleep(2)
    print("Timestamp: ", datetime.datetime.now())
    context.driver.save_screenshot('2.png')

@then(u'Sorts the result according to Customer Review')
def sortCReview(context):
    context.driver.find_element_by_id("a-autoid-0-announce").click()
    context.driver.find_element_by_id("s-result-sort-select_3").click()
    time.sleep(2)
    print("Timestamp: ", datetime.datetime.now())
    context.driver.save_screenshot('3.png')

@then(u'Selects the Age range between 5 to 7 years old')
def selectAge5(context):
    context.driver.find_element_by_xpath("//li[@id='p_n_age_range/6882176011']/span/a/div/label/i").click()
    time.sleep(2)
    print("Timestamp: ", datetime.datetime.now())
    context.driver.save_screenshot('4.png')

@then(u'Add first two products to cart')
def add2Product2cart(context):
    context.driver.find_element_by_xpath("//body/div[@id='a-page']/div[@id='search']/div[1]/div[1]/div[1]/span[3]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/a[1]/div[1]").click()
    time.sleep(2)
    context.driver.find_element_by_id("add-to-cart-button").click()
    time.sleep(2)
    context.driver.save_screenshot('5.png')
    context.driver.back()
    time.sleep(2)
    context.driver.back()
    time.sleep(2)
    context.driver.find_element_by_xpath(
        "//body/div[@id='a-page']/div[@id='search']/div[1]/div[1]/div[1]/span[3]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/a[1]/div[1]").click()
    time.sleep(2)
    context.driver.find_element_by_id("add-to-cart-button").click()
    time.sleep(2)
    print("Timestamp: ", datetime.datetime.now())
    context.driver.save_screenshot('6.png')

@then(u'Validate presence of those products to cart')
def validateCart(context):
    context.driver.find_element_by_xpath("//div[@id='nav-cart-text-container']/span[2]").click()
    time.sleep(2)
    print("Timestamp: ", datetime.datetime.now())
    context.driver.save_screenshot('7.png')
    try:
        cartStatus = context.driver.find_element_by_xpath("//span[@id='sc-subtotal-label-activecart']").text
        print(cartStatus)
    except:
        context.driver.delete_all_cookies()
        context.driver.close()
        assert False,"Test Failed"
    if cartStatus == "Subtotal (2 items):":
        context.driver.delete_all_cookies()
        context.driver.close()
        assert True,"Test Passed"
print("End Timestamp: ", datetime.datetime.now())
