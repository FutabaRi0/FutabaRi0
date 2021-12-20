origin = input("请输入一整数四则运算算式（包含正负整数）（不带等号）：");nosp = "";a = "";b = "";counter = 0;cal = 0;
for i in range(len(origin)):
    if origin[i] == " ":
        continue
    else:
        nosp = nosp + origin[i]
for i in range(len(origin)):
    if origin[i] != '+' or origin[i] != '-' or origin[i] != '*' or origin[i] != '/':
        a = a + origin[i]
        counter = counter + 1
    elif origin[i] == '+':
        cal = cal + 1
        counter + 1
        break
    elif origin[i] == '-':
        cal = cal + 2
        counter + 1
        break
    elif origin[i] == '*':
        cal = cal + 3
        counter + 1
        break
    elif origin[i] == '/':
        cal = cal + 4
        counter + 1
        break
for i in range(counter+1,len(origin)):
    b = b + origin[i]
a = int(a)
b = int(b)
if cal == 1:
    print(a,'+',b,'=',a+b,sep='')
elif cal == 2:
    print(a,'-',b,'=',a-b,sep='')
elif cal == 3:
    print(a,'*',b,'=',a*b,sep='')
elif cal == 4:
    if b != 0:
        print(a,'/',b,'=',a/b,sep='')
    else:
        print:("错误！零不能做除数！")
