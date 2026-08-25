def all_thing_is_obj(object: any) -> int:
    if object.__class__.__name__ == "list":
        print(f"List : {type(object)}")
    elif object.__class__.__name__ == "tuple":
        print(f"Tuple : {type(object)}")
    elif object.__class__.__name__ == "set":
        print(f"Set : {type(object)}")
    elif object.__class__.__name__ == "dict":
        print(f"Dict : {type(object)}")
    elif object.__class__.__name__ == "str":
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    return 42


