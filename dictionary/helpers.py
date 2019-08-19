
def str_to_bool(v):
    if isinstance(v, bool):
        return v
    if v == 'True':
        return True
    elif v == 'False':
        return False
    else:
        raise ValueError('Is not a correct value')
