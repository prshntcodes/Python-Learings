class Student:
    SUBJECTS:list = ["Phys","Chem","Maths"]  # class variable

    def __init__(self):
        self.students:list = []   # instance variable

#----------Avoding entry of student with same roll number----------------
    def roll_exists(self,roll):
        for student in self.students:
            if student['roll'] == roll:
                return True
            return False

#-----------Search by roll number ----------
    def search_details(self):
        roll = int(input("Enter the Roll No. to search:"))

        for student in self.students:
            if student["roll"] == roll:
                print("\n🔎 Student Found:")
                print(f"Name : {student['fname']} {student['lname']}")
                #print(f"Roll No : {student['roll']}")

                for sub, mark in student["marks"].items():
                    print(f"▶️ {sub} : {mark}")

                print()
                return

        print("❌ Student Not Found ❌\n")
        
#------------ Adding Details ------------
    def add_details(self, fname, lname, roll):

        if self.roll_exists(roll):
            print("❌ Roll number already exists , cannot add the student❌.\n📩Please use a unique roll number.")
            return

        marks_record : dict = {}

        for subject in Student.SUBJECTS:
            mark = float(input(f"Enter mark for {subject}: "))
            marks_record[subject] = mark

        details = {
            "fname":fname,
            "lname":lname,
            "roll":roll,
            "marks":marks_record
        }

        self.students.append(details)
        print("Details added successfully ✅\n")


#------------ Displaying ------------
    def display_details(self):
        if not self.students:
            print("\n❌ No students in the Database to display.❌\n")
            return

        print("\n💻 Displaying Student Details:")
        for student in self.students:
            print(f"Name : {student['fname']} {student['lname']} | Roll No : {student['roll']} ")
            for sub, mark in student['marks'].items():
                print(f"▶️ {sub} : {mark}")
            print("\n")
        print("✅Complete Students Details Displayed✅")

#------------ Updating ------------
    def update_details(self):
        roll = int(input("Enter Roll No. of student to be updated: "))

        for student in self.students:
            if student['roll']==roll:
                print("\n")
                print("1.Update Name")
                print("2.Update Roll")
                print("3.Update Marks")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    student['fname'] = input("Enter new  first name: ")
                    student['lname'] = input("Enter new  last name: ")
                    
                elif choice==2:
                    student['roll'] = int(input("Enter new roll number:"))

                elif choice==3:
                    print(f"Available subjects to update mark:{Student.SUBJECTS}")
                    sub = input("Enter a subject to update mark:")

                    if sub in Student.SUBJECTS:
                        mark = float(input(f"Enter new mark for {sub}: "))
                        student["marks"][sub]= mark
                    else:
                        print('Invalid Subject ❌❌')
                        return
                else:
                    print("❌Please select appropiate option.❌")
                    return

                print("Student Details Updated ✅")
                return
            
        print("❌ Student Not Found ❌ \n")

#------------ Removing ------------
    def remove_details(self):
        roll = int(input("Enter roll no to remove: "))

        for student in self.students:
            if student['roll'] == roll:
                self.students.remove(student)
                print("Details Removed Successfully✅ \n")
                return
            
        print("\n❌ No such student exists in database. ❌")

#------------ Main Function ------------
def main():
    reference = Student()
    while True:
        print("\n--------Choose an option.-------")
        print("1.Add details")
        print("2.Display details")
        print("3.Update Details")
        print("4.Remove Details")
        print("5.Search Student")
        print("6.Exit")
        print("------------------------------------")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid Input. Please choose a correct option. \n")
            continue


        if choice == 1:
            fname = input("Enter first name: ")
            lname = input("Enter last name: ")
            roll = int(input("Enter roll number: "))
            reference.add_details(fname,lname,roll)

        elif choice==2:
            reference.display_details()

        elif choice==3:
            reference.update_details()

        elif choice==4:
            reference.remove_details()

        elif choice==5:
                    reference.search_details()

        elif choice==6:
            print("....Exiting....")
            break

        else:
            print("Invalid Input \n")

#------------ Running the Main Function ----------
if __name__ == "__main__":
    main()