
  import re

#Validamos los mensajes de Syslog

txt = "The rain in Spain"
x = re.search("<(?'Priority'[0-9]{1,3})>(?'Date'[a-zA-Z]{1,3}\s(?(?=\s)\s|[0-9])[0-9])\s(?'Time'(?:[0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])\s(?'Host'(?(?=\d)(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)+)|\w+)\s(?'Message'.+$)
", txt)

if (x):
  print("SI! Coincide!")
else:
  print("No coincide")
