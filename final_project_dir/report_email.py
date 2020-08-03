#! /usr/bin/env python3
import os
import datetime
import emails
import glob
import reports

files = glob.glob("/home/student-00-4094e4e9d9f9/supplier-data/descriptions/*.txt")
todays_date = datetime.date.today()
report_title = "Processed Update on {date}".format(date=todays_date)
text_block = ""

for file in files:
    with open(file, "r") as f:
        text = f.read().split("\n")
        paragraph = "Name: {}<br/> Weight: {}<br/><br/>".format(text[0], text[1])
        text_block = text_block + paragraph

if __name__ == "__main__":
    sender = "automation@example.com"
    recipient = "student-00-4094e4e9d9f9@example.com"
    subject = " Upload Completed - Online Fruit Store "
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attach_path = "/tmp/processed.pdf"

    reports.generate_report(attach_path, report_title, text_block)
    email_message = emails.generate_email(sender, recipient, subject, body, attach_path)
    emails.send_email(email_message)

