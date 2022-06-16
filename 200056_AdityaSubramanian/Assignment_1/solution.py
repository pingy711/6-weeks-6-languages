from operator import truediv


class Member:
    def __init__(self,id,name,username,phone_number,dob):
        self.name = name
        self.id = id
        self.username = username
        self.phone_number = phone_number
        self.dob = dob
        self.age=0
    def update_info_by_id(self,id):
        if(self.id!=id):
            print("Cannot access this id, you are not authorized. Please retry with your id")
        else:
            print("You have been authorized, kindly enter the updated details below. If you do not wish to change it kindly enter the current details.")
            self.name = input(" Your current name is {}. Enter updated name: ".format(self.name))
            self.username = input("Your current username is {}. Enter updated username: ".format(self.username))
            self.phone_number = int(input("Your current number is {}. Enter updated number: ".format(self.phone_number)))
            self.age = int(input("Enter your age: "))
            update_dob = input("Your current dob is {}. Do you wish to update it? (Y/N)".format(self.dob))
            if(update_dob=='Y' or update_dob=='y'):
                self.dob = input("Enter updated dob as ddmmyyyy")
    def display_info_by_id(self,id):
        if(self.id!=id):
            print("You are not authorized to view this page. Retry with your own id")
        else:
            print("Name: {}\nUsername: {}\nPhone number: {}\nDate of birth: {}".format(self.name,self.username,self.phone_number,self.dob))
    def contact_details(self):
        print("Phone number of {} is {}.".format(self.name,self.phone_number))
    def display_age(self):
        if(self.age==0):
            print("Age not updated, please update personal information first!")
        else:
            print(self.age)
class Professor(Member):
    def __init__(self,id,name,username,phone_number,dob,field,attendance):
        Member.__init__(self,id,name,username,phone_number,dob)
        self.field = field
        self.attendance = attendance
    def travel_ticket_discount(self,ticket_price):
        if(self.age==0):
            print("Please update your age and retry")
        else:
            if(self.age<=12):
                return 0
            elif(self.age<=25):
                return ticket_price/2
            else:
                return ticket_price
    def attendance_is_ok(self):
        if(self.attendance>=90):
            return True
        else:
            return False
    def display_info_by_id(self,id):
        if(self.id!=id):
            print("You are not authorized to view this page. Retry with your own id")
        else:
            print("Name: {}\nUsername: {}\nPhone number: {}\nDate of birth: {}\nField: {}".format(self.name,self.username,self.phone_number,self.dob,self.field))
class Student(Member):
    def __init__(self,id,name,username,phone_number,dob,branch,attendance):
        Member.__init__(self,id,name,username,phone_number,dob)
        self.branch = branch
        self.attendance = attendance
    def travel_ticket_discount(self,ticket_price):
        if(self.age==0):
            print("Please update your age and retry")
        else:
            if(self.age<=12):
                return 0
            elif(self.age<=25):
                return ticket_price/2
            else:
                return ticket_price
    def attendance_is_ok(self):
        if(self.attendance>=75):
            return True
        else:
            return False
    def display_info_by_id(self,id):
        if(self.id!=id):
            print("You are not authorized to view this page. Retry with your own id")
        else:
            print("Name: {}\nUsername: {}\nPhone number: {}\nDate of birth: {}\nBranch: {}".format(self.name,self.username,self.phone_number,self.dob,self.branch))
