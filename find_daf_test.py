import sys
fo = open(sys.argv[1], "r")  ##bison
fo1 = open(sys.argv[2],"r")
fo2 = open(sys.argv[3],"w")
list0=[]
list1=[]
list11=[]
list2=[]

for i in fo:
    if i.startswith("##"):
        pass
    else:
        i1 = i.strip().split()
        geno=i1[9].split(":")[0]
        list0.append([i1[0],i1[1]])              ##所有bisoncall出来的
        if geno == "0/0" :
            list1.append([i1[0],i1[1],geno])   ##0/0祖先等位
        elif geno == "1/1" :                   ##1/1祖先等位
            list11.append([i1[0],i1[1],geno])
for j in fo1:                      ##输入文件
    if j.startswith("##"):
        pass
    elif j.startswith("#"):
        j = j.strip().split()
        all = int(len(j[9:])*2)   ##总等位基因数
    else:
        j1 = j.strip().split('\t')
        for z in j1[9:]:
            z = z.split(":")[0]
            list2.append([j1[0], j1[1], z])
list5=[]


dic={}
list7=[]
list8=[0]
l1=0
for m in list2:
    if [m[0],m[1]] not in list0:
        list5.append(m)
for m1 in list5:
    if m1[2] == '0/0':
        l1+= 0
    elif m1[2] == '1/0' or m1[2] == '0/1':
        l1+=1
    elif m1[2] == '1/1':
        #print(m[2])
        l1+=2
    dic[m1[0],m1[1]]=l1
for key,value in dic.items():
    temp = key,value
    list7.append(temp)
for t in list7:
    list8.append(t[1])
    t1 = list8[-1] - list8[-2]
    fo2.write(str(t[0]).rstrip(")").lstrip("(").replace("'","").replace(",","\t")+"\t"+str(t1/all)+"\n")

###call出部分的讨论
h1=0
f1=0
listh1=[0]
listf1=[0]

for h in list1:
    for k in list2:
      ##call出的0/0祖先型
        if h[0] == k[0] and h[1] == k[1] :
            if h[2] == k[2]:
                h1+=0
            elif k[2] == '0/1' or k[2] =='1/0':
                h1+=1
            elif k[2] == '1/1':
                h1+=2
    listh1.append(h1)
    n1= listh1[-1]-listh1[-2]
    fo2.write(h[0]+"\t"+h[1]+"\t"+str(n1/all)+"\n")
for f in list11:
    for k in list2:
        ##call出的1/1祖先型
        if k[0] == f[0] and k[1] == f[1]:
            if k[2] == f[2]:
                f1+=0
            elif k[2] == '0/1' or k[2] == '1/0':
                f1+=1
            elif k[2] == '0/0':
                f1 = f1 +2
    listf1.append(f1)
    n2 = listf1[-1]-listf1[-2]
    fo2.write(f[0]+"\t"+f[1]+"\t"+str(n2/all)+"\n")



