data = [
    {"roll":1 , "marks":100 , "attendance": 56},
    {"roll":2 , "marks":50 , "attendance": 36},
    {"roll":3 , "marks":70 , "attendance": 100}
]
#function to display only some details
def display(data):
    print(f"{'roll':<10}{'marks':<15}")
    print("-" * 35)
    for student in data:
        print(f"{student['roll']:<10}{student['marks']:<15}")
        
display(data)