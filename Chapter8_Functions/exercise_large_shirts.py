def make_shirt(size, message):
    if size == 'L':
        message = "\nI love Python."
        print(message)
    elif size == 'M':
        print(f"\n{message}.")
    else:
        print(f"\nMan, you are wearing small?!?!")

make_shirt('L', 'Failing is learning')
make_shirt('M', 'Head full of Dreams')
make_shirt('S', 'What will you do?')
