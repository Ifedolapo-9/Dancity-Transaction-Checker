import requests
from datetime import date, timedelta
import smtplib
from email.message import EmailMessage
import ssl

response = requests.get('https://dancitysub.com/api/data/',
                        headers={'Authorization': 'Token 7ff080fd8905c8bf17d67d86e1db0138f7bc2056'})

data = response.json()
status = data["results"]

today = date.today()
today = (str(today))
yesterday = str(date.today() - timedelta(days=1))

text = "Today's transactions are/is:\n"
failed_transaction = "Thus, today's failed transactions are/is:\n"
yesterday_text = "Yesterday's transactions are/is:\n"
failed_transaction_yesterday = "Thus, yesterday's failed transactions are/is:\n"

for i in status:
    if i["create_date"][:10] == today:
        text += f"The status of {i['mobile_number']} is {i['Status']} \n "
        if i["Status"] == "failed":
            failed_transaction += f"The failed transactions are {i['mobile_number']} \n"

    if i["create_date"][:10] == yesterday:
        yesterday_text += f"The status of {i['mobile_number']} is {i['Status']} \n"
        if i["Status"] == "failed":
            failed_transaction_yesterday += f"The failed transactions are {i['mobile_number']} \n"

final_text_today = f"{text} \n {failed_transaction}"
final_text_yesterday = f"{yesterday_text} \n {failed_transaction_yesterday}"

print(final_text_today)
print(final_text_yesterday)

#Sending transaction updates to email

email_receiver = "ifedolapoojow@gmail.com"
my_email = "ifedolapo387@gmail.com"
pass_word = "tcpzblyhdoasdrzs"
subject = "Transaction Update"
body = f"{final_text_today} \n {final_text_yesterday}"

en = EmailMessage()
en["from"] = my_email
en["To"] = email_receiver
en["Subject"] = subject
en.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(user=my_email, password=pass_word)
    smtp.sendmail(my_email, email_receiver, en.as_string())