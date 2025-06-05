import requests

# url = "https://v2.jokeapi.dev/joke/Any?type=twopart&idRange=0-10"

# response = requests.get(url)

# # print (response) #נותן מספר תגובה
# # print (response.text) #נותן את כל ערך המילון

# joke_dict= response.json() #שומר את המילון
# print (joke_dict)
# print (type(joke_dict)) #מראה לנו שמדובר במילון
# print (joke_dict["setup"],joke_dict["delivery"])

# url="https://api.spacexdata.com/v4/capsules"
# resp=requests.get(url)

# if resp.status_code !=200:
#     raise Exception("Get /capsules/ {}".format(resp.status_code))

# for item in resp.json():
#     print('Capsule Serial: {} Capsule Type: {} \\nStatus: {} \\nLast Update: {} \\n\\n'.format(item['serial'], item['type'], item['status'], item['last_update']))

# url="https://api.github.com/repos/microsoft/vscode/issues"
# response = requests.get(url)
# issues= response.json ()

# for issue in issues:
#     print (issue["title"])


#API Exercises
#Q1
# import time

# url = "https://official-joke-api.appspot.com/jokes/random"

# response = requests.get(url)

# print (response) #נותן מספר תגובה
# print (response.text) #נותן את כל ערך המילון

# joke_dict= response.json() #שומר את המילון
# while True:
#     response = requests.get(url)

#     if response.status_code==429:
#         time.sleep(5)
#         print("יותר מדי בקשות, ממתין 5 שניות...")
#         continue
#     joke_dict= response.json()
#     if "banana" in joke_dict["setup"] or "banana" in joke_dict["punchline"]:
#         print (joke_dict["setup"],joke_dict["punchline"])
#         break
#     time.sleep(1) 

#Q2

# url = "https://official-joke-api.appspot.com/jokes/random"

# response = requests.get(url)
# ratings={}
# joke_dict= response.json() #שומר את המילון
# for i in range (10):
#     response = requests.get(url)
#     joke_dict= response.json()
#     print (joke_dict["setup"],joke_dict["punchline"])
#     rating_joke=float(input("Rate this joke from 1-10:"))
#     ratings[i]=rating_joke
# average=sum(ratings.values())/len(ratings)
# print(f"Average rating: {average}")

#Q3
# url = "https://official-joke-api.appspot.com/jokes/random"

# response = requests.get(url)
# joke_dict= response.json() #שומר את המילון
# setup=joke_dict["setup"]
# punchline=joke_dict["punchline"]
# print (setup)
# print (punchline)

#Q4
# url = "https://official-joke-api.appspot.com/jokes/random"
# response = requests.get(url)
# ratings={}
# joke_dict= response.json() #שומר את המילון
# for i in range (10):
#     response = requests.get(url)
#     joke_dict= response.json()
#     if len(joke_dict["setup"])+len(joke_dict["punchline"])>50:
#         print (joke_dict["setup"],joke_dict["punchline"])
    
#Q5

# bad_words=["What","what","Why","why","Fuck","because","Because"]
# def filter_joke(joke):
#     setup=joke["setup"]
#     punchline=joke["punchline"]
#     for word in bad_words: #על כל מילה רעה שקיימת
#         setup=setup.replace(word,"*"* len(word)) #נחליף את המילה הרעה בסטאפ באורכה בכוכביות, פונקציה חדשה
#         punchline=punchline.replace(word,"*"* len(word)) #נחליף את המילה הרעה בפאנצ'ליין באורכה בכוכביות
#     return setup,punchline #מחזיר 2 ערכים לכן נשווה ל2 ערכים

# url = "https://official-joke-api.appspot.com/jokes/random"
# response = requests.get(url)
# joke_dict= response.json()

# setup,punchline=filter_joke(joke_dict) #פה יש השוואה ל2 ערכים
# print(setup)
# print(punchline)

#Q6
# url = "https://official-joke-api.appspot.com/jokes/random"

# category=input("Enter a Category:")
# params ={"category":category} #מפתח בשם קטגוריה, ערך בשם הקטגוריה הרצויה
# response = requests.get(url,params=params) #זה בעצם מוסיף לשורת יו-אר-אל את הבקשה שהקטגוריה תהיה מה שמופיע בפאראמס
# joke_dict= response.json()
# print(joke_dict["setup"])
# print(joke_dict["punchline"])

#Q7
# url = "https://official-joke-api.appspot.com/jokes/random"
# response = requests.get(url)
# categories={}
# joke_dict= response.json() #שומר את המילון
# for i in range (10):
#     response = requests.get(url)
#     joke_dict= response.json()
#     if joke_dict["type"] in categories:
#         categories[joke_dict["type"]]+=1
#     else:
#         categories[joke_dict["type"]]=1
# print (categories)

#API Exercises 2
#Q1
# url ="https://dog.ceo/api/breeds/list/all"
# response = requests.get(url)
# joke_dict= response.json()
# list=list(joke_dict["message"])
# print(list)

#Q2
# url ="https://dog.ceo/api/breeds/image/random/3"
# response = requests.get(url)
# joke_dict= response.json()
# list=list(joke_dict["message"])
# print(list)

#Q3
# url ="http://jsonplaceholder.typicode.com/posts"
# user_data = {'wannabe': 'Bomba', 'id': '3333', 'title':'oompa loompa','body':'this is a test for tommy'}
# response = requests.post(url, json=user_data)

# if response.status_code in [200,201,204]:
#     print(response.json())
#     print('User added successfully!')

# else:
#     print(f'Failed to add user. Status code: {response.status_code}')

#Q4
# url ="https://api.restful-api.dev/objects"
# user_data = {'id':"a123321",'name': 'Bolly', 'data':{"Stength":"8/10","Height":"184cm","Weight":"78kg","Charimsa":"6/10"} }
# response = requests.post(url, json=user_data)
# print(response.json())
# if response.status_code in [200,201,204]:
#     print('User added successfully!')
# else:
#     print(f'Failed to add user. Status code: {response.status_code}')

#Q5
# url = "https://catfact.ninja/fact"
# response = requests.get(url)
# joke_dict= response.json()
# if response.status_code in [200,201,204]:
#     print(f'Cat Fact: {joke_dict["fact"]}')
# else:
#     print(f'Failed to add user. Status code: {response.status_code}')

#Lambda Functions
# lambda= print ("hello world") #יצרנו פונקציה מהירה וחד פעמית שמדפיסה שלום עולם

#נשתמש במילה למדא במקום במילה דף כדי להגדיר פונקציית למדא.
# greet= lambda:print ("Hello World")
# greet() #יפעיל את הערך וידפיס לנו שלום עולם

# greet_user=lambda name:print (f"Hey there, {name}") #יצרנו פונקציית למדא שמקבלת ערך (שם המבורך)
# greet_user("Tomer") #נשתמש בפונקציה וניתן לה את הערך תומר

# add_numbers= lambda x,y:x+y #יצרנו פונקצית למדא שמקבלת 2 מספרים ומחברת אותם
# sum=add_numbers(5,3)
# print(sum)

# numbers=[1,2,3,4,5]
# squared=list(map(lambda x:x**2,numbers)) #פונקציית המפה מפעילה את למדא לכל אלמנט שיש ברשימה
# print (f"Squared: {squared}")

# numbers=[1,2,3,4,5,6,7,8,9,10]
# even_numbers=list(filter(lambda x:x%2==0,numbers)) #פונקציית פילטר מסננת לנו את הערכים שאנחנו רוצים בלבד
# print (f"The even numbers are: {even_numbers}")

# words= ["apple","banana","cherry","date","eggplant"]
# sorted_words=sorted(words,key=lambda x:len(x)) #מקבל את הליסט ומסדר אותו לפי אורך המילים, 
# #בגדול הפונקציה תחילה רק מודדת את אורך המילים ואז מסדרת אותה
# print (f"Sorted by Length: {sorted_words}")
# sorted_words=sorted(words,key=lambda x:len(x),reverse=True) #פה נדפיס בסדר הפוך
# print (f"Sorted by Length: {sorted_words}")

# people = [
#     {'name': 'Alice', 'age': 30},
#     {'name': 'Bob', 'age': 25},
#     {'name': 'Carol', 'age': 35}
# ]
# #סידור לפי גיל
# sorted_people=sorted(people,key=lambda x:x["age"])
# print (sorted_people)

# Classes and Objects
#אופציה 1
# class Bike:
#     name =""
#     gear= 0

# bike1= Bike ()
# bike1.name="Mountain Bike"
# bike1.gear= 9
# print (bike1.name, bike1.gear)
# bike2= Bike ()
# bike2.name="Tomer's Bike"
# bike1.gear= 1
# print (bike2.name, bike2.gear)


# אופציה 2
# class Bike:
#     total_bikes = 0
#     default_gear=3 #נגדיר ברירת מחדל למקרה שלא יוזן הילוך

#     def __init__(self,name,gear=None): #פונקציית קונסטרקטור (בנייה)
#         self.name=name
#         if gear==None: #אם לא נתנו שום ערך להילוך הוא יהיה אוטומטית מוגדר כמו ברירת המחדל
#             self.gear= Bike.default_gear
#         else:
#             self.gear=gear
#         Bike.total_bikes+=1 #בכל פעם שיוגדר בייק חדש, יתווסף 1

# bike1= Bike (name="Mountain Bike")
# bike2= Bike (name="Tomer's Bike", gear=1)
# print (bike1.gear) #ידפיס 3 (איזה הילוך זה)
# print (bike2.total_bikes) #ידפיס 2 (מספר האופנים ששמרתי)


# class Room:
#     length=0.0
#     breadth=0.0
#     def __init__(self,length,breadth): #קונסטרקטור חשוב
#         self.length=length
#         self.breadth=breadth

#     def calculate_area(self): #פונקציה פנימית בתוך קלאס מסוים
#         print ("Area of Room:", self.length*self.breadth) 

# study_room= Room()
# study_room.length= 4.0
# study_room.breadth=3.5
# study_room.calculate_area() # קריאה לפונקציה, בסופה יש לנו הדפסה של התוצאה

# class Employee:
#     employee_id=0

# employee1=Employee()
# employee2=Employee()

# employee1.employee_id=1001
# employee2.employee_id=1002

# print (employee1.employee_id,employee2.employee_id) #מדפיס את התז שלהם

#Q1
# my_lambda=lambda x:x*2
# print (my_lambda(5))

#Q2
# my_l=lambda x,y:x+y
# print (my_l(5,3))

#Q3
# url = "https://catfact.ninja/fact"
# response = requests.get(url)

#Q4
# url = "https://catfact.ninja/fact"
# response = requests.get(url)
# json_data=response.json()

#Q5
# class Person:
#      def __init__(self,name,age): #פונקציית קונסטרקטור (בנייה)
#         self.name=name 
#         self.age=age
# person1=Person(name="Tomer Samchi",age=25)
# person2=Person(name="Nikol Shvets",age=25)
# print (person1.name,person1.age)
# print (person2.name,person2.age)

#Q6
# class Person:
#     def __init__(self,name,age): #פונקציית קונסטרקטור (בנייה)
#         self.name=name 
#         self.age=age
#     def greet (self):
#         print (f"Hello, {self.name}")
        
# person1=Person("Tomer Samchi",25) #דרך 1
# person2=Person(name="Nikol Shvets",age=25) #דרך 2
# # print (person1.name,person1.age)
# # print (person2.name,person2.age)
# person1.greet() #לא צריך לתת לו ערך משום שהוא לוקח את הסלף של אותו איבר

#Q7
# url = "https://catfact.ninja/fact"
# response = requests.get(url)
# json_data=response.json()
# rev_string=lambda x:x[::-1] #נגדיר פונקציית למדא
# fact=(json_data["fact"]) #נשמור את העובדה
# rev_fact=rev_string(fact) #נהפוך את העובדה בעזרת פונקצית הלמדא שלנו
# print (rev_fact) #נדפיס

# proccesed_data=list(map(lambda x:x*2,json_data)) #ניצור רשימה של המפתחות וכל איבר בה יהיה שם המפתח פעמיים
# print (proccesed_data) #נדפיס את הרשימה


#Project
url = "https://v2.jokeapi.dev/joke/Any"
try:
    response= requests.get(url)
    json_jokes=response.json()
    if response.status_code not in [200,201,204]:
        print ("response code returns error")
    else:
        if json_jokes["type"]=="single":
            print (json_jokes["joke"])
        else:
            print (json_jokes["setup"], json_jokes["delivery"])
except Exception as e: #כל דבר, לא חייב להיות אי
    print ("we have some error")
    print (e) #מדפיס את סוג השגיאה
try:    
    url = "https://v2.jokeapi.dev/joke/Programming" #בדיחות תכנות
    response= requests.get(url)
    json_jokes=response.json()
    if response.status_code not in [200,201,204]:
        print ("response code returns error")
    else:
        if json_jokes["type"]=="single":
            print (json_jokes["joke"])
        else:
            print (json_jokes["setup"], json_jokes["delivery"])
    print (json_jokes["category"])
except Exception as e: #כל דבר, לא חייב להיות אי
    print ("we have some error")
    print (e) #מדפיס את סוג השגיאה