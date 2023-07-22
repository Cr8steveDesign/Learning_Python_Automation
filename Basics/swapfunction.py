# A Simple swap function in python


def swap_array(a = []):
    temp = a[0]
    a[0] = a[1]
    a[1] = temp
    return [a[0], a[1]]