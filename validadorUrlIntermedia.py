

  import re

#Validamos las urls con http contenidas en un logs

txt = "The rain in Spain"
x = re.search("(?<=https:\/\/strm.yandex.ru\/kal\/)(.*?)(?=\/)", txt)

if (x):
  print("SI! Coincide!")
else:
  print("No coincide")
  
  # "content_url": "https://strm.yandex.ru/kal/probusiness_cv_supres/probusiness_cv_supres0.m3u8?from=unknown&partner_id=188262&target_ref=https%3A//yastatic.net&uuid=42b7c9a63d2c656ab5dc8c5ec0934d6f&video_category_id=1017
  # Como vemos estamos haciendo que arroje la informacion que esta despues del https://strm.yandex.ru/kal/   hasta el proximo /.
