# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# T. Ward, 12-09-20,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #

if __name__ == "__main__":
    print("This file is the starting point of my program!")
    # Will error if the modules are not found
    from ProcessingClasses import FileProcessor as Fp
    from DataClasses import Employee as Emp
    from IOClasses import EmployeeIO as Eio

else:
    raise Exception("This file was not created to be imported")


# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee objects when script starts
lstTable = []
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))

while True:

    try:
        # Show user a menu of options
        Eio.print_menu_items()
        # Get user's menu option choice
        choice = Eio.input_menu_options()

        if choice == "1": # Show user current data in the list of employee objects
            Eio.print_current_list_items(lstTable)

        if choice == "2": # Let user add data to the list of employee objects
            lstTable.append(Eio.input_employee_data())

        if choice == "3": # Let user save current data to file
            Fp.save_data_to_file("EmployeeData.txt", lstTable)

        elif choice == "4": # Let user exit program
            print("Goodbye!")
            break

        else:
            print("Please enter a valid choice.  Try again. ")

    except ValueError as e:
        print("The built-in Python error message is: ")
        print(e, "\n")

# Main Body of Script  ---------------------------------------------------- #
