count=0
for i in range(1,4):
    print('请输入第',i,'个班级的学生成绩')
    for j in range (1,4):
        score=int(input('请输入第',j,'个学生成绩'))
        if score<0:
            print('输入负数进入下一个班级')
            break
        if score<80:
            continue
        count+=1
print('大于80的人数：',count)
