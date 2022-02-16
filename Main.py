import Booker
import time
import json 
import sys

# load parameter from file
with open('config.json','r', encoding='utf-8') as f:
    config = json.load(f)

# Create booker object
booker = Booker.Booker(config["id"],
    config["checksum"],
    config["zh_surname"],
    config["zh_name"],
    config["tel"],
    config["districts"],
    config["date"]
)

# Main flow
booker.browse()
booker.fill_id()
time.sleep(2)
booker.consent()
time.sleep(2)
booker.fill_PI()

success = False
while not success:
    success = booker.select_timeslot()

# booker.submit()

# except:
#     print('error occured, program exit')
#     sys.exit()