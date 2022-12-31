from datetime import datetime
from mail import mailing
from model.summary import Summary
from datetime import datetime as dt


def get_summary(data):
    s = Summary(
        total_balance(data),
        transactions_per_month(data),
        average_debit_amount(data),
        average_credit_amount(data),
        dt.now().strftime("%A, %B %d, %Y %I:%M %p")
    )
    mailing.send_report(s)


def total_balance(data):
    # Initialize variables
    balance = 0.0
    for x in data:
        balance += float(x[2])

    return balance


def transactions_per_month(data):
    # Initialize dictionary
    dict_months = {}
    value = ""

    # Debit operations
    for x in data:
        # Parse date
        date_time = datetime.strptime(x[1], '%m/%d')
        month = date_time.strftime('%B')
        if month in dict_months:
            count = dict_months.get(month)
            count += 1
            dict_months.update({month: count})
        else:
            dict_months[month] = 1

    for x in dict_months:
        value += x + ": " + str(dict_months[x])
        value += "<br>"

    return value


def average_debit_amount(data):
    # Initialize variables
    operations = 0
    balance = 0.0

    # Debit operations
    for x in data:
        if float(x[2]) < 0:
            balance += float(x[2])
            operations += 1

    return balance/operations


def average_credit_amount(data):
    # Initialize variables
    operations = 0
    balance = 0.0

    # Credit operations
    for x in data:
        if float(x[2]) > 0:
            balance += float(x[2])
            operations += 1

    return balance/operations

