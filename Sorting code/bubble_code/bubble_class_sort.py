class BubbleSort:
    @staticmethod
    def sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Bubble Sort
    bubble_sort = BubbleSort()
    bubble_sort.sort(arr)
    print("Bubble Sort Result:", arr)