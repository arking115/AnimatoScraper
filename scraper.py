import pandas as pd
import re
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def process_views(self, elements):
        views = []
        element_texts = [self.driver.execute_script("return arguments[0].outerHTML;", element) for element in elements]
        for element_text in element_texts:
            view_element = re.search(r'(\d+(?:\.\d+)?[K|M] views)', element_text)
            if view_element:
                views.append(view_element.group())
        return views
            
    def scroll(self):
        previous_position = None
        
        while True:
            time.sleep(1)
            self.driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
            
            current_position = self.driver.execute_script("return window.pageYOffset;")
            
            if current_position == previous_position:
                break
            
            previous_position = current_position
    
    def get_views(self):
        try:
            video_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='tabsContent']/tp-yt-paper-tab[2]/div/div[1]"))
            )
            video_button.click()

            self.scroll()
            
            # Wait for the videos section to load
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "metadata-line")))
            
            # Find all elements that represent video items in the videos section
            elements = self.driver.find_elements(By.ID, "metadata-line")
            print(self.process_views(elements))
        except Exception as e:
            print("Error occurred while fetching views", str(e))

    def get_yt_info(self, video_link):
        self.driver.get(video_link)
        self.get_views()

dawg = Scraper()
dawg.get_yt_info("https://www.youtube.com/c/3blue1brown")