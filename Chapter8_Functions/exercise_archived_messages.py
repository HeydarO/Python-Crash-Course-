"""
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
function send_messages() with a copy of the list of messages. After calling the
function, print both of your lists to show that the original list has retained its
messages.
"""

text_messages = [
'Hello Heydar',
'How was your day, ma man?',
'Are you doing ok?'
]
sent_messages = []

def send_messages(text_messages, sent_messages):
    while text_messages:
        message = text_messages.pop()
        print(message)
        sent_messages.append(message)

send_messages(text_messages[:], sent_messages)

print(sent_messages)
print(text_messages)
