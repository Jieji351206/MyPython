score = int(input("รับค่าคะแนน:"))

if score>=101:
    print("กรุณารับป้อนข้อมูล 0-100")
    print("...")
    
elif score>=80:
    print("เกรด A")
    print(">//<")
elif score>=70:
    print("เกรด B")
    print(">w<")
elif score>=60:
    print("เกรด C")
    print(">o<")
elif score>=50:
    print("เกรด D")
    print("TwT")
elif score>=0:
    print("เกรด F")
    print("TOT")

elif score<0:
    print("กรุณารับป้อนข้อมูล 0-100")
    print("...")