import json
   
json_data = '[{"Employee ID":1,"Name":"Abhishek","Designation":"Software Engineer"},' \
            '{"Employee ID":2,"Name":"Garima","Designation":"Email Marketing Specialist"}]'
   
json_object = json.loads(json_data)
   
# Indent keyword while dumping the
# data decides to what level 
# spaces the user wants.
# print(json.dumps(json_object, indent = 1))
   
# Difference in the spaces 
# near the brackets can be seen
print(json.dumps(json_object, indent = 3))