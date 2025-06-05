#First Project - Basic Calculator:
# num1 = input("Enter your first number: ")
# operator = input("enter what action do you wanna do: ")
# num2 = input("Enter your second number: ")
# if operator=="+":
#     print ("The result is: ",int(num1)+int(num2))
# elif operator=="-":
#     print ("The result is: ",int(num1)-int(num2))
# elif operator=="*":
#     print ("The result is: ",int(num1)*int(num2))
# elif operator=="/":
#     print ("The result is: ",int(num1)/int(num2))
# else:
#     print ("you didn't choose a correct operator")

#If exercises
#Q1
# num=float(input("Enter a number:"))
# if (num>0):
#     print ("The number is positive")
# elif(num<0):
#     print ("The number is negative")
# else:
#     print ("The number is zero")

#Q2
# year=int(input("Enter a year:"))
# if (year%4==0 and year%100!=0) or year%400==0:
#     print ("It's a leap year!")
# else:
#     print ("It's not a leap year")

#Q3
# num=int(input("Enter a number:"))
# if (num%2==0):
#     print ("This is an even numnber")
# else:
#     print("This is an odd number")

#Q4
# num1=int(input("Enter the first number:"))
# num2=int(input("Enter the second number:"))
# num3=int(input("Enter the third number:"))
# if num1>num2:
#     if (num1>num3):
#         print (f"The biggest number is {num1}")
#     else:
#         print (f"The biggest number is {num3}")
# elif (num2>num3):
#     print (f"The biggest number is {num2}")
# else:
#     print (f"The biggest number is {num3}")

#Q5
# char=input("Enter the character:")
# if char in ["i","e","a","u","o"]: #לבדוק אם משהו נוכח בתוך ליסט
#     print ("The char is a vowel")
# else:
#     print ("The char is a consonant")

#Q6
# string=input ("Enter a string:") 
# if (string==string[::-1]): #בודק האם הסטרינג הוא פלינדרום
#     print ("The string is a palindrome")
# else:
#     print ("The string is not a palindrome")

#Q7
# percentage= float(input ("Enter the precentage:"))
# if percentage>=90:
#     grade="A"
# elif percentage>=80:
#     grade="B"
# elif percentage>=70:
#     grade="C"
# elif percentage>=60:
#     grade="D"
# else:
#     grade="F"
# print (f"The grade is {grade}")

#Q8
# year=int(input("Enter a year:"))
# if (year%100==0):
#     print ("It's a century year!")
# else:
#     print ("It's not a century year")

#Q9
import math

# num=int(input("Enter a number:"))

# if(math.isqrt(num)**2==num): #בודק האם שורש של מספר ועיגול כלפי מטה שווה לשורש של מספר. יהיה אמת למספרים עם שורש שלם.
#     print("The number is a perfect square!")
# else:
#     print("The number is not a perfect square")

#Q10
# side1=int(input("Enter first length of side:"))
# side2=int(input("Enter second length of side:"))
# side3=int(input("Enter third length of side:"))

# if(side1==side2==side3):
#     print ("This triangle is equilateral")
# elif (side1==side2 or side2==side3 or side1==side3):
#     print ("This triangle is isosceles")
# else:
#     print ("This triangle is scalene")

#Loops
#For Loop
# for letter in "Python": #לולאה שמטרתה לרוץ על כל אות בסטרינג ולהדפיס אותה
#     print (letter)
# x= range(6) #ריינג' זו פעולה שכוללת בתוכה את כל הטווח מ0 עד המספר
# for i in x:
#     print (i)

# digits = [1,3,5,7]
# for i in digits:
#     print (i)
# else: #אפשר לעשות אלס גם ללולאת פור, שתפעל כאשר לא נכנס ללואה יותר
#     print ("That's it folks")

#While Loop
# total =0
# number=int(input("Enter a number you want to add up:")) #לולאת וייל שמטרתה לסכום את הקלטים עד אשר יתקבל 0
# while number!=0:
#     total+=number
#     number=(int(input("Enter a number you want to add up:")))
# print (f"your total is: {total}")

# count=0
# while count<3:
#     print ("You're inside the While loop")
#     count+=1
# else:
#     print("You're inside the else condition") #גם ללולאות וייל אפשר לעשות אלס

# count=0
# while count<3:
#     print ("You're inside the While loop")
#     count+=1
#     if (count==3):
#         break #אפשר לראות שלא נכנס לתנאי האלס אם יש לנו פקודת ברייק. ברייק גורם לנו להפסיק לרוץ בלולאה לגמרי
# else:
#     print("You're inside the else condition") 

# for i in range(5):
#     if i==3:
#         continue #מטרתו להחזיר אותנו לתחילת תנאי הלולאה, לא ממשיכים אחריו לפקודות בתוך הלולאה
#     print (i)

# num=0 #מדפיס רק מספרים אי זוגיים
# while num<10:
#     num+=1
#     if (num%2==0):
#         continue
#     print (num)


#Q1
# sum=0
# for i in range(1,101):
#     if i%3==0 and i%5==0: #לולאה שסוכמת את כל המספרים שמתחלקים ב3 ו5 ללא שארית
#         sum+=i
# print (f"the sum is: {sum}")

#Q2
# str=input("Enter a string:")
# i=len(str)-1
# revstr=""
# while i>=0: #לולאה להדפסת הסטרינג הפוך
#     revstr+=str[i]
#     i=i-1
# print(revstr)

#Q3
# str1= [1,2,3,4,5,6,7] #לולאת פור שתמצא את המשותף בין 2 רשימות
# str2=[9,8,7,6,5,4]
# common=[]
# for i in str1:
#     if i in str2:
#         common.append(i)
# print (common)

#Q4
# list=[1,1,1,1,3,3,4,4,2,2,7,7,7,"Strong","Strong","Hello","but"] #לולאת פור שמדפיסה את הרשימה ללא כפילויות איברים
# uniquelist=[]
# for i in list:
#     if i not in uniquelist:
#         uniquelist.append(i)
# print (uniquelist)

#Q5
# wordcount=0
# sentence=input("Enter a sentence:")
# splitsen=sentence.split()  #מפצל סטרינג לליסט שכל איבר הוא מילה
# for i in splitsen:
#     wordcount+=1
# print (wordcount)

#Q6
# word=""
# while word != "exit":
#     word=input("Enter a word:")

#Q7
# password="Tomer9249!"
# count=0
# while count<3:
#     insert=input("Enter your password:")
#     if insert==password:
#         print ("Success!")
#         break
#     count+=1
# if count==3:
#     print ("You've failed to enter the correct password in 3 attempts")

#Q8
# count=1 #מדפיס את כל המספרים הזוגיים מ1 ועד 50
# while count<=50:
#     if count%2==0:
#         print (count)
#         count+=2
#         continue
#     count+=1

#Q9
# sum=0 #סוכם את כל המספרים שיוכנסו עד אשר יוכנס 0
# num=1
# while num!=0:
#     num=int(input("Enter a number to be summed up:"))
#     if num==0:
#         break
#     sum+=num
# print (f"the sum is {sum}")

#Dictionary 
# country_capitals={  #מילון שכולל את שם המדינה כמפתח ואת עיר הבירה כערך
#     "USA":"Washington D.C.",
#     "England":"London",
#     "France":"Paris",
#     "Italy":"Naples",
#     "Israel":"Jerusalem"
# }
#print (country_capitals["USA"]) #להדפיס ערך של מפתח ספציפי
#print (country_capitals) #להדפיס את כל המילון
#country_capitals["Italy"]="Rome" #לשנות את הערך של מפתח מסוים
#print (country_capitals["Italy"])
#country_capitals["Germany"]="Berlin" #הוספת מפתח וערך שלא היו קיימים
#print(country_capitals)
#del country_capitals["USA"] #אופציה 1: מחיקת מפתח וערך ממילון
#print (country_capitals)
#country_capitals.pop("France") #אופציה 2: מחיקת מפתח וערך ממילון
#print (country_capitals)
#country_capitals.clear() #מחיקת כל תוכן המילון
#print (country_capitals)
#print(country_capitals.keys()) #מחזיר רק את המפתחות
#print(country_capitals.values()) #מחזיר רק את הערכים
#print(country_capitals.get("Israel")) #מחזיר את הערך של מפתח ספציפי
#tuple1=country_capitals.popitem() #מחזיר את המפתח+ערך האחרון כטופל
#print(tuple1)
#dic1=country_capitals #זה לא ייצור לנו קופי של המילון, אלא שיהיה לנו 2 משתנים שמצביעים על אותו מילון בזכרון
#print (dic1)
#dic2=country_capitals.copy() #זה כן ייצור לנו מילון חדש, וכאשר נשנה את המילון החדש/הישן, הוא לא ישפיע על ההופכי לו
#print (dic2)


# dic3={"a":1,"b":2}
# dic4={"b":10,"c":15}
# dic3.update(dic4) #מעדכן את המילון שעליו עושים את הפונקציה לפי המילון שממנו שואבים מידע
# dic3.update([("d",5),("e",20)]) #אפדייט מוכן לקבל גם טופל
# dic3.update(f=88,g=100) #ואפילו פרמטרי קווארגס
# print (dic3)
# print ("a" in dic3) #ידפיס לנו האם המפתח נמצא במילון בתשובה בוליאנית
# for letter in dic3:
#     print(letter) #לולאה שתדפיס את כל המפתחות של המילון
# print ("-------------")
# for value in dic3:
#     num=dic3[value]
#     print(num) #לולאה שתדפיס את כל הערכים של המילון


#Q1
# list=["apple","banana","watermelon","watermelon","banana","melon"]
# wordfreq={}
# for word in list:
#     if word in wordfreq:
#         wordfreq[word]+=1
#     else:
#         wordfreq[word]=1
# print (wordfreq)

#Q2
# dict1= {"a":1,"b":2,"c":3,"d":4} 
# dict2= {"a":1,"b":5,"c":6,"d":4,"e":4}
# dict3={}
# for letter in dict1: #פונקציה שיוצרת מילון חדש עם כל המפתחות+ערכים המשותפים (חשוב שלכל מפתח יהיה ערך זהה)
#     if dict1[letter]==dict2[letter]:
#         dict3[letter]=dict1[letter]
# print (dict3)

#Q3
# dict= {"a":1,"b":"Yellow!","c":3,"d":4} #פעולה שמטרתה לסכום את הערכים המספריים
# total=0
# for number in dict.values(): #נשתמש רק בערכים של המילון כי אותם נרצה לסכום
#     if isinstance(number,int): #בודק האם משתנה מסוים הוא מסוג מסוים, במקרה הזה, אינט. אם כן, מחזיר אמת ואם לא, שקר
#         total+=number
# print (total)

#Q4

# Sample= "this is a test . hello , test me , is this a test" #פונקציה שלוקחת סטרינג ומכניסה למילון את המילים כמפתחות ואת החזרות כערכים
# words=Sample.split()
# dic={}
# for word in words:
#     if word in dic:
#         dic[word]+=1
#     else:
#         dic[word]=1
# print (dic)

#Q5
# dict= {"a":1,"b":"Yellow!","c":3,"d":4} #פונקציה שלוקחת מילון והופכת את המפתחות לערכים והערכים למפתחות
# revdict={}
# for key in dict:
#     revdict[dict[key]]=key
# print (revdict)

#Q6
# dic={"banana":5,"apple":0,"cucumber":1,"tomato":10}
# sorted_keys =sorted(dic, key=dic.get, reverse=True) #פונקציה שממיינת את המילון לתוך ליסט בסדר יורד לפי הערכים
# print (sorted_keys)

#Q7

# data = [
#     {"name": "Alice", "age": 25, "score": 85},
#     {"name": "Bob", "age": 30, "score": 92},
#     {"name": "Charlie", "age": 22, "score": 78},
#     {"name": "David", "age": 35, "score": 88}
# ]

# sorted_by_age = sorted(data, key=lambda d: d["age"]) #למבדה היא דרך להגדיר פונקציה מהירה, במקרה הזה פונקציה שלוקחת מילון די ומחזירה את הערך של הגיל
# print("age sorted:", sorted_by_age)

# # מיון לפי ציון מהגבוה לנמוך
# sorted_by_score = sorted(data, key=lambda d: d["score"], reverse=True) #כנ"ל, פה מסודר לפי ציון גבוה לנמוך בעזרת רוורס=טרו
# print("score sorted:", sorted_by_score)

##### List Comprehensions
# square_list=[x**2 for x in range(5)] #יצור לנו רשימה של שטח ריבועים החל מצלע=0 ועד צלע=4 (תחום של עד 5 לא כולל)
# print (square_list)

# evennumbers=[x for x in range (10) if x%2==0] #יש לנו פה תנאי שאפשר להוסיף, במקרה הזה אנחנו נמנע ממספרים אי-זוגיים
# print (evennumbers)

# low_words=["facts","elon musk","burgir","banane"]
# up_words=[word.upper() for word in low_words] #יוצר לנו רשימה חדשה שבה האותיות עם קאפס לוק. חשוב לשים את סוג המשתנה הנכון אחרי הפור
# print (up_words)

# low_words=["facts","elon musk","burgir","banane"]
# up_words=[word*2 for word in low_words] #יוצר לנו רשימה חדשה שבה המילים הוכפלו 
# print (up_words)


#Q1
# strings=["foo","bar","baz"]
# firstletter=[word[0] for word in strings] #יוצר רשימה של האותיות הראשונות של כל מילה
# print (firstletter)

#Q2
# nums=[1,2,3,4,5]
# sqrnums=[x for x in nums if float(x**0.5)==int(x**0.5)] #לא מה שהתבקשתי אבל זה יוצר רשימה רק של מספרים עם שורשים שלמים
# print (sqrnums)

# nums=[1,2,3,4,5]
# sqrnums=[x**2 for x in nums] #יוצר רשימה של כל המספרים בריבוע
# print (sqrnums)

#Q3
# nums=[1,2,3,4,5,6,7,8]
# even_nums=[x for x in nums if x%2==0] #יוצר רשימה של מספרים זוגיים
# print (even_nums)

#Q4
# list1=[1,2,3] #פעולה שתיצור לנו רשימה מחוברת של סכום המספרים בכל אינדקס
# list2=[4,5,6]
# list_unite=[x+y for x,y in zip(list1,list2)] #זיפ יוצר לנו טופל משני איברים. במקרה הזה, 2 מספרים בכל פעם.
# print (list_unite)

#Q5
# strings=["foo","bar","baz","Messi"] #תמיין את הליסט למילון שבו השם יהיה מפתח והאורך יהיה הערך
# dic={x:len(x) for x in strings} #לא משנה מה האות שאבחר העיקר שהיא תלווה לאורך כל השורה
# print (dic)

# strings=["foo","bar","baz","Messi"] #תמיין את הליסט למילון שבו האורך יהיה מפתח והשם יהיה הערך
# dict = {}
# [dict.update({len(x): dict.get(len(x), []) + [x]}) for x in strings] #עדכון מילון כאשר יש לנו פונקציית גט שלוקחת את הערך ומוסיפה אותו לרשימה ומשייכת אותו למפתח שהוא האורך
# print (dict) # בעצם אנחנו נראה פה רשימה ריקה שמוספת לרשימה עם הסטרינג והרשימה עם הסטרינג תתווסף לרשימה הנכונה לפי אורך (מפתח)

# test=[1,3,4] +[5] #חיבור רשימות הופך אותם לרשימה אחת גדולה 
# print (test)
#Q6
# strings=["bad","mad","glad"]
# newstrings=[word for word in strings if word!="mad"] #יוצר רשימה חדשה עם המילים שאינם מד
# print (newstrings)

#Q7
# strings=["foo","bar","baz"]
# count=len([word for word in strings if "a" in word]) #סופר כמה מילים עם האות איי יש ברשימה החדשה שיצרנו
# print (count)

#Q8
# nums=[1,2,3,4]
# x10nums=[x*10 for x in nums] #דרך מתמטית לעשות את זה
# print (x10nums)

# x10nums2=[str(x)+"0" for x in nums] #דרך תווים לעשות את זה
# print (x10nums2)

#Q9
# strings=["foo","bar","baz","",""]
# new_string=[word for word in strings if word!=""] #דרך למחוק איברים ריקים
# print (new_string)

def main(): #קשור לש.ב.5
    print ("Hello World")
if __name__=="__main__":
    print (__name__)