from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException, \
    ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import helpers as H
import time
import unittest

class Chrome_Acurity_brand(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_1_chrome_description_OUR_Mission(self):
        driver = self.driver
        driver.get(H.main_url)
        wait = WebDriverWait(driver, 10)
        print("__________________Positive_test____________"
              "Test 1 Verify that 'Media Links' works in footer")
        # Time delay from 1 - 3
        H.delay1_3()
        # Check API
        H.check_API(driver)
        # Check Title is correct and present on web page
        H.assert_title(driver, 'Acuity Brands | Lighting, Controls, and Building Management Solutions')
        # Verify that main logo is present on the page
        driver.find_element(By.XPATH, H.main_logo)
        # Close ads
        H.close_ad(driver)
        time.sleep(1)
        # move to footer
        actions = ActionChains(driver)
        footer = driver.find_element(By.XPATH, '//*[@href="https://www.facebook.com/acuitybrands"]')
        actions.move_to_element(footer).perform()
        # close privacy policy
        try:
            driver.find_element(By.ID, 'pi_tracking_opt_in_no').click()
            print("Privacy Policy was closed")
        except NoSuchElementException:
            print("No Privacy Policy")

        # Verify that "Facebook link" is present on the page
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@href="https://www.facebook.com/acuitybrands"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@href="https://www.facebook.com/acuitybrands"]')))
            # click on "Facebook link"
            driver.find_element(By.XPATH, '//*[@href="https://www.facebook.com/acuitybrands"]').click()
            time.sleep(2)
            # switch window and get photo on facebook page
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(1)
            # Get src from Facebook Page
            print(driver.find_element(By.XPATH,'//*[@mask="url(#jsc_c_2)"]//*[@preserveAspectRatio="xMidYMid slice"]'
                    ).get_attribute('xlink:href'), "Logo from Facebook Page")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(3)
        except TimeoutException:
            driver.get_screenshot_as_file("Facebook_error.png")
        # Verify that "Twitter link" is present on the page
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@href="https://twitter.com/acuitybrands"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@href="https://twitter.com/acuitybrands"]')))
            # click on "Twitter link"
            driver.find_element(By.XPATH, '//*[@href="https://twitter.com/acuitybrands"]').click()
            time.sleep(2)
            # switch window and get photo on Twitter page
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(1)
            # Get src from Twitter Page
            print(driver.find_element(By.XPATH, '//a[@href="/AcuityBrands/photo"]'
                                      ).get_attribute('href'), "Logo from Twitter Page")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(3)
        except TimeoutException:
            driver.get_screenshot_as_file("Twitter_error.png")

        # Verify that "LinkedIn link" is present on the page
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         '//*[@href="http://www.linkedin.com/company/acuitybrands"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   '//*[@href="http://www.linkedin.com/company/acuitybrands"]')))
            # click on "LinkedIn link"
            driver.find_element(By.XPATH, '//*[@href="http://www.linkedin.com/company/acuitybrands"]').click()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(3)
        except TimeoutException:
            driver.get_screenshot_as_file("LinkedIn_error.png")

        # Verify that "YouTube link" is present on the page
        try:
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//a[@href="http://www.youtube.com/user/acuitybrandsinc" and @title="YouTube"]')))
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//a[@href="http://www.youtube.com/user/acuitybrandsinc" and @title="YouTube"]')))
            # click on "YouTube link"
            driver.find_element(By.XPATH,
                                '//a[@href="http://www.youtube.com/user/acuitybrandsinc" and @title="YouTube"]').click()
            time.sleep(2)
            # switch window and get photo on YouTube page
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(1)
            # Get src from YouTube Page
            print(driver.find_element(By.ID, "img").get_attribute('src'), "Logo from YouTube Page")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(3)
        except TimeoutException:
            driver.get_screenshot_as_file("Youtube_error.png")

        # Verify that "Instagram link" is present on the page
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         '//a[@href="https://www.instagram.com/acuitybrands"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   '//a[@href="https://www.instagram.com/acuitybrands"]')))
            # click on "Instagram link"
            driver.find_element(By.XPATH, '//a[@href="https://www.instagram.com/acuitybrands"]').click()
            time.sleep(2)
            # switch window and get photo on Instagram page
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(1)
            # Get src from Instagram Page
            print(driver.find_element(By.XPATH,
                        '//*[@alt="acuitybrands\'s profile picture"]').get_attribute('src'), "Logo from Instagram Page")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(3)
        except TimeoutException:
            driver.get_screenshot_as_file("Instagram_error.png")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~Test is Passed~~~~~~~~~~~~~~~~~~~~~~~~"
              "~~~~~~~~All Media Links Works and Present on the Main page in the Footer~~~~~~~~~~~~")

    def test_2(self):
        driver = self.driver
        driver.get(H.main_url)
        wait = WebDriverWait(driver, 10)
        print("__________________Positive_test____________"
              "___________________Test 2 Verify 'ECLYPSE Connected Thermostat_______________")
        # Time delay from 1 - 3
        H.delay1_3()
        # Check API
        H.check_API(driver)
        # Check Title is correct and present on web page
        H.assert_title(driver, 'Acuity Brands | Lighting, Controls, and Building Management Solutions')
        # Verify that main logo is present on the page
        driver.find_element(By.XPATH, H.main_logo)
        # Close ads
        H.close_ad(driver)
        time.sleep(1)
        # move to footer
        footer = driver.find_element(By.XPATH, '//*[@class="row justify-content-center"]')
        actions = ActionChains(driver)
        actions.move_to_element(footer).perform()
        time.sleep(1)
        # verify that "Distech Controls" visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Distech Controls"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Distech Controls"]')))
        # Click on "Distech Controls"
        driver.find_element(By.XPATH, '//*[text()="Distech Controls"]').click()
        time.sleep(5)
        # switch tab
        driver.switch_to.window(driver.window_handles[1])
        # check title
        H.assert_title(driver, 'Distech Controls | Intelligent Building Solutions')
        # check logo on the main page
        wait.until(EC.visibility_of_element_located((By.XPATH, H.distech_logo)))
        # get src of video on the main page
        # if video is different get screenshot of it
        try:
            print(driver.find_element(By.XPATH, '//*[@class="hero__background-video"]').get_attribute('src'))
        except NoSuchElementException:
            print("Video is NOT present on the Main Page")
            driver.get_screenshot_as_file("Video_is_different.png")
        # verify that "Welcome to Distech Controls" is present and we on right page
        assert 'Welcome to Distech Controls' in driver.page_source
        # move to section "Latest News"
        latest_News = driver.find_element(By.XPATH,
                                          '//a[@href="/landing-pages/ecy-stat"]')
        actions = ActionChains(driver)
        actions.move_to_element(latest_News).perform()
        time.sleep(3)
        # discover section "Latest News" and get a photo
        print(driver.find_element(By.XPATH, '//*[@alt="Atrius"]').get_attribute('src'),
              "photo of 'Atrius Building Insights '")
        # Verify that button "Atrius Building Insights" is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH,
            '//*[@href="https://atrius.com/why-atrius/atrius-distech-building-management'
            '/?utm_source=distech&utm_medium=website&utm_campaign=distech_atrius_intro"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH,
            '//*[@href="https://atrius.com/why-atrius/atrius-distech-building-management'
            '/?utm_source=distech&utm_medium=website&utm_campaign=distech_atrius_intro"]')))
        # get a photo of "Smart Air Control Valve"
        print(driver.find_element(By.XPATH, '//*[@alt="Smart-Air-Control-Valve"]').get_attribute('src'),
              "photo of 'Smart Air Control Valve'")
        # Verify that button "Smart Air Control Valve" is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH,
            '//*[@href="https://atrius.com/why-atrius/atrius-distech-building-management/?utm_source=distech&utm'
            '_medium=website&utm_campaign=distech_atrius_intro"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH,
            '//*[@href="https://atrius.com/why-atrius/atrius-distech-building-management/?utm_source=distech&utm'
            '_medium=website&utm_campaign=distech_atrius_intro"]')))
        # move to element "ECLYPSE Connected Thermostat"
        # Use html for move down
        main_body = driver.find_element(By.XPATH, '//html')
        main_body.send_keys(Keys.SPACE)
        # verify that element is present on the page
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@alt="Eclypse-Connected-Thermostats"]')))
        # get src of photo
        print(driver.find_element(By.XPATH,
                                  '//*[@alt="Eclypse-Connected-Thermostats"]').get_attribute("src"), 'Thermostat')
        # verify that button "View Details" visible and clickable for "ECLYPSE Connected Thermostat"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@href="/landing-pages/ecy-stat"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@href="/landing-pages/ecy-stat"]')))
        # click on button
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".two-up:nth-child(8) button:nth-child(2) span:nth-child(1)").click()
        time.sleep(2)
        # check title
        H.assert_title(driver, 'ECY-Stat')
        # verify main logo
        wait.until(EC.visibility_of_element_located((By.XPATH, H.distech_logo)))
        # verify that video on background is present
        print(driver.find_element(By.XPATH, '//*[@class="hero__background-video"]').get_attribute('src'),
              "src of video on the main page")
        # move to element "google play"
        google_play = driver.find_element(By.XPATH, '//*[@alt="ECY STAT"]')
        actions.move_to_element(google_play).perform()
        # verify that "Apple Store" link is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@alt="AppStore"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@alt="AppStore"]')))
        # verify that "Google Play" link is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@alt="GooglePlay"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@alt="GooglePlay"]')))
        # move to "The Perfect Solution for:"
        perfect_solution = driver.find_element(By.XPATH, '//*[text()="What our customers say"]')
        actions.move_to_element(perfect_solution).perform()
        time.sleep(2)
        # Check elements in "The Perfect Solution for:" aria
        assert "Schools" in driver.page_source
        # verify that "Schools" present on the page and has src
        driver.find_element(By.XPATH, '//*[@alt="Schools"]').get_attribute('src')
        # check if user can open video for "Schools"
        driver.find_element(By.XPATH,
                            '//*[@href="https://www.youtube.com/watch?v=1y__JflseFE&forceBehavior=open"]').click()
        # wait for loading video
        time.sleep(5)
        # switch tab
        driver.switch_to.window(driver.window_handles[2])
        # then close window
        driver.close()
        # again switch window on main page
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        # verify that "Commercial Buildings" present on the page and has src
        driver.find_element(By.XPATH, '//*[@alt="Commercial Buidlings"]').get_attribute('src')
        # verify that "Hotels" present on the page and has src
        driver.find_element(By.XPATH, '//*[@alt="Hotels"]').get_attribute('src')
        # check if user can open video for "Hotels"
        driver.find_element(By.XPATH,
                            '//*[@href="https://www.youtube.com/watch?v=-QUQfQywH40&forceBehavior=open"]').click()
        # wait for loading video
        time.sleep(5)
        # switch tab
        driver.switch_to.window(driver.window_handles[2])
        # then close window
        driver.close()
        # again switch window on main page
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        # verify that "High-Rise Residential" on the page and has src
        driver.find_element(By.XPATH, '//*[@alt="Hi-Rise Residential"]').get_attribute('src')
        # verify that "Retail" on the page and has src
        driver.find_element(By.XPATH, '//*[@alt="retail_250x175"]').get_attribute('src')
        # check if user can open video for "Retail"
        driver.find_element(By.XPATH,
                            '//*[@href="https://www.youtube.com/watch?v=jDT80u7Es50&forceBehavior=open"]').click()
        time.sleep(5)
        # wait for loading video
        # switch tab
        driver.switch_to.window(driver.window_handles[2])
        # then close window
        driver.close()
        # again switch window on main page
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~Test is Passed~~~~~~~~~~~~~~~~~~~~~~~~"
              "~~~~~~~~User is able to go to the site and do verification 'ECLYPSE Connected Thermostat'~~~~~~~~~~~~")


    def test_3_add_product(self):
        driver = self.driver
        driver.get(H.main_url)
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)
        print("__________________Positive_test____________"
              "Test 3 add to cart 'Lithonia Lighting® Round Baffle LED' ")
        # Time delay from 1 - 3
        H.delay1_3()
        # Check API
        H.check_API(driver)
        # Check Title is correct and present on web page
        H.assert_title(driver, 'Acuity Brands | Lighting, Controls, and Building Management Solutions')
        # Verify that main logo is present on the
        driver.find_element(By.XPATH, H.main_logo)
        # Close ads
        H.close_ad(driver)
        time.sleep(1)
        # verify that button "Support" is visible anc clickable
        wait.until(EC.visibility_of_element_located((By.XPATH,
                            "//a[@class='has-sub-nav__desktop-link']//span[contains(text(),'Support')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,
                            "//a[@class='has-sub-nav__desktop-link']//span[contains(text(),'Support')]")))
        # click on button
        driver.find_element(By.XPATH,
                            "//a[@class='has-sub-nav__desktop-link']//span[contains(text(),'Support')]").click()
        time.sleep(1)
        # Verify title on Support page
        H.assert_title(driver, 'Support | Acuity Brands')
        # verify that button "How to Buy" is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@alt="support-how-to-buy-icons"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//img[@alt="support-how-to-buy-icons"]')))
        # click on button
        driver.find_element(By.XPATH, '//img[@alt="support-how-to-buy-icons"]').click()
        time.sleep(1)
        # verify that "How to Buy Lighting and Controls Products" present on the page
        assert "How to Buy Lighting and Controls Products" in driver.page_source
        # verify that logo is present on the page and get scr on photo
        print(driver.find_element(By.XPATH, '//img[@alt="Acuity-Brands-Logo-Green-306x44"]').get_attribute("src"))
        # verify that button "ACUITY Surplus Lighting" is present and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@href="#surplusAnchor"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@href="#surplusAnchor"]')))
        # click on the button
        driver.find_element(By.XPATH, '//a[@href="#surplusAnchor"]').click()
        # verify photo on "ACUITY Surplus Lighting" section and get photo
        print(driver.find_element(By.XPATH, '//*[@alt="Acuity-Surplus-LeftRight-700x400"]').get_attribute("src"))
        # verify that button "Buy Now!" is present and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="with-arrow"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="with-arrow"]')))
        # click on the button
        driver.find_element(By.XPATH, '//*[@class="with-arrow"]').click()
        # verify title on "Surplus Lighting"
        H.assert_title(driver, 'Surplus Lighting | Acuity Brands')
        # verify that "SURPLUS LIGHTING" is present on the page
        assert 'SURPLUS LIGHTING' in driver.page_source
        # switch frame to get access for "products"
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@name='frame-productSet-212924235929']"))
        # Scroll till the products
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH,
                                                '//img[@alt="Lithonia Lighting® Round Baffle LED Remodel Kit"]'))
        time.sleep(2)
        # verify that product "Lithonia Lighting" is present and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     '//img[@alt="Lithonia Lighting® Round Baffle LED Remodel Kit"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     '//img[@alt="Lithonia Lighting® Round Baffle LED Remodel Kit"]')))
        # get photo of the product
        print(driver.find_element(By.XPATH, '//img[@alt="Lithonia Lighting® Round Baffle LED Remodel Kit"]'
                                  ).get_attribute("src"), "took a photo of the product")
        # click on the product
        # also additional, it was hard to find locators, and I've been used selenium IDE
        driver.find_element(By.CSS_SELECTOR, ".has-image:nth-child(1) .shopify-buy__btn").click()
        time.sleep(1)
        # verify again that product is right and correct
        driver.find_element(By.XPATH, '//img[@alt="Lithonia Lighting® Round Baffle LED Remodel Kit"]'
                            ).get_attribute("src")
        time.sleep(1)
        # switch frame
        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[contains(@name,'frame-modal')]"))
        # change from 3 to 5 size
        # verify that element is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="shopify-buy__option-select__select"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="shopify-buy__option-select__select"]')))
        # click on "placeholder". "it works without this step"
        driver.find_element(By.XPATH, '//*[@class="shopify-buy__option-select__select"]').click()
        # choose "4" size
        driver.find_element(By.XPATH, '//*[@class="shopify-buy__option-select__select"]').send_keys(Keys.ARROW_DOWN)
        # choose "5" size
        driver.find_element(By.XPATH, '//*[@class="shopify-buy__option-select__select"]').send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        # then choose quantity for this time i wanna 2 piece of this product
        # placeholder is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@type="number"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@type="number"]')))
        # clear field for input
        driver.find_element(By.XPATH, '//*[@type="number"]').clear()
        # choose 2 quantity
        driver.find_element(By.XPATH, '//*[@type="number"]').send_keys(2)
        time.sleep(1)
        # add to Cart
        driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]").click()
        time.sleep(1)
        # switch to cart iframe
        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@name='frame-cart']"))
        # verify that price is correct
        wait.until(EC.visibility_of_element_located((By.XPATH,
                            '//*[@class="shopify-buy__cart-item__price" and text()="$41.54"]')))
        # verify that name of product is correct
        wait.until(EC.visibility_of_element_located((By.XPATH,
          '//*[@class="shopify-buy__cart-item__title" and text()="Lithonia Lighting® Round Baffle LED Remodel Kit"]')))
        # Verify that button "Checkout" is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Checkout"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Checkout"]')))
        # click on button "Checkout"
        driver.find_element(By.XPATH, '//*[text()="Checkout"]').click()
        time.sleep(5)
        # change tab for child window
        p = driver.current_window_handle
        # get first child window
        chwd = driver.window_handles
        for w in chwd:
            # switch focus to child window
            if (w != p):
                driver.switch_to.window(w)
        # Check title on "Checkout" page
        H.assert_title(driver, 'Information - Acuity Brands Lighting - Checkout')
        # Use POM for payment
        H.payment(driver)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~Test is Passed~~~~~~~~~~~~~~~~~~~~~~~~"
              "~~~~~~~~~Use is Able to Choose Product Change quantity, size and add information~~~~~~~~~~~~~~~ ")

        time.sleep(4)

    def test_4_Search_field(self):
        driver = self.driver
        driver.get(H.main_url)
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)
        print("__________________Positive_test____________"
              "Test 4 verify that 'Search field works' Enter value 'Contact US'  ")
        # Time delay from 1 to 3
        H.delay1_3()
        # Check API
        H.check_API(driver)
        # Check Title is correct and present on web page
        H.assert_title(driver, 'Acuity Brands | Lighting, Controls, and Building Management Solutions')
        # Verify that main logo is present on the
        driver.find_element(By.XPATH, H.main_logo)
        # Close ads
        H.close_ad(driver)
        time.sleep(1)
        # Use POM for verify "Search Field"
        H.search_field(driver)
        # Enter Value "Contact Us"
        driver.find_element(By.XPATH, '//*[@title="Enter keywords to search"]').send_keys("Contact Us")
        driver.find_element(By.XPATH, '//*[@title="Enter keywords to search"]').send_keys(Keys.ENTER)
        time.sleep(1)
        # Check if the search result matches
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     '//h1[text()="Search Results:"]//span[text()="CONTACT US"]')))
        # get scr of the photo
        print(driver.find_element(By.XPATH,
                                  '//img[@src="-/media/3cd82c6432de4575b74b4aa58b0d1be5.ashx"]').get_attribute("src"))
        assert 'Contact us if you need more information.' \
               ' Our lighting and controls products are primarily' in driver.page_source
        # Verify that button "Contact Us" is present on the page
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[text()="Contact Us"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Contact Us"]')))
        # click on button "Contact Us"
        driver.find_element(By.XPATH, '//a[text()="Contact Us"]').click()
        time.sleep(2)
        # check title
        H.assert_title(driver, 'Contact Us | Acuity Brands')
        # Contact Us is present on the page
        assert 'Contact Us' in driver.page_source
        # verify that "Corporate Headquarters" is present and number visible
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Acuity Brands Lighting"]')))
        assert '1-800-922-9641' in driver.page_source
        # verify that "Acuity Brands Lighting" is present and number visible
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Corporate Headquarters"]')))
        assert '770-922-9000' in driver.page_source
        # switch frame
        driver.switch_to.frame(0)
        # Verify that "Technical Support" visible and clickable
        wait.until(EC.visibility_of_element_located((By.ID, '616d96d327dab')))
        wait.until(EC.element_to_be_clickable((By.ID, '616d96d327dab')))
        # click on "Technical Support"
        driver.find_element(By.ID, "616d96d327dab").click()
        time.sleep(2)
        # change tab
        window_before = driver.window_handles[0]
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(5)
        # Check title
        H.assert_title(driver, 'Technical Support | Acuity Brands')
        # verify that "Technical Support and Controls Services" is visible
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Technical Support and Controls Services"]')))
        # get photo of icon "Contact Technical Support"
        print(driver.find_element(By.XPATH,
                    '//*[@alt="tech-support-contact-information"]').get_attribute('scr'),
              'photo of icon "Contact Technical Support')
        # verify "Contact Technical Support" is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Contact Technical Support"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Contact Technical Support"]')))
        # Click on "Contact Technical Support"
        driver.find_element(By.XPATH, '//*[text()="Contact Technical Support"]').click()
        time.sleep(2)
        assert "Technical Support Contact Information" in driver.page_source
        # check if "Architectural Brands" is present on the page
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     '//span[text()="Architectural Brands: (800) 705-7378"]')))
        # check if "Commercial Lighting" is present on the page
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[text()="Commercial Lighting: (800) 705-7378"]')))
        # check if "Controls" is present on the page
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[text()="Controls: (800) 535-2465"]')))
        time.sleep(1)
        driver.close()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~Test is Passed~~~~~~~~~~~~~~~~~~~~~~~~"
              "~~~~~~~~~Use is Able to Enter 'Contact US' and get information~~~~~~~~~~~~~~~ ")

    def tearDown(self):
        self.driver.quit()












