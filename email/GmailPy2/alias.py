primary_alias = None
aliases = gmail_service.users().settings().sendAs().\
    list(userId='me').execute()
for alias in aliases.get('sendAs'):
    if alias.get('isPrimary'):
        primary_alias = alias
        break

sendAsConfiguration = {
    'signature': 'I heart cats'
}
result = gmail_service.users().settings().sendAs().\
    patch(userId='me',
          sendAsEmail=primary_alias.get('sendAsEmail'),
          body=sendAsConfiguration).execute()
print 'Updated signature for: %s' % result.get('displayName')