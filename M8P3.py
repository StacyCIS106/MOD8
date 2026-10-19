file_content = """Adms, 50000
Baker, 75000
Smith, 450000
Johnson, 60000
Lee, 30000
"""
with open("employee_salaries.txt", "w") as file:
    file.write(file_content)

def get_bonus_rate(salary):
    if salary >= 100000:
        return 0.20
    elif salary >= 50000:
        return 0.15
    else:
        return 0.10
total_bonus = 0
with open("employee_salaries.txt", "r") as file:
    lines = file.readlines()
    print(f"{"last_name":<15} {"salary":<10} {"bonus_rate":<12}")
    print("-" * 40)
    for line in lines:
        last_name, salary_str = line.split(",")
        salary = float(salary_str)
        bonus_rate = get_bonus_rate(salary)
        bonus_amount = salary * bonus_rate
        total_bonus += bonus_amount
        print(f"{last_name:<15} {salary:<10.2f} {bonus_rate:<12.2%}")
print(f"Total bonus for all employees: ${total_bonus:.2f}")