from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
LISTINGS = (By.CSS_SELECTOR, "[data-test*='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')

@then('Verify search results shown for {product}')
def verify_search_results_shown(context, product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-tests='resultsHeading']").text
    assert product in actual_result, f'Expected text {product} not in actual {actual_result}'


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
     # context.driver.find_elements(By.CSS_SELECTOR, "[id*='addToCartButton']")[0].click()
     # context.driver.wait.until(EC.visibility_of_element_located(ADD_TO_CART_SIDE_NAV_BTN))

@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')

@when('Confirm Add to Cart buttong from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_SIDE_NAV_BTN)).click()
    # context.driver.find_element(*ADD_TO_CART_SIDE_NAV_BTN)
    sleep(4)


#@then('Verify that every product has a name and an image')
#def verify_products_name_ing(context):
 #   context.driver.execute_script("window.scrollBy(0,2000)","")
  #  sleep(4)
   # context.driver.execute_script("window.scrollBy(0,2000)","")

   # all_products = context.driver_find_elements(+LISTINGS)
   # print(all_products)
   # assert len(all_products) > 0, 'No products found'

   # for product in all_products:
    #    title = product.find.element(*PRODUCT_TITLE).text
     #   assert title != '', 'Product title not shown'
      #  print(title)
       # product.find_element(*PRODUCT_IMG)

