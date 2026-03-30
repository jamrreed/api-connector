def python_arrays():
    list_type: list = ("item1", "item2", 3, 3)
    # also constructed like this: = list(("item1", "item2", 3, 3))
    # lists are ordered, indexed, changeable, with duplicates allowed
    list_type.append(4)
    list_type.remove(4) # remove by value
    list_type.pop() # remove by index

    tuple_type: tuple = ("item1", "item2", 3, 3)
    # also constructed like this: = tuple(("item1", "item2", 3, 3))
    # tuple_type.append - not allowed, tuples are like lists except they are unchangeable

    set_type: set = {"item1", "item2", 3}
    # also constructed like this: = set (("item1", "item2", 3))
    set_type.add(4)
    set_type.remove(4) # remove by value (key)
    # set items are unordered, unindexed, and unchangeable (but you can add new items or remove them)

    dict_type: dict = {"key1": "value1", "key2": "value2"}
    dict_type["key3"] = "value3"
    dict_type.pop("key3") # remove by key
    # dict are ordered, changeable, but cannot have duplicate keys
    pass