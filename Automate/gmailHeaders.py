#!/usr/bin/env python

import sys
import imaplib
import getpass
import email
import datetime

M = imaplib.IMAP4_SSL('imap.gmail.com')

try:
	M.login('kggiorno@gmail.com', getpass.getpass())
except impalib.IMAP4.error:
	print("LOGIN FAILED!!! ")
	# ... exit or deal with failure...

rv, mailboxes = M.list()
if rv == 'OK':
	print("Mailboxes:")
	print(mailboxes)

rv, data = M.select("TNabbed Docs")
if rv == 'OK':
	print('Processing mailbox...\n')
	process_mailbox(M) # ... do something with emails, see below ...
	M.close()
M.logout()

