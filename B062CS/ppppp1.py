def get_salary(employee):
    return employee["salary"]

def is_middle_salary(salary, min_salary, max_salary):
    return salary != min_salary and salary != max_salary
def calculate_average(values):
    return sum(values)/len(values) if values else 0
def average_salary_excluding_min_max(employees):
    salaries = list(map(get_salary,employees))
    #print(salaries)
    min_salary = min(salaries)
    max_salary = max(salaries)

    def salary_filter(salary):
        return is_middle_salary(salary, min_salary, max_salary)
    
    middle_salary = list(filter(salary_filter,salaries))
    #print(middle_salary)
    return calculate_average(middle_salary)

def main():
    