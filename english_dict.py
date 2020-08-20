d = {}
print('歡迎來到英文高手字典。')
while True:
    print('1.新增字典')
    print('2.列出字典')
    print('3.英翻中')
    print('4.中翻英')
    print('5.測驗')
    print('6.離開')
    option=input('請輸入選項:')
    if option == "6":
        break
    if option == "1":
        while True:
            voc = input('請輸入英文單字，退出請輸入0:')
            if voc=="0":
                break
            if voc not in d:
                voc_zh = input('請入中文意思')
                d[voc]=voc_zh
            else:
                print('已存在')
    elif option == "2":
        s = sorted(d)
        for i in s:
            print(i,':',d[i])
    elif option == '3':
        get=1
        while True:
            voc=input("請輸入英文單字，輸入0退出")
            if voc == "0" :
                break
            for k in d.keys():
                if voc==k:
                    print(voc,"的中文是",d[voc])
                    get=2
            if get == 1:
                print("無此單字")            
    elif option == "4":
        while True:
            get=1
            ch=input("請輸入中文，輸入0退出")
            if ch=="0":
                break
            for k,v in d.items():
                if ch == v:
                    print(k,"的中文是",v)
                    get=2
            if get == 1:
                print("無此單字")
    elif option == "5":
        lan=input("請選擇考中文(輸入1)考英文(輸入2)")
        score=0
        if lan==1:
            for k,v in d.items():
                print(k)
                ans = input('中文?')
                if ans == k:
                    print("正確")
                    score=score+(100/int(len(d)))
                else:
                    print("錯了請加油")
            print("你的分數是",score)
        if lan == 2:
            for k,v in d.items():
                print(v)
                ans = input('英文?')
                if ans == v:
                    print("正確")
                    score=score+(100/int(len(d)))
                else:
                    print("錯了請加油")
            print("你的分數是",score)


print('感謝使用')