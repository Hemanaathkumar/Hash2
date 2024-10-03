# Sample employee data
employees = [
    {'EmployeeID': 'E02001', 'Name': 'John Doe', 'Gender': 'Male', 'Department': 'IT'},
    {'EmployeeID': 'E02002', 'Name': 'Jane Smith', 'Gender': 'Female', 'Department': 'HR'},
    {'EmployeeID': 'E02003', 'Name': 'Sam Green', 'Gender': 'Male', 'Department': 'Finance'},
    {'EmployeeID': 'E02004', 'Name': 'Chris Brown', 'Gender': 'Male', 'Department': 'IT'},
]

collections = {}


def createCollection(p_collection_name):
    collections[p_collection_name] = []
    print(f"Collection '{p_collection_name}' created.")

def indexData(p_collection_name, p_exclude_column):
    if p_collection_name in collections:
        for employee in employees:
            indexed_employee = {key: value for key, value in employee.items() if key != p_exclude_column}
            collections[p_collection_name].append(indexed_employee)
        print(f"Data indexed into '{p_collection_name}', excluding column '{p_exclude_column}'.")

def searchByColumn(p_collection_name, p_column_name, p_column_value):
    if p_collection_name in collections:
        result = [emp for emp in collections[p_collection_name] if emp.get(p_column_name) == p_column_value]
        print(f"Search results for {p_column_name} = {p_column_value}: {result}")
        return result

def getEmpCount(p_collection_name):
    if p_collection_name in collections:
        count = len(collections[p_collection_name])
        print(f"Employee count in '{p_collection_name}': {count}")
        return count

def delEmpById(p_collection_name, p_employee_id):
    if p_collection_name in collections:
        collections[p_collection_name] = [emp for emp in collections[p_collection_name] if emp.get('EmployeeID') != p_employee_id]
        print(f"Employee with ID '{p_employee_id}' deleted from '{p_collection_name}'.")

def getDepFacet(p_collection_name):
    if p_collection_name in collections:
        department_count = {}
        for emp in collections[p_collection_name]:
            department = emp.get('Department')
            if department:
                department_count[department] = department_count.get(department, 0) + 1
        print(f"Department facet for '{p_collection_name}': {department_count}")
        return department_count

# Variable Definitions
v_nameCollection = 'Hash_JohnDoe'
v_phoneCollection = 'Hash_1234'

# Function Executions
createCollection(v_nameCollection)
createCollection(v_phoneCollection)

getEmpCount(v_nameCollection)

indexData(v_nameCollection, 'Department')
indexData(v_phoneCollection, 'Gender')

delEmpById(v_nameCollection, 'E02003')
getEmpCount(v_nameCollection)

searchByColumn(v_nameCollection, 'Department', 'IT')
searchByColumn(v_nameCollection, 'Gender', 'Male')
searchByColumn(v_phoneCollection, 'Department', 'IT')

getDepFacet(v_nameCollection)
getDepFacet(v_phoneCollection)