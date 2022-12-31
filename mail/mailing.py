from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
import json

import logging

# Info SendGrid
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
TEMPLATE_ID = os.environ.get('TEMPLATE_ID')
FROM_EMAIL = 'msereno@kyda.mx'
TO_EMAILS = [('msereno@exire.mx', 'Miguel Angel Sereno')]


# Logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# SendGrid
def send_report(summary):
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAILS)

    message.dynamic_template_data = {
        'report_date': summary.date_report,
        'transactions_month': summary.dict_trans_per_month,
        'average_debit_amount': summary.average_debit_amount,
        'average_credit_amount': summary.average_credit_amount,
        'total_balance': summary.balance
    }
    message.template_id = TEMPLATE_ID

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        logger.info(f'status_code: {response.status_code}')
    except Exception as e:
        logger.info(f'error {e.message}')
        print(e.message)
    return {
        'statusCode': 200,
        'body': json.dumps('OK Exchange!')
    }
