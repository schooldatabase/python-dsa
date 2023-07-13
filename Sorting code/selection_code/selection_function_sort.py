#   selection function sorting

def selection_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                print(arr)
    return arr

if __name__ == "__main__":
    arr = [45,20,50,15,10]
    # arr = [1,22, 64, 34, 25, 3, 12, 22, 11, 90, 33,500]
    selection_sort(arr)
    print("Selection Sort function Result:", arr)
    
    
    """
               ------------------ output -------------------
    Selection Sort function Result: [1, 3, 11, 12, 22, 22, 25, 33, 34, 64, 90, 500]
    """