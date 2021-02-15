def does_contain(input_str, list_of_kw):
    for f in list_of_kw:
        if isinstance(f, str) and f.lower() in input_str.lower():
            return (True, f)
        if isinstance(f, list):
            sub_cond = True
            for sub_f in f:
                sub_cond = sub_cond and (sub_f.lower() in input_str.lower())
            if sub_cond and len(f)>0:
                return (True, f)
    return (False, None)
   
# one of the input in input_list is part of the list_of_kw
def does_contain_list(input_list, list_of_kw):
    for input_str in input_list:
        contain_bool, evidence = does_contain(input_str, list_of_kw)
        if contain_bool:
            return (contain_bool, evidence)
    return (False, None)
