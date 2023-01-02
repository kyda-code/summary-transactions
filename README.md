# Process Transactions

## Prerequisites
- Python >= 3.8
- Sendgrid => 6.9.7
- AWS Account
- Sqlite 3

## Description
This application consist of the following:

- Database package:  contains the repository for connection to SQLite 3
- File package:  contains the CSV file to process.
- Model package: models that contains the summary.
- Process package: contains the business rules to process each transaction.
- Util package: contains the class to read file.

The project contains a simple process class that saves a transactions in a database generate a summary and sent it via Sendgrid.
The challenge consists of completing as many of the following steps as possible:
- Save transaction and account info to a database
- Style the email and include logo company
- Package and run code on a cloud platform like AWS. Use AWS Lambda and S3 in lieu of Docker

Delivery and code requirements
Your project must meet these requirements:
- The summary email contains information on the total balance in the account, the number of
transactions grouped by month, and the average credit and average debit amounts grouped by
month. Using the transactions in the image above as an example, the summary info would be

- Total balance is 39.74
- Number of transactions in July: 2
- Number of transactions in August: 2
- Average debit amount: -15.38
- Average credit amount: 35.25 
- Include the file you create in CSV format. 
- Code is versioned in a git repository. The README.md file should describe the code interface and
instructions on how to execute the code

## Database
SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.

For more information:
https://www.sqlite.org/index.html

## Sendgrid
SendGrid delivers your transactional and marketing emails through the world's largest cloud-based email delivery platform. Send with confidence.

For more information:
https://sendgrid.com/

## Dynamic Template
SendGrid offers the creation of dynamic templates that can be configure to receive variables.

For more information:
https://docs.sendgrid.com/ui/sending-email/how-to-send-an-email-with-dynamic-templates

## Sendgrid Python 
Sendgrid offers an API for Python, is necessary before create an API Key.

For more information:
https://github.com/sendgrid/sendgrid-python

## Result 
When the summary is completed the process generates a report in HTML and send it, this 
an example for the final report.

![Summary](https://certifications-mass.s3.us-east-2.amazonaws.com/summary_report.png)



