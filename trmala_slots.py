from selenium import webdriver 
import webcolors
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options 
import datetime 
from datetime import date
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

today = date.today()
current_date = int(today.strftime("%d"))
current_month_name = today.strftime("%B")
current_month_number = int(today.strftime("%m"))

if current_month_number == 12:
    next_month_number = 1
else:
    next_month_number = current_month_number + 1
datetime_object = datetime.datetime.strptime(str(next_month_number), "%m")
next_month_name = datetime_object.strftime("%B")

month_lists = [current_month_name, next_month_name]

cal_list = []
current_ticket_list = []
next_ticket_list = []
  
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://tirupatibalaji.ap.gov.in') 
sleep(1) 

driver.find_element_by_partial_link_text('Special').click()
sleep(1)

driver.find_element_by_name('accept').click()
driver.find_element_by_xpath("//span/button[text()='Agreed']").click()

current_list = driver.find_elements_by_xpath("//span[contains(text(),'{}')]//parent::div/parent::calendar/div".format(month_lists[0]))
next_list = driver.find_elements_by_xpath("//span[contains(text(),'{}')]//parent::div/parent::calendar/div".format(month_lists[1]))

#rgba(121, 193, 57, 1) -- green
#rgba(255, 30, 34, 1) -- red
for x in range(len(current_list)):
    all_options = current_list[x].find_elements_by_tag_name("span")
    for option in all_options:
        if 'rgba(121, 193, 57, 1)' == option.value_of_css_property('background-color'):
            current_ticket_list.append(option.text)
            
for x in range(len(next_list)):
    all_options = next_list[x].find_elements_by_tag_name("span")
    for option in all_options:
        if 'rgba(121, 193, 57, 1)' == option.value_of_css_property('background-color'):
            next_ticket_list.append(option.text)

if len(current_ticket_list) < 1:
    text_message_1 = "No Tickets are opened yet for the month of {}".format(current_month_name)
else:    
    text_message_1 = "Tickets are avilable for the {} month below dates {}".format(current_month_name, current_ticket_list)
    
if len(next_ticket_list) < 1:
    text_message_2 = "No Tickets are opened yet for the month of {}".format(next_month_name)
else:
    text_message_2 = "Tickets are avilable for the {} month below dates {}".format(next_month_name, next_ticket_list)

message = client.messages.create(
    to="", #your registered mobile number in twillio
    from_="", #number created from twillio
    body=text_message_1 + text_message_2)

input('Press anything to quit') 
driver.quit() 
print("Finished") 
