mat_1 = [
    [3, 2, 3],
    [2, 1, 2],
    [1, 2, 1]
]

mat_2 = [
    [2, 2],
    [3, 2],
    [1, 1]
]

mat_2_new = []

for i in range(0,len(mat_2[0])):
    temp = [
        mat_2[0][i],
        mat_2[1][i],
        mat_2[2][i]
    ]
    mat_2_new.append(temp)

print("Martix One: ") 
[print(x) for x in mat_1]

print("Martix Two: ") 
[print(x) for x in mat_2]
res = []

print("##################")

for i in mat_1:
    temp = []

    for j in mat_2_new:
        temp_count = 0
        for k in range(len(j)):
            temp_count += i[k] * j[k]
        temp.append(temp_count)
    res.append(temp)
        
print("The result: ")
[print(x) for x in res]
