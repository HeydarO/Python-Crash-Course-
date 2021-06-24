rivers = {
'Hungary': 'Danube',
'Germany': 'Danube',
'Serbia': 'Danube',
'Croatia': 'Danube',
'Austria': 'Danube',
'Slovakia': 'Danube',
'Romania': 'Danube',
'Moldova': 'Danube',
'Ukraine': 'Danube',
'Bulgaria': 'Danube',
'France': 'Loire',
'Germany': 'Elbe',
'Czech': 'Elbe',
'Switzerland': 'Rhine',
'Netherlands': 'Rhine',
'Russia': 'Volga',
}

for country in set(rivers.keys()):
    print(country)

###
for river in set(rivers.values()):
    print(river)

###
for country, river in rivers.items():
    print(f"{river} is flowing over {country}.")
