#Using Variables in Strings
first_name = "Ava"
last_name = "Lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

#Using title in the String
first_name = "ava"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

#Adding full name to the variable and displaying
first_name = "Ava"
last_name = "Lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

#Adding Whitespace to Strings with Tabs or Newlines
print("Python") #w/o Whitespace
print("\tPython") #w Whitespace

#Adding Newlines
print("Languages:\nPython\nC\nJavaScript")

#Using Whitespace and newlines together
print("Languages:\n\tPython\n\tC\n\tJavascript")

#Stripping Whitespaces DID NOT WORK
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
