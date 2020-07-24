#in this program our script not only takes in the data but also saves it in a document
from datetime import date

today_date = str(date.today())
today_list = [today_date]
infl = open('todo list\just_for_the_record','w')

def add_new():
    ina = input("what task do you wish to add? \n")
    today_list.append(ina)

def clear_list():
    today_list.clear()

def activity_completed():
    inr = input("which activity have you completed? \n")
    today_list.remove(inr)

def correction_to_the_list():
    inrp1 = input("what do you wanna replace \n")
    today_list.remove(inrp1)
    inrp2 = input("what is the updated task \n")
    today_list.append(inrp2)

def closemYfilE():
    for element in today_list:
        infl.write(element)
        infl.write("\n")

    infl.close()
    
def start():
    print("today is " + str(today_date))
    in1 = input("what do wish to do? \n")

    if in1 == "an":
        add_new()
        start()


    elif in1 == "AddNew" :
        add_new()
        start()

    elif in1 == "CleanList" :
        clear_list()
        start()

    elif in1 == "JobDone" :
        activity_completed()
        start()

    elif in1 == "ReplaceActivity" :
        correction_to_the_list()
        start()

    elif in1 == "ShowList" :
        for element in today_list:
            print(element)
        start()

    elif in1 == "close":
        closemYfilE()
        print("app closed")

     
    else:
        start()

start()

#an or AddNew 
#JobDone
#ReplaceActivity
#close
#CleanList
