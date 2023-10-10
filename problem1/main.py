def remove_duplicates(array):
    if not array:
        return 0

    unique_set = set()
    unique_pointer = 0

    for i in range(len(array)):
        if array[i] not in unique_set:
            unique_set.add(array[i])
            array[unique_pointer] = array[i]
            unique_pointer += 1

    return unique_pointer

if __name__ == "__main__":
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))  # 4
    print(remove_duplicates([2, 3, 4, 5, 6, 9, 9]))  # 6
    print(remove_duplicates([2, 2, 2, 11]))          # 2
    print(remove_duplicates([2, 2, 2, 11]))          # 2
    print(remove_duplicates([1, 2, 3, 11, 11]))      # 4