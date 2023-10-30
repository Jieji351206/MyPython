def myFunc():
    num1 = int(input("รับค่าตัวเลข:"))
    num2 = num1
    while  num1>0:
        print(num1)
        num1-=1
    
    #ให้แก้โจทย์เพิ่มนับขึ้นจาก 0 ถึง num
    while num1<num2:
        print(num1)
        num1+=1
    

for i in range(0,10,1):  
    if i == 5:
        #pass
        #break
        continue
    if i == 8:
        continue
    print(i)
    
myFunc()