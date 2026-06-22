emp = []
def add():
    try:
         emp_id = int(input("Enter id: "))
    except ValueError:
        print("Enter valid number: ")
        return
    for i in emp:
        if i["id"] == emp_id:
            print("This id already exist")
            return
    emp_name = input("Enter name: ")
    emp_dep = input("Enter department: ")
    try:
        emp_salary = int(input("Enter salary: "))
    except ValueError:
        print("Enter valid salary: ")
        return
    employee = {
        "id" : emp_id, "name" : emp_name, "department" : emp_dep, "salary" : emp_salary
    }
    emp.append(employee)
def view():
    if emp:
        for i in emp:
           
            print("ID: ",i["id"])
            print("Name: ",i["name"])
            print('Department: ',i["department"])
            print("Salary: ",i["salary"])
            print()
          
    else:
        print("No employees found")
def search():
    if emp:
        found = False
        try:
            val = int(input("Enter id:"))
        except ValueError:
            print("Enter valid id:")
            return
        for i in emp:
            if i["id"] == val:
                print("Found")
                print("ID: ",i["id"])
                print("Name: ",i["name"])
                print("Department: ",i["department"])
                print("Salary: ",i["salary"])
                found = True
        if not found:
            print("This employee not found")
    else:
        print("No employee found")
def delete():
    if emp:
        found = False
        try:
            val = int(input("Enter id: "))
        except ValueError:
            print("Enter valid number: ")
            return
        for i in emp:
            if i["id"] == val:
                emp.remove(i)
                print("Deleted successfully")
                found = True
                return
        if not found:
            print("this employee not found")
    else:
        print("No employee found")
def update():
    if emp:
        found = False
        try:
            val = int(input("Enter id: "))
        except ValueError:
            print("Enter valid id: ")
            return
        for i in emp:
            if i["id"] == val:
                try:
                    newid = int(input("Enter new id: "))
                except ValueError:
                    print("Enter valid number: ")
                    return
                for j in emp:

                   if j["id"] == newid and newid != val:
                        print("Already exist")
                        return
                    
                newname = input("Enter new name: ")
                newdep = input("Enter new department: ")
                try:
                    newsalary = int(input("Enter new salary: "))
                except ValueError:
                    print("Enter valid salary: ")
                    return
                
                i["id"] = newid
                i["name"] = newname
                i["department"] = newdep
                i["salary"] = newsalary
                print("Updated successfully")
                found = True
                break
                    
        if not found:
            print("Employee not found")
    else:
        print("No employee found")
def totalSalary():
    if emp:
        total = 0
        for i in emp:
            total = total + i["salary"]
        print("Total salary is: ",total)
    else:
        print("No employee")
def averageSalary():
    if emp:
         total = 0
         count = len(emp)
         for i in emp:
            total = total + i["salary"]
         print("Average salary is: {:.2f}".format(total/count))
    else:
        print("No employee")
        
def countemp():
    if emp:
        count = len(emp)
        print("No of employees: ",count)
    else:
        print("No employee")
def highSalary():
    if emp:
        highest = emp[0]
        for i in emp:
            
            if i["salary"] > highest["salary"]:
               highest = i
        print("Highest salary is: ",highest["salary"])
        print("Id: ",highest["id"])   
        print("Name: ",highest["name"])
        print("Department: ",highest["department"])
    else:
        print("No employee")
def lowSalary():
    if emp:
        lowest = emp[0]
        for i in emp:
            if i["salary"] < lowest["salary"]:
                lowest = i
        print("Lowest salary: ",lowest["salary"])
        print("Id: ",lowest["id"])
        print("Name: ",lowest["name"])
        print("Department: ",lowest["department"])
    else:
        print("No employee")
def searchByDepartment():
    if emp:
        dep = input("Enter department: ")
        found = False
        for i in emp:
            if i["department"].lower() == dep.lower():
                print("ID: ",i["id"])
                print("Name: ",i["name"])
                print("Department: ",i["department"])
                print("Salary: ",i["salary"])
                print()
                found = True
        if not found:
            print("No employee in this department")
    else:
        print("No employee")
def empCountByDep():
    if emp:
        dep = input("Enter department:")
        count = 0
        for i in emp:
            if i["department"].lower() == dep.lower():
                count = count + 1
        if count > 0:
            print("Department: ",dep)
            print("No of employees: ",count) 
        else:
            print("No employee in this department")
    else:
        print("No employee")
def sortEmpBySalary():
    if emp:
        sort_list = sorted(emp, key=lambda x: x["salary"], reverse=True)
        for i in sort_list:
            print("ID: ",i["id"])
            print("Name: ",i["name"])
            print("Department: ",i["department"])
            print("Salary: ",i["salary"])
            print()
    else:
        print("No employee")
def sortByName():
    if emp:
         sort_list = sorted(emp, key=lambda x:x["name"].lower())
         for i in sort_list:
             print("ID: ",i["id"])
             print("Name: ",i["name"])
             print("Department: ",i["department"])
             print("Salary: ",i["salary"])
             print()
    else:
        print("No employee")
def empAboveAvgSalary():
    if emp:
        found = False
        total = 0
        for i in emp:
            total = total + i["salary"]
        Avg = total/len(emp)
        
        for i in emp:
            if i["salary"] > Avg:
                print("ID: ",i["id"])
                print("Name: ",i["name"])
                print("Department: ",i["department"])
                print("Salary: ",i["salary"])
                print()
                found = True
        if not found:
            print("No employees above average salary")
    else:
        print("No employee")
def secondHighSalary():
    if emp:
        if len(emp) < 2:
            print("Need atleast 2 employees")
            return
        else:
            sort_list = sorted(emp, key=lambda x: x["salary"], reverse=True)
            sec = sort_list[1]
            print("ID:",sec["id"])
            print("Name: ",sec["name"])
            print("Department: ",sec["department"])
            print("Salary: ",sec["salary"])
    else:
        print("No employee")
def thirdHighSalary():
    if emp:
        if len(emp) <3:
            print("Need atlest 3 employees")
            return
        else:
            sort_list = sorted(emp, key=lambda x: x["salary"], reverse=True)
            third = sort_list[2]
            print("ID:",third["id"])
            print("Name:",third["name"])
            print("Department:",third["department"])
            print("Salary:",third["salary"])
    else:
        print("No employee")
def saveFile():
    if emp:
        with open("emp_data.txt","w") as file:
            for i in emp:
                file.write(f'{i["id"]},{i["name"]},{i["department"]},{i["salary"]}\n')
            print("Data saved successfully")
        
    else:
        print("No data")
def loadFile():
    try:
        with open("emp_data.txt","r") as f:
            emp.clear()
            for line in f:
                data = line.strip().split(",")
                employee = {
                            "id" : int(data[0]),
                            "name" : data[1],
                            "department" : data[2],
                            "salary" : int(data[3])
                            }
                emp.append(employee)
            print("Data loaded successfully")
    except FileNotFoundError:
        print("File not found")
def searchByname():
    if emp:
        name = input("Enter the name: ")
        found = False
        for i in emp:
            if i["name"].lower() == name.lower():
                print("Found")
                print("ID :",i["id"])
                print("Name :",i["name"])
                print("Department :",i["department"])
                print("Salary :",i["salary"])
                found = True
        if not found:
            print("Not found")
    else:
        print("No employee")
def depSalary():
    if emp:
          found = False
          dep = input("Enter department: ")
          salary = 0
          for i in emp:
              if i["department"].lower() == dep.lower():
                  salary += i["salary"]
                  found = True
          if found == True:
              print("Total salary of ",dep,"dep: ",salary)
          else:
              print("No employees in this department")
    else:
        print("No employee")
def remEmployee():
    if emp:
        emp.clear()
        print("Removed successfully")
    else:
        print("No employee")

def depEmp():
    if emp:
        dep = input("Enter department")
        found = False
        for i in emp:
            if i["department"].lower() == dep.lower():
                print("ID:",i['id'])
                print("Name:",i["name"])
                print("Department:",i["department"])
                print("Salary:",i["salary"])
                print()
                found = True
        if not found:
            print("No employees in this department")
    else:
        print("No employee")
def exportCsv():
    if emp:
        with open("employees.csv","w") as f:
            f.write("ID,NAME,DEPARTMENT,SALARY\n")
            for i in emp:
                f.write(f"{i['id']},{i['name']},{i['department']},{i['salary']}\n")
                
            print("Export to csv successfully")   

    else:
        print("No employee")
def empBySalaryRange():
    if emp:
        found = False
        try:
            minsal = int(input("Enter minimum range"))
            maxsal = int(input("Enter maximum range"))
        except ValueError:
            print("Enter valid input")
            return
        for i in emp:
            if i["salary"] >= minsal and i["salary"] <=maxsal:
                print("ID ",i["id"])
                print("Name ",i["name"])
                print("Department ",i["department"])
                print("Salary ",i["salary"])
                print()
                found = True
        if not found:
            print("No employee in between this range")
    else:
        print("No employee")

def increaseSalary():
    if emp:
        try:
            percentage = float(input("Enter percentage"))
        except ValueError:
            print("Enter valid input")
            return
        for i in emp:
            i["salary"] += i["salary"] * percentage / 100
        print("Salary updated successfully")
    else:
        print("No employee")
def increaseSalByDep():
    if emp:
        found = False
        dep = input("Enter department")
        try:
            percentage = float(input("Enter increment percentage"))
        except ValueError:
            print("Enter valid input")
            return
        for i in emp:
            if i["department"].lower() == dep.lower():
                i["salary"] = round(i["salary"] * (1 + percentage / 100), 2)
                found = True
        if not found:
            print("No employee in this department")
    else:
        print("No employees")
def lowSalByDep():
    if emp:
        dep = input("Enter department")
        dept_salary = []
        for i in emp:
            if i["department"].lower() == dep.lower():
                dept_salary.append(i)
        if dept_salary:
            lowest = min(dept_salary, key=lambda x: x["salary"])
            print("Lowest salary is ", lowest["salary"])
            print("ID ",lowest["id"])
            print("Name ",lowest["name"])
            print("Department ",lowest["department"])
            
        else:
            print("No employee in this department")
    else:
        print("No employee")

def highsalByDep():
    if emp:
      
        dep = input("Enter department")
        dept_salary = []
        for i in emp:
            if i["department"].lower() == dep.lower():
                dept_salary.append(i)
        if dept_salary:
            highest = max(dept_salary, key=lambda x: x["salary"])
            print("Highest salary is ",highest["salary"])
            print("ID ",highest["id"])
            print("Name ",highest["name"])
            print("Department ",highest["department"])
            
        else:
            print("No employee in this department")
    else:
        print("No employees")

def AvgSalByDep():
    if emp:
       
        dep = input("Enter department")
        total_Salary = count = 0
        for i in emp:
            if i["department"].lower() == dep.lower():
                total_Salary += i["salary"]
                count += 1
                
        if count > 0:
            print("average salary is ",total_Salary / count)
        else:
        
            print("No employee in this department")
    else:
        print("No employees")

        
while True:
    print("1.Add Employee")
    print("2.View Employees")
    print("3.Search Employee")
    print("4.Delete Employee")
    print("5.Update Employee")
    print("6.total salary")
    print('7.count employee')
    print("8.highest salary")
    print("9.lowest salary")
    print("10.Average salary")
    print("11.Search By Department")
    print("12.Employee Count By Department")
    print("13.sort By Salary")
    print("14.Sort by name")
    print("15.Employees above average salary")
    print("16.Second highest salary")
    print("17.Save file")
    print("18.loadFile")
    print("19.Search by name")
    print("20.Department wise salary")
    print("21.Remove Employee")
    print("22.Third High Salary")
    print("23.Department wise Employee list")
    print("24.Export to Csv file")
    print("25.Emmployee by salary range")
    print("26.Increase salary")
    print("27.Increase salary by department")
    print("28.Lowest salary by department")
    print("29.Lowest salary by department")
    print("30.Average salary by department")
    print("31.Exit")
    try:
        choice = int(input("enter your choice"))
    except ValueError:
        print("enter valid choice")
        continue
    if choice == 1:
        add()
    elif choice == 2:
        view()
    elif choice == 3:
        search()
    elif choice == 4:
        delete()
    elif choice == 5:
        update()
    elif choice == 6:
        totalSalary()
    elif choice == 7:
        countemp()
    elif choice == 8:
        highSalary()
    elif choice == 9:
        lowSalary()
    elif choice == 10:
        averageSalary()
    elif choice == 11:
        searchByDepartment()
    elif choice == 12:
        empCountByDep()
    elif choice == 13:
        sortEmpBySalary()
    elif choice == 14:
        sortByName()
    elif choice == 15:
        empAboveAvgSalary()
    elif choice == 16:
        secondHighSalary()
    elif choice == 17:
        saveFile()
    elif choice == 18:
        loadFile()
    elif choice == 19:
        searchByname()
    elif choice == 20:
        depSalary()
    elif choice == 21:
        remEmployee()
    elif choice == 22:
        thirdHighSalary()
    elif choice == 23:
        depEmp()
    elif choice == 24:
        exportCsv()
    elif choice == 25:
        empBySalaryRange()
    elif choice == 26:
        increaseSalary()
    elif choice == 27:
        increaseSalByDep()
    elif choice == 28:
        lowSalByDep()
    elif choice == 29:
        highsalByDep()
    elif choice == 30:
        AvgSalByDep()
    elif choice == 31:
        break
    else:
        print("Enter valid choice")
    

    


