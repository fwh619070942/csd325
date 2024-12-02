def main():
  #promt the file number.
  filename = input("Enter the file name: ")
  filename = filename + ".txt"
  user='y'
  security_commands = ['rm', 'cp', 'mv', 'ls', 'pwd', 'cd', 'mkdir', 'cat', 'cat_dir', 'exit']
  #open the file as write mode.
  with open(filename, 'w') as infile:
    while user == 'y' or user == 'Y':
        #Get the users information
        print('Enter the following data:')
      
        #input validation for first name
        first_name = input('First name: ')
        while not first_name.isalpha() or any(command in first_name for command in security_commands):
          if not first_name.isalpha():
            print("Invalid input. Please enter only alphabetic characters")
          elif any(command in first_name for command in security_commands):
            print("Input contains potential security commands. Please reenter.")
          first_name = input('First name: ')
          
        #input validation for last name
        last_name = input('Last name: ')
        while not last_name.isalpha() or any(command in last_name for command in security_commands):
          if not last_name.isalpha():
            print("Invalid input. Please enter only alphabetic characters")
          elif any(command in last_name for command in security_commands):
            print("Input contains potential security commands. Please reenter.")
          last_name = input('Last name: ')
          print("Invalid input. Please enter only alphabetic characters")
          last_name = input('Last name: ')

        #input validation for address
        street_address = input('Street address: ')
        while any(command in street_address for command in security_commands):
          print("Input contains potential security commands. please reenter.")
          street_address = input('Street address: ')
      
        #input validation for phone number
        phone_number = input('Phone number: ')
        while not phone_number.isdigit() or any(command in phone_number for command in security_commands):
          if not phone_number.isdigit():
            print("Invalid input. Please enter only numeric characters")
          elif any(command in phone_number for command in security_commands):
            print("Input contains potential security commands. Please reenter.")
          phone_number = input('Phone number: ')
          
        #write the data to the file.
        infile.write(f'{first_name}, {last_name}, {street_address}, {phone_number}')
        print("Do you want to add another user's information?")
        user = input("Enter 'Y' for yes, else = no: ")
  print("Data appended to the file.")

  with open(filename, 'r') as outfile:
      line = outfile.readline()
      print(line)

if __name__ == "__main__":
    main()
