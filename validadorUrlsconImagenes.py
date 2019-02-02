  import re

#Validamos las urls con http contenidas en un logs

txt = "The rain in Spain"
x = re.search("(.*)([\/](\w+))(\.(jpg|png|gif|jpeg))", txt)

if (x):
  print("SI! Coincide!")
else:
  print("No coincide")
