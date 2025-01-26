array = list(map(int, input().split()))

sorted_array = sorted(array)

def c():
    for i in range(4):
        new_array = array[:]
        p = new_array[i+1]
        new_array[i+1] = new_array[i]
        new_array[i] = p
        for j in range(5):
            if new_array[j] != sorted_array[j]:
                break
            elif j == 4:
                return 'Yes'
    return 'No'

print(c())
                
            
