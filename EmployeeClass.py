class EmployeeClass:
    def __init__(self, name,IDnumber,department,jobTitle, monthlySalary):
        self.__name = name
        self.__IDnumber = IDnumber
        self.__department = department
        self.__jobTitle = jobTitle
        self.__monthlySalary = monthlySalary
        
    def getName(self):
        return self.__name

    def getIDnumber(self):
        return self.__IDnumber
    
    def getDepartment(self):
        return self.__department

    def getjobTitle(self):
        return self.__jobTitle

    def getmonthlySalary(self):
        return self.__monthlySalary
