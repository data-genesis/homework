def introspection_info(obj):

    obj_type = type(obj).__name__
    obj_module = getattr(obj, '__module__', 'built-in')
    obj_attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    obj_methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    result = {
        'type': obj_type,
        'module': obj_module,
        'attributes': obj_attributes,
        'methods': obj_methods,
    }

    if isinstance(obj, (list, tuple, set, dict)):
        result['length'] = len(obj)
    elif isinstance(obj, (int, float, complex)):
        result['is_integer'] = isinstance(obj, int)
    elif isinstance(obj, str):
        result['length'] = len(obj)
        result['is_numeric'] = obj.isnumeric()

    return result

number_info = introspection_info(42)
print(number_info)
