def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        if i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        else:
            j < len(right)
            array[k] = right[j]
            j += 1
            k += 1
    return array


def is_anagram(first_string, second_string):
    first_string = list(first_string.lower())
    second_string = list(second_string.lower())
    sort_first_string = "".join(merge_sort(first_string))
    sort_second_string = "".join(merge_sort(second_string))

    if not first_string and not second_string:
        return ('', '', False)
    if sort_first_string == sort_second_string:
        return (sort_first_string, sort_second_string, True)
    else:
        return (sort_first_string, sort_second_string, False)
