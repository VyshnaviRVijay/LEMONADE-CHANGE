def lemonade():
    bills=[5,20,10,5]
    five_d=0
    ten_d=0
    if bills[0]!=5:
        return False
    for i in bills:
        if i==5:
            five_d=five_d+1
        elif i==10:
            if five_d>0:
                ten_d=ten_d+1
                five_d=five_d-1
            else:
                return False
        else:
            if five_d>0 and ten_d>0:
                ten_d=ten_d-1
                five_d=five_d-1
            elif five_d>=3:
                five_d=five_d-3
            else:
                return False
    return True
print(lemonade())







