from human import Human


class ToJSON:

    def __num_to_json(self, obj):
        return str(obj)

    def __string_to_json(self, obj):
        return '"{}"'.format(obj)

    def __bool_to_json(self, obj):
        return "true" if obj else "false"

    def __none_to_json(self, obj):
        return "null"

    def __list_to_json(self, obj):
        return "[{}]".format(", ".join(self.dumps(item) for item in obj))

    def __dict_to_json(self, obj):
        return "{{{}}}".format(
            ", ".join("{}: {}".format(self.dumps(key), self.dumps(value)) for key, value in obj.items()))

    def __custom_to_json(self, obj):
        obj_attr_s = dict()
        obj_attr_s.update(obj.__dict__)
        obj_attr_s.update(obj.__class__.__dict__)
        attrs_updated = dict()
        for key, value in obj_attr_s.items():
            if key.startswith('_'):
                continue
            attrs_updated[key] = value if not hasattr(value, '__dict__') else self.__custom_to_json(value)
        return self.__dict_to_json(attrs_updated)

    def dumps(self, obj):
        if isinstance(obj, bool):
            return self.__bool_to_json(obj)
        elif isinstance(obj, (int, float)):
            return self.__num_to_json(obj)
        elif isinstance(obj, str):
            return self.__string_to_json(obj)
        elif isinstance(obj, type(None)):
            return self.__none_to_json(obj)
        elif isinstance(obj, (list, tuple)):
            return self.__list_to_json(obj)
        elif isinstance(obj, dict):
            return self.__dict_to_json(obj)
        else:
            return self.__custom_to_json(obj)

