import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from datetime import date, timedelta
import smtplib
from email.message import EmailMessage
import ssl


session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# session.get(url), i changed rwquests in the next section to session
#Getting the data from dancity
response = session.get('https://dancitysub.com/api/data/',
                        headers={'Authorization': 'Token 7ff080fd8905c8bf17d67d86e1db0138f7bc2056'})

this_day = str(date.today())
data = response.json()
status = data["results"]
number = 0
dates =[]
for i in status:
    if i["create_date"].split("T") == this_day:
        print("True")
    number += 1
    dates.append(i["create_date"])

list_of_transactions_dates = []
for date in dates:
    list_of_transactions_dates. append ((date.split("T"))[0])


#
# for date in list_of_transactions_dates:
#     if date == this_day:
#         print (" True ")






# check for the split date per loop if it's equal to today's date then take the data value print true or something
print (list_of_transactions_dates)





print (dates)
print (status)