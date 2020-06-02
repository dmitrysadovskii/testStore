class JsonHelper:

    def update_json(self, json_data, **kwargs):
        for key, value in kwargs.items():
            if key in json_data and value is not None:
                json_data[key] = value
        return json_data

# data = {
#   "id": 0,
#   "category": {
#     "id": 0,
#     "name": "string"
#   },
#   "name": "dog",
#   "photoUrls": [x     D
#     "string"
#   ],
#   "tags": [
#   {
#     "id": 0,
#     "name": "string"
#   }
#   ],
#   "status": "status"
#   }
#
# a = JsonHelper().update_json(data, id=1, name='Dima')
# print(a)