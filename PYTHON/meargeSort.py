arr = [5, 10,30, 8, 1, 9, 3]


def mearge(array):
    if len(array) > 1:
        mid = len(array) // 2
        a = array[:mid]
        b = array[mid:]
        mearge(a)
        mearge(b)

        i = 0
        j = 0
        k = 0
        while i < len(a) and j < len(b):
            if a[i] >= b[j]:
                array[k] = b[j]
                j += 1
                k += 1
            else:
                array[k] = a[i]
                i += 1
                k += 1
        while i < len(a):
            array[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            array[k] = b[j]
            j += 1
            k += 1
    return array


print(mearge(arr))
