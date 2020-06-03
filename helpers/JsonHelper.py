class JsonHelper:

    def update_json(self, json_data, **kwargs):
        for key, value in kwargs.items():
            if key in json_data and value is not None:
                json_data[key] = value
        return json_data
