DESK_CAPACITY = 5

students_in_classes = [20, 21, 22]

def calc_necessary_desk_amount(students_in_class):
    return students_in_class // DESK_CAPACITY + int(students_in_class % DESK_CAPACITY != 0)

for cl, students in enumerate(students_in_classes):
    print(f"Class {cl}, students: {students}, desks needed: {calc_necessary_desk_amount(students)}")