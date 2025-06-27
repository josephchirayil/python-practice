#! python3

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6', 'blog': 'VmALvQyKAxiVH5GI8v01if1MLZFEsdt', 'luggage': '12345'}

import sys

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
        
account = sys.argv[1]  # first commnd line arg is account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
