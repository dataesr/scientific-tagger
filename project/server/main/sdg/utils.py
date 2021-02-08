def does_contain(input_str, list_of_kw):
    for f in list_of_kw:
        if isinstance(f, str) and f in input_str:
            return (True, f)
        if isinstance(f, list):
            sub_cond = True
            for sub_f in f:
                sub_cond = sub_cond and (sub_f in input_str)
            if sub_cond and len(f)>0:
                return (True, f)
    return (False, None)
    
