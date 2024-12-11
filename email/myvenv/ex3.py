from __future__ import print_function
import argparse
import time
from time import strftime, localtime
import os

import base64
import os
import httplib2
from httplib2 import Http

from apiclient import errors
from apiclient import discovery

import oauth2client
from oauth2client import file, client, tools

SCOPES = 'https://mail.google.com'
CLIENT_SECRET_FILE = 'client_secret.json'
store = file.Storage('storage.json')
credentials = store.get()
if not credentials or credentials.invalid:
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    credentials = tools.run_flow(flow, store, flags)

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
        'gmail-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def send_message(service, user_id, message):
  """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
  try:
      message = (service.users().messages().send(userId=user_id, body=message)
                 .execute())
      print ('Message Id: %s' % message['id'])
      return message
  except errors.HttpError, error:
      print ('An error occurred: %s' % error)


def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    send_message(service, 'me','test message')


main()