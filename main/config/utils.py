from collections import namedtuple


class Utils:
    @staticmethod
    def dict_to_tuple(obj, name="X"):
        if isinstance(obj, dict):
            fields = obj.keys()
            field_value_pairs = {str(field): Utils.dict_to_tuple(obj[field], field) for field in fields}
            try:
                return namedtuple(typename=name, field_names=fields, rename=True)(**field_value_pairs)
            except TypeError:
                # Cannot create namedtuple instance so fallback to dict (invalid attribute names)
                return dict(**field_value_pairs)
        elif isinstance(obj, (list, set, tuple, frozenset)):
            return [Utils.dict_to_tuple(item) for item in obj]
        else:
            return obj
