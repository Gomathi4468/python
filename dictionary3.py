#nested dictionary
choc={"diarymilk":{"quantity":5,"Price":10},
      "Kitkat":{"quantity":9,"Price":12},
      "Munch":{"qunantity":8,"Price":12}}
print(choc.keys())
print(choc['diarymilk'])
print(choc['diarymilk'].keys())
print(choc['diarymilk'].values())
print(choc['diarymilk'].items())
for x in choc.keys():
    print(x)
