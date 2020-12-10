# --------------------------------------------------------------- #
# Title: Test Harness
# Description: Test harness to ensure that all modules are working
#
# ChangeLog (Who,When,What):
# T.Ward, 12-08-20, Created script
# --------------------------------------------------------------- #

if __name__ == "__main__":
    from DataClasses import Person as P
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported.")

# Test the Person class from DataClasses
print("\nTesting the Person class from DataClasses")
lstTable = []
objP1 = P("Theresa", "Ward")
objP2 = P("Michael", "Williams")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test the Employee class from DataClasses
print("\nTesting the Employee class from DataClasses")
lstTable = []
objEmp1 = Emp(1, "Theresa", "Ward")
objEmp2 = Emp(2, "Michael", "Williams")
lstTable = [objEmp1, objEmp2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module from ProcessingClasses.
# I've decided to check read_data_to_file instead
print("\nTesting the processing module from DataClasses")
lstTable = []
Fp.read_data_from_file("EmployeeData.txt")
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

# Test the EmployeeIO class from IOClasses
print("\nTesting the EmployeeIO class from IOClasses")
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())
