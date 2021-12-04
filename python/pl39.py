import csv
import json

FILENAME_CSV = 'pl39.csv'

def create_csv_example_file():

    write_sucess = False

    # 'with' will close in the end 'f' file descriptor
    # no need to f.close()
    with open(FILENAME_CSV, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        header = ['Department', 'EmpName', 'EmpRole', 'EmpSalary']
        writer.writerow(header)

        # write the data
        row1 = ['DEP_A', 'NAME_A1', 'ROLE_A', '123']
        writer.writerow(row1)
        row1 = ['DEP_A', 'NAME_A2', 'ROLE_A', '123']
        writer.writerow(row1)

        row2 = ['DEP_B', 'NAME_B1', 'ROLE_B', '321']
        writer.writerow(row2)
        row2 = ['DEP_B', 'NAME_B2', 'ROLE_B', '321']
        writer.writerow(row2)

        row3  = ['DEP_C', 'NAME_C1', 'ROLE_C', '222']
        writer.writerow(row3)
        row3  = ['DEP_C', 'NAME_C2', 'ROLE_C', '222']
        writer.writerow(row3)

        write_sucess = True

    return write_sucess



def read_csv_example_file():

    department_dict = dict()

    with open(FILENAME_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            department_key = row['Department']
            emp_name = row['EmpName']
            emp_role = row['EmpRole']
            emp_sal = row['EmpSalary']

            emp_list = [emp_role, emp_sal]
            emp_dict = {emp_name: emp_list}

            if not department_key in department_dict:
                # careful - used ( ) to represent a list with one dict inside
                department_list = list()
                department_list.append(emp_dict)
                department_dict[department_key] = department_list
            else:
                current_dep_list = department_dict[department_key]
                current_dep_list.append(emp_dict)
            
    return department_dict


def save_to_json(dep_dict):

    has_sucess = False
    with open('pl39.json', 'w') as fp:
        json.dump(dep_dict, fp, indent=4, sort_keys=True)
        has_sucess = True
    return has_sucess


has_sucess = create_csv_example_file()
if not has_sucess:
    print("Error!")
    exit(1)

dep_dict = read_csv_example_file()

has_sucess = save_to_json(dep_dict)

if has_sucess:
    print("End!")
else:
    print("Error!")
    exit(1)

