from selenium import webdriver
import time

class Booker():
    
    def __init__(self, id, checksum, zh_surname, zh_name, tel, districts, date):
        self.driver = webdriver.Chrome('Tools/chromedriver.exe')
        self.id = id
        self.checksum = checksum
        self.zh_surname = zh_surname
        self.zh_name = zh_name
        self.tel = tel
        self.districts = districts
        self.date = date

    # open url 
    def browse(self, url='https://booking.communitytest.gov.hk/form/index_tc.jsp'):
        self.driver.get(url)

    # step 1
    def fill_id(self):
        self.driver.find_element_by_id('step_1_documentId_HKIC_prefix').send_keys(self.id)
        self.driver.find_element_by_id('step_1_documentId_HKIC_check_digit').send_keys(self.checksum)
        self.driver.find_element_by_xpath("//input[@value='開始預約']").click()

    # step 2
    def consent(self):
        self.driver.find_element_by_xpath('//span[@class="ckbox-checkmark"]').click()
        self.driver.find_element_by_id('note_2_confirm').click()
    
    # step 3
    def fill_PI(self):
        self.driver.find_element_by_id('step_2_language_preference_chinese').click()
        self.driver.find_element_by_id('step_2_surname').send_keys(self.zh_surname)
        self.driver.find_element_by_id('step_2_givenname').send_keys(self.zh_name)
        self.driver.find_element_by_id('step_2_tel_for_sms_notif').send_keys(self.tel)
        self.driver.find_element_by_id('step_2_tel_for_sms_notif_confirm').send_keys(self.tel)
        self.driver.find_element_by_id('step_2_travel_info_no').click()

    # Step 4: select the prefered testing center and date in list order
    def select_timeslot(self):
        # list districts
        for l in self.districts:
            path = '//*[@id="step_2_district"]/option[@value="{}"]'.format(l)
            self.driver.find_element_by_xpath(path).click()
            
            # list centers
            centers = self.driver.find_elements_by_xpath('//*[@id="step_2_center"]/option')
            for c in centers:
                if c.is_enabled():
                    c.click()
                    
                    # ensure the timeslot is retrieved
                    if self.driver.find_element_by_xpath('//*[@class="list_timeslot"]/li').is_displayed():
                        # list time
                        for d in self.date:
                            path = '//*[@id="collapse{}"]'.format(d)
                            timeslot = self.driver.find_elements_by_xpath(path+'/div/input')

                            # expand the timeslot
                            if d >= 3:
                                self.driver.find_element_by_xpath(path+'/..').click()

                            # check the nearest time
                            for t in timeslot:
                                if t.is_enabled():
                                    t.click()
                                    return True

        return False
    
    # Step 5
    def submit(self):
        self.driver.find_element_by_id('step_2_form_control_confirm').click()
        if self.driver.find_element_by_xpath('//*[@id="step_2_form_control"]/div[1]/input').is_displayed():
            self.driver.find_element_by_xpath('//*[@id="step_2_form_control"]/div[1]/input').click()



# if __name__ == '__main__':
#     booker = Booker()
#     booker.browse()
#     time.sleep(1)
#     booker.fill_id()
#     time.sleep(1)
#     booker.consent()
#     time.sleep(1)
#     booker.fill_PI()
#     time.sleep(1)
#     booker.select_timeslot()

    #<li class="validate_msg">你選擇的時段預約已滿。</li>