try:
    import json
except ImportError:
    print('This program requires the json module, please try it again')
    json.exit()
    

"""Define filename"""
fileName = '../csd325/module-8/student.json'

"""Define New student info"""
new_student_info = {  
        "F_Name": 'Weihao', 
        "L_Name": 'Fu', 
        "Student_ID": 123456, 
        "Email": "abcwf@gmail.com" }

def main():
    Read_Student_File(fileName)
    print("You have successfully read the file")

    Append_Student_File(fileName, new_student_info)
    print("You have successfully append the new student to the existing file")

def Read_Student_File(fileName):

    """read file as JSON file"""
    try:
        with open (fileName, 'r') as fp:
            data = json.load(fp)
            print(type(data))
            print(data)

            """print last name, firstname, id, and email from the json file"""
            print("This is the original student list: ")
            for student in data:
                print(f'{student.get('L_Name')}, {student.get('F_Name')}: ID = {student.get('Student_ID')}, Email = {student.get('Email')}')
            
            return data
    except FileNotFoundError:
        print('The file is not found')

def Append_Student_File(fileName, new_student_info):
    """Append new student data"""
    data = Read_Student_File(fileName)
    data.append(new_student_info)
    print (f'This is the updated Student list: \n{data}')

    """Write the updated data into the file"""
    try:
        with open(fileName, 'w') as json_file:
            json.dump(data, json_file, indent=4, separators = (',', ':'))
        print("The JSON file was updated")
    except FileNotFoundError:
        print("The file is not found")




if __name__ == '__main__':
    try:
        main()
    except:
        json.exit



