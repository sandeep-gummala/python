def flat_list(li):
    li1=[]
    for i in li:
        for j in i:
            li1.append(j)
    return li1
print(flat_list([[1,2,3],[4,7,8],[5,3,8]]))
