file_content = """Adams, I, 12
Johnson, I, 10
Smith, O, 12
Lee, O, 16
"""
with open("student_credits.txt", "w") as file:
    file.write(file_content)

total_tuition = 0
student_count = 0
with open("student_credits.txt", "r") as file:
    print(f"{'last_name':<15} {'student_type':<15} {'credits':<10} {'tuition':<10}")
   
    for line in file:
        last_name, student_type, credits_str = line.split(",")
        credits = int(credits_str)
        if student_type.strip() == "I":
            tuition = credits * 250
        else:
            tuition = credits * 500
        total_tuition += tuition
        student_count += 1
        print(f"{last_name:<15} {student_type:<15} {credits:<10} {tuition:<10.2f}")
num_students = student_count
print(f"{'Total Students:':<15} {num_students:<15}")