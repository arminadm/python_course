#Armin Darabi Mahboub
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

def main():
    """using selenium and chrome driver to get to source page"""
    driver = Chrome(executable_path="chromedriver.exe")
    driver.get("https://google.com")
    search_bar = driver.find_element_by_name("q")
    search_bar.send_keys("کرونا")
    search_bar.send_keys(Keys.ENTER)
    
    """open text file to save headers"""
    with open("corona_google_headers.txt", "w", encoding="utf8") as f:

        """using loop to get all of header in first 10 pages"""
        header_counter = 1
        for page in range(10):
            next_page_button = driver.find_element_by_id("pnnext")

            """using beautifulsoup to get all of the headers"""
            soup = BeautifulSoup(driver.page_source)
            header_list = soup.find_all("h3", attrs={"class": "LC20lb MBeuO DKV0Md"})
            for header in header_list:
                f.write(f"{header.text} -{header_counter}")
                f.write("\n")
                header_counter += 1
            next_page_button.send_keys(Keys.ENTER)


if __name__ == "__main__":
    main()

