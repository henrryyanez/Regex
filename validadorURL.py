  import re

#Validamos las urls con http contenidas en un logs

txt = "The rain in Spain"
x = re.search("http:\/\/(www\.[a-z0-9]+([\-\.][a-z0-9]+)*\.[a-z]{2,5})(:[0-9]{1,5})?(\/.*)?$|^(\/.*)", txt)

if (x):
  print("SI! Coincide!")
else:
  print("No coincide")
