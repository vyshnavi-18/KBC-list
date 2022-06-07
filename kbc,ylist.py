print("hii,welcome to KBC")
que=[
   ["how many continents are there?"],
   ["What is capital of indin?"],
   ["which cource provide in NVG?"]
]
opt=[
    ["Foue","Nine","Seven","eight"],
    ["Chandigar","Bhopal","chennai","Delhi"],
    ["Software Engineer","Counseling","Tourism","Agriculture"]
    ]
sol=["seven","delhi","software"]
i=0
c=0
while (i<len(que)):
    print(que[i])
    j=0
    while c<len(opt):
        while j<=len(opt):
            c+=1
            print(c,opt[i][j])
            j+=1
    lifeln1=input("you want life line:")
    if (lifeln1=="yes"):
        print("1.four","3.seven")
        ans1=input("select opt")
        if ans1=="seven":  
            print("correct")  
            print("your answer is correct so you win rs.10,000/-")  
            print("your a qualified to the next round")  
            print("next question is:")
        break
    else:
        print("good")
        ans1=input("select opt")
        if ans1=="seven":
            print("correct")
            print("your answer is correct so your win rs.10,000/-")
            print("your qualify to the next round")
            print("next question is:")
        else:
            print("wrong")
            print("sorry! your answer is wrong so you are disqualified")
        break
i+=1
c=0
while i<len(que):
    print(que[i])
    j=0
    while c<len(opt):
        while j<=len(opt):
            c+=1
            print(c,opt[i][j])
            j+=1
    life2=input("you want life line:")
    if life2=="yes":
        print("1.chandigarh","4.delhi")
        ans2=input("select opt:")
        if ans2=="delhi":
            print("correct")
            print("your answer is correct so you win rs.25,000/-")
            print("your qualified to the next rount")
            print("next question is:")
        break
    else:
        print("great")
        ans2=input("select opt:")
        if ans2=="delhi":
            print("correct")
            print("your answer is correct so your win rs.25,000/-")
            print("your qualify to the next round")
            print("next question is:")
        else:
            print("wrong")
            print("sorry! your answer is wrong so you are disqualified")
        break
i+=1
c=0
while i<len(que):
    print(que[i])
    j=0
    while c<len(opt):
        while j<=len(opt):
            c+=1
            print(c,opt[i][j])
            j+=1
    life3=input("you want life line:")
    if life3=="yes":
        print("software engineer","tourism")
        ans3=input("select opt")
        if ans3=="software engineer":
            print("correct")  
            print("your answer is correct so you win rs.10,000/-")  
            print("your a qualified to the next round")  
            print("next question is:")
        break
    else:
        print("great")
        ans3=input("select opt:")
        if ans3=="software engineer":
            print("correct")
            print("your answer is correct so your win rs.25,000/-")
            print("your qualify to the next round")
        else:
            print("wrong")
            print("sorry! your answer is wrong so you are disqualified")
        break
