from typing import get_type_hints, List


def create_attributes(obj: object):
    for attribute, type_hint in get_type_hints(obj).items():
        setattr(obj, attribute, type_hint)

def make_object(json_data: dict, obj: object):
    create_attributes(obj)
    for key, value in json_data.items():
        attribute = getattr(obj, key)
        if attribute:
            # if attribute is a basic type
            if obj.__annotations__[key] in [str, bytes, int, float, bool]:
                setattr(obj, key, value)
                continue
            # if attribute is a list
            try:
                if obj.__annotations__[key].__origin__ == list:
                    base_type = obj.__annotations__[key].__args__[0]
                    temp_list = [base_type(item) for item in value]
                    setattr(obj, key, temp_list)
                    continue
            except:
                pass
            # if attribute is a dict
            if obj.__annotations__[key] == dict:
                pass
                continue
            # if attribute is a specific class
            else:
                attribute_type = obj.__annotations__[key]
                setattr(obj, key, attribute_type(value))