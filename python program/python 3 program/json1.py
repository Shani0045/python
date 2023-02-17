import json
data='''{
"a":"shani",
"b":"amit"}
'''
parsed=json.loads(data)
print(parsed["a"])
print(type(parsed))
