__all__ = ['list_to_dict']

def list_to_dict(list):
    dict = {}
    for index, value in enumerate(list):
        dict[index] = value

    return dict