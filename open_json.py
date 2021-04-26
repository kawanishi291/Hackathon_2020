import json

json_open = open('/sample.json', 'r')
json_load = json.load(json_open)
genre = "Afghan Hound"


for num in list(json_load.keys()):
  if num == '0':
    all_obj = json_load[num]

for obj_name in all_obj.keys():
  if obj_name == genre:
     list_2 = all_obj[obj_name]



print(list_2)