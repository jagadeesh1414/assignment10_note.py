def Cloning(li1): 
 
    li_copy = [] 
 
    li_copy.extend(li1) 
 
    return li_copy 
 
 
li1 = [5,3,10,30,12,11,5,4] 
 
li2 = Cloning(li1) 
 
print("Original List:", li1) 
 
print("After Cloning:", li2)