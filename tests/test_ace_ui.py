import os
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestAceUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--headless")
        cls.driver = webdriver.Firefox(options=options)
        cls.driver.implicitly_wait(5)
        cls.file_url = "file://" + os.path.abspath("ace.html")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_full_flow(self):
        d = self.driver
        d.get(self.file_url)

        # Step 1 - select gender
        gender_select = Select(d.find_element(By.ID, "gender"))
        gender_select.select_by_value("male")
        d.find_element(By.CSS_SELECTOR, 'button[onclick="nextStep()"]').click()

        # Step 2 - choose first trauma
        trauma_checkbox = WebDriverWait(d, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#traumaTypes input[type='checkbox']"))
        )
        trauma_checkbox.click()
        d.find_element(By.CSS_SELECTOR, 'button[onclick="processTraumaSelection()"]').click()

        # Step 2 -> 3 - fill occurrence for trauma
        age_checkbox = WebDriverWait(d, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#occurrence0 input[type='checkbox']"))
        )
        age_checkbox.click()
        Select(d.find_element(By.ID, "frequency0_0-2")).select_by_value("Once")
        Select(d.find_element(By.ID, "severity0_0-2")).select_by_value("Mild")
        d.find_element(By.CSS_SELECTOR, 'button[onclick="saveOccurrences(0)"]').click()

        # Step 3 - generate report
        WebDriverWait(d, 10).until(EC.visibility_of_element_located((By.ID, "step3")))
        d.find_element(By.CSS_SELECTOR, 'button[onclick="generateReport()"]').click()

        report = WebDriverWait(d, 10).until(
            EC.visibility_of_element_located((By.ID, "report"))
        )
        self.assertTrue(report.text.strip())


if __name__ == "__main__":
    unittest.main()
