

def array_merge_sort(n, m, array): # n rows, m columns

    if n == 1:
        if m == 1:
            return array
        #print('ok', array)
        temp = one_d_merge_sort(m, array[0])
        #print(temp, 10000)

        return [temp]

    elif m == 1:

        temp = [[array[i][0] for i in range(n)]]
        temp = one_d_merge_sort(n, temp[0])

        #a = [temp[i] for i in range(m)]
        #print(temp)
        #print(temp, 200)
        return [[temp[i]] for i in range(n)]


    rowsplit = 1 + int((n - 1) / 2)
    colsplit = 1 + int((m - 1) / 2)
    #print(rowsplit, colsplit)


    topleft = [array[i][0:colsplit] for i in range(0, rowsplit)]
    topright = [array[i][colsplit:m] for i in range(0, rowsplit)]
    bottomleft = [array[i][0:colsplit] for i in range(rowsplit, n)]
    bottomright = [array[i][colsplit:m] for i in range(rowsplit, n)]
    #print(rowsplit, colsplit, topleft, topright, bottomleft, bottomright)

    topleft = array_merge_sort(rowsplit, colsplit, topleft)
    topright = array_merge_sort(rowsplit, m - colsplit, topright)
    bottomleft = array_merge_sort(n - rowsplit, colsplit, bottomleft)
    bottomright = array_merge_sort(n - rowsplit, m - colsplit, bottomright)


    #print(topleft, topright, bottomleft, bottomright)
    return merge(n, m, rowsplit, colsplit, topleft, topright, bottomleft, bottomright)





def one_d_merge_sort(n, arr):
    if n > 1:

        # Finding the mid of the array
        mid = 1 + int((len(arr) - 1) / 2)
        #print(arr, mid)

        # Dividing the array elements
        L = arr[:mid]
        # into 2 halves
        R = arr[mid:]
        #print(L, R)
        #print(arr, mid, L, R)
        # Sorting the first half
        L = one_d_merge_sort(mid, L)
        # Sorting the second half
        R = one_d_merge_sort(n-mid, R)
        i = j = k = 0
        #print(R, L)
        # Copy data to temp arrays L[] and R[]
        out = one_d_merge(R, L)

        return out
    else:
        return arr



    # Code to print the

def merge(rows, cols, rowsplit, colsplit, a, b, c, d): # first merges rows together, then iterates through columns
    #row sorting
    toprows = [one_d_merge(a[i], b[i]) for i in range(0, rowsplit)]
    bottomrows = [one_d_merge(c[i], d[i]) for i in range(0, cols - colsplit)]
    rowarray = toprows + bottomrows
    #column sorting
    #print(rowarray)
    for i in range(0, cols): # a and c

        ac_column = one_d_merge([rowarray[j][i] for j in range(rowsplit)], [rowarray[j][i] for j in range(rowsplit, rows)])
        #print(ac_column, i)
        for index, element in enumerate(ac_column):
            rowarray[index][i] = element


    #print(rowarray)
    return rowarray

def one_d_merge(list1, list2): # assumes each sub list are sorted, then combines them by iterating over each element
    output = [0] * (len(list1) + len(list2))

    i, j, k = 0, 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            output[k] = list1[i]
            i += 1
        else:
            output[k] = list2[j]
            j += 1
        k += 1

        # Checking if any element was left
    while i < len(list1):
        output[k] = list1[i]
        i += 1
        k += 1

    while j < len(list2):
        output[k] = list2[j]
        j += 1
        k += 1
    #print(output, 100)
    return output

if __name__ == '__main__':
    '''a = []
    #print(a)
    n = int(input("Num Rows: "))
    m = int(input("Num Cols: "))
    for i in range(n):
        a.append([])
        for j in range(m):
            a[i].append(int(input("array value: ")))

    print(a)
    print(array_merge_sort(n, m, a))'''

    n, m = map(int, input("N, M: ").split())

    temparray = input("Enter Values: ").split()
    array = []
    for i in range(n):
        array.append([])
        for j in range(m):
            index = i * n + j
            array[i].append(int(temparray[index]))
    print(array_merge_sort(n, m, array))
