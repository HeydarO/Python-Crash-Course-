glossary = {
'append:': "function that's add new item to the list",
'del:': 'function that deletes item in the list',
'lower:': 'function that changes all of the characters to the lowercase',
'items:': 'function that enables assigning of keys and values to the variables in the loop',
'keys:': 'function that enables assigning of keys to the variable in the loop',
'values:': 'function that enables assigning of values to the variable in the loop',
}

for word, descr in glossary.items():
    print(f"{word.title()} {descr.title()}.")
