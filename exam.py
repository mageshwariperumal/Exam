print("*******************************************************************************************")
print("-----------------------------------USER-DETAILS-----------------------------------------")
name=input("Enter the name :")
age=input("Enter the age:")
eduq=input("Enter the qualification:")
print("*******************************************************************************************")
for i in range(3):
    print(i)
    wh=int(input("if you want to coninue press 1 else press 0.......  :"))
    while(wh==1):
        print("1.python")
        print("2.c")
        print("3.c++")
        w=int(input("enter the course choice:"))
        if(w==1):
            print("*******************************************************************************************")
            q=int(input("press 1 to go to questions... : "))
            if(q==1):
                print("*******************************************************************************************")
                print("1.who developed python")
                print("11.wick van rossum")
                print("12.rasmus lerdorf")
                print("13.guido van rossum")
                print("14.niene stom")
                print("*********************************")
                A=int(input("Enter the choice:"))
                if((A==11)or(A==12)or(A==13)or(A==14)):
                    E=input("Enter the answer:")
                    print("your answer is:",E)
                else:
                    print("not in choice")
                print("*********************************")
                print("2.Extension of the python file")
                print("11.python")
                print("12.pl")
                print("13.py")
                print("14.p")
                print("*********************************")
                A=int(input("Enter the choice:"))
                if((A==11)or(A==12)or(A==13)or(A==14)):
                    F=input("Enter the answer:")
                    print("your answer is:",F)
                else:
                    print("not in choice")
                print("*********************************")
                print("3.All keywords in python are.......")
                print("11.capitalized")
                print("12.lower case")
                print("13.upper case")
                print("14.none of the above")
                print("*********************************")
                A=int(input("Enter the choice:"))
                if((A==11)or(A==12)or(A==13)or(A==14)):
                    G=input("Enter the answer:")
                    print("your answer is:",G)
                else:
                    print("not in choice")
                print("*********************************")
                print("4.single line command in python")
                print("11.//")
                print("12.#")
                print("13.!")
                print("14./*")
                print("*********************************")
                A=int(input("Enter the choice:"))
                if((A==11)or(A==12)or(A==13)or(A==14)):
                    H=input("Enter the answer:")
                    print("your answer is:",H)
                else:
                    print("not in choice")
                print("*********************************")
            print("**************************************************************************")
            print("---------STUDENT_DETAILS---------")
            print("*********************************")
            print(" NAME :",name)
            print(" AGE :",age)
            print(" EDUCATIONAL QUALIFICATION:",eduq)
            print("\n")
            print("----------------RESULT----------------")
            print("\n")
            print("ANSWERS : ")
            print("1.correct")if(E.lower()=="11")else print("1.wrong")
            print("2.correct")if(F.lower()=="13")else print("2.wrong")
            print("3.correct")if(G.lower()=="14")else print("3.wrong")
            print("4.correct")if(H.lower()=="12")else print("4.wrong")
            print("\n\n")
            if(E.lower()=="11"):
                qi=1
            else:
                qi=0
            if(F.lower()=="13"):
                qe=1
            else:
                qe=0
            if(G.lower()=="14"):
                qr=1
            else:
                qr=0
            if(H.lower()=="12"):
                qt=1
            else:
                qt=0
            total1=qi+qe+qr+qt
            print("\t\t TOTAL MARKS  :  ",total1)
            print("**********************************************************")
            ans=input("If you need answer y/n ? : ")
            if(ans.lower()=="y"):
                print("1.a.wick van rossum\n2.c.py\n3.d.none of the above\n4.b.#")
            else:
                print("ALL THE BEST.............")
        print("---------------------------------------------------------------------------------------------------")
        if (w==2):
            p=int(input("press 1 to go to questions... : "))
            if(p==1):
                print("*******************************************************************************************")
                print("1.who is the father of c")
                print("11.steve jobs")
                print("12.james gosling")
                print("13.dennis ritchie")
                print("14.rasmus lerdorf")
                print("*********************************")
                A=int(input("Enter the choice:"))
                if((A==11)or(A==12)or(A==13)or(A==14)):
                    E=input("Enter the answer:")
                    print("your answer is:",E)
                else:
                    print("not in choice")
                print("*********************************")
                print("2.cannot be a variable in c")
                print("11.volatile")
                print("12.true")
                print("13.friend")
                print("14.export")
                print("*********************************")
                A=int(input("Enter the choice:"))
                if((A==11)or(A==12)or(A==13)or(A==14)):
                    F=input("Enter the answer:")
                    print("your answer is:",F)
                else:
                    print("not in choice")
                print("*********************************")
                print("3.All keywords in c are.......")
                print("11.capitalized")
                print("12.lower case")
                print("13.upper case")
                print("14.none of the above")
                print("*********************************")
                A=int(input("Enter the choice:"))
                if((A==11)or(A==12)or(A==13)or(A==14)):
                    G=input("Enter the answer:")
                    print("your answer is:",G)
                else:
                    print("not in choice")
                print("*********************************")
                print("4.keyword which is used to revent any changes in the variable within c")
                print("11.immutable")
                print("12.mutable")
                print("13.const")
                print("14.volatile")
                print("*********************************")
                A=int(input("Enter the choice:"))
                if((A==11)or(A==12)or(A==13)or(A==14)):
                    H=input("Enter the answer:")
                    print("your answer is:",H)
                else:
                    print("not in choice")
                print("*********************************")
            print("----------------RESULT----------------")
            print("\n")
            print("ANSWERS : ")
            print("1.correct")if(E.lower()=="13")else print("1.wrong")
            print("2.correct")if(F.lower()=="11")else print("2.wrong")
            print("3.correct")if(G.lower()=="12")else print("3.wrong")
            print("4.correct")if(H.lower()=="13")else print("4.wrong")
            print("\n\n")
            if(E.lower()=="13"):
                pi=1
            else:
                pi=0
            if(F.lower()=="11"):
                pe=1
            else:
                pe=0
            if(G.lower()=="12"):
                pr=1
            else:
                pr=0
            if(H.lower()=="13"):
                pt=1
            else:
                pt=0
            total2=pi+pe+pr+pt
            print("\t\t TOTAL MARKS  :  ",total2)
            total=total1+total2
            print("\t\t TOTAL MARKS  :  ",total)
            print("**********************************************************")
            ans=input("If you need answer y/n ? : ")
            if(ans.lower()=="y"):
                print("1.c.dennis ritchie\n2.a.volatile\n3.b.lower case\n4.c.const")
            else:
                print("ALL THE BEST.............")
        print("---------------------------------------------------------------------------------------------------")
        if(w==3):
            s=int(input("press 1 to go to questions... : "))
            if(s==1):
                print("*******************************************************************************************")
                print("1.who invented c++")
                print("11.dennis ritchie")
                print("12.ken thompson")
                print("13.brian kernighan")
                print("14.bjarne stroustrup")
                print("*********************************")
                A=int(input("Enter the choice:"))
                if((A==11)or(A==12)or(A==13)or(A==14)):
                    E=input("Enter the answer:")
                    print("your answer is:",E)
                else:
                    print("not in choice")
                print("*********************************")
                print("2.Extension of the c++ file")
                print("11.hg")
                print("12.cpp")
                print("13.h")
                print("14.c")
                print("*********************************")
                A=int(input("Enter the choice:"))
                if((A==11)or(A==12)or(A==13)or(A==14)):
                    F=input("Enter the answer:")
                    print("your answer is:",F)
                else:
                    print("not in choice")
                print("*********************************")
                print("3.Approach is used by c++ is")
                print("11.left to right")
                print("12.right to left")
                print("13.bottom up")
                print("14.top down")
                print("*********************************")
                A=int(input("Enter the choice:"))
                if((A==11)or(A==12)or(A==13)or(A==14)):
                    G=input("Enter the answer:")
                    print("your answer is:",G)
                else:
                    print("not in choice")
                print("*********************************")
                print("4.which of the following type is provided by c not in c++")
                print("11.double")
                print("12.float")
                print("13.int")
                print("14.bool")
                print("*********************************")
                A=int(input("Enter the choice:"))
                if((A==11)or(A==12)or(A==13)or(A==14)):
                    H=input("Enter the answer:")
                    print("your answer is:",H)
                else:
                    print("not in choice")
                print("*********************************")
            print("----------------RESULT----------------")
            print("\n")
            print("ANSWERS : ")
            print("1.correct")if(E.lower()=="14")else print("1.wrong")
            print("2.correct")if(F.lower()=="12")else print("2.wrong")
            print("3.correct")if(G.lower()=="13")else print("3.wrong")
            print("4.correct")if(H.lower()=="14")else print("4.wrong")
            print("\n\n")
            if(E.lower()=="14"):
                si=1
            else:
                si=0
            if(F.lower()=="12"):
                se=1
            else:
                se=0
            if(G.lower()=="13"):
                sr=1
            else:
                sr=0
            if(H.lower()=="14"):
                st=1
            else:
                st=0
            total3=si+se+sr+st
            print("\t\t TOTAL MARKS  :  ",total3)
            print("**********************************************************")
            ans=input("If you need answer y/n ? : ")
            if(ans.lower()=="y"):
                print("1.d.bjarne stroustrup\n2.b.cpp\n3.c.bottom up\n4.d.bool")
            else:
                print("ALL THE BEST.............")
            total=total1+total2+total3
            print("\t\t TOTAL MARKS  :  ",total)
        print("---------------------------------------------------------------------------------------------------")

    
    
    

