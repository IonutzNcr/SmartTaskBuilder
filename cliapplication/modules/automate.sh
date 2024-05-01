#!/usr/bin/expect -f

# Set timeout for each command
set timeout 1

# Launch the Python application
spawn python3 App.py

# Expect the application to ask for a command
expect "Enter command:"

# Send the 'view' command and wait for the next prompt
send "view\r"
expect "Enter command:"

# Send the 'search' command with an argument
# send "search oth\r"
# expect "Enter command:"

send "filter category:other\r"
expect "Enter command:"

send "filter 'content:faire les courses'\r"
expect "Enter command:"

# Optional: Add more commands if needed
# send "anothercommand\r"
# expect "Enter command:"

# End the interaction with the application (assuming it can exit with 'exit')
send "exit\r"

# Wait for the process to finish
expect eof
