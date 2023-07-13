#   selection sort

x = [10,20,90,100,40,34,4,100]

for i in range(0,len(x)-1):
    for j in range(i+1, len(x)):
        if x[i] > x[j]:
            x[i],x[j] = x[j],x[i]
            
            
print('-------- selection sort --------------')
print(x)



"""
    -------- selection sort output --------------
[4, 10, 20, 34, 40, 90, 100, 100]

"""