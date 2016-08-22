usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username_attempt = input("Please emter username: ")
if username_attempt in usernames:
    print("Access granted")
else:
    print("Access denied")