# phan tich loi
    # khi tach file ra se tai su dung duoc lai code
    # de bao tri va sua loi
    # de dang thu code hon
# sua loi

students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]

def validate_score(score_input):

    score_input = score_input.strip()
    
    if score_input == "":
        return False

    if score_input.count('.') == 1:
        parts = score_input.split('.')
        if not (parts[0].isdigit() and parts[1].isdigit()):
            return False

    elif not score_input.isdigit():
        return False

    score = float(score_input)
    if 0 <= score <= 10:
        return True
        
    return False

def find_student_by_id(student_list, student_id):
    for index in range(len(student_list)):
        if student_list[index]["student_id"] == student_id:
            return index
    return -1
def get_rank(average_score):

    if average_score >= 8.0:
        return "Gioi"
    elif average_score >= 6.5:
        return "Kha"
    elif average_score >= 5.0:
        return "Trung binh"
    else:
        return "Yeu"

def display_students(student_list):
    if len(student_list) == 0:
        print("Danh sach hoc vien hien dang trong.")
        return
        
    for index in range(len(student_list)):
        student = student_list[index]
        print(f"{index + 1}. Ma: {student['student_id']} | Ten: {student['name']} | Toan: {student['math_score']} | Anh: {student['english_score']}")

def add_student(student_list):
    student_id = input("Nhap ma hoc vien moi: ").upper().strip()
    if student_id == "":
        print("Loi: Ma hoc vien khong duoc de trong!")
        return

    for student in student_list:
        if student["student_id"] == student_id:
            print("Ma hoc vien da ton tai, vui long chon lai tinh nang de nhap ma khac!")
            return 

        name = input("Nhap ten hoc vien: ").title().strip()
        if name == "":
            print("Loi: Ten hoc vien khong duoc de trong!")
            return
        math_input = input("Nhap diem Toan: ")
        if validate_score(math_input):
            math_score = float(math_input)
        else:
            print("Diem khong hop le, phai la so tu 0 den 10")
            return

        eng_input = input("Nhap diem Anh: ")
        if validate_score(eng_input):
            english_score = float(eng_input)
        else:
            print("Diem khong hop le, phai la so tu 0 den 10")
            return
        new_student = {
        "student_id": student_id,
        "name": name,
        "math_score": math_score,
        "english_score": english_score
        }
        student_list.append(new_student)
        print("Them hoc vien thanh cong!")

def update_score(book):
    input_id = input("Nhap ma hoc vien can cap nhat: ").upper().strip()
    found=False
    for student in book:
        if student["id"] == input_id:
            found=True
            math_input = input("Nhap diem Toan moi: ")
            if validate_score(math_input):
                new_math = float(math_input)
            else:
                print("Diem khong hop le, phai la so tu 0 den 10")
                return

            eng_input = input("Nhap diem Anh moi: ")
            if validate_score(eng_input):
                new_eng = float(eng_input)
            else:
                print("Diem khong hop le, phai la so tu 0 den 10")
                return 

            student["math_score"]= new_math
            student["english_score"]= new_eng
            print("Cap nhat diem so thanh cong!")
            return 

    if not found:
        print(f"Khong tim thay hoc vien mang ma [{input_id}]!")

def evaluate_students(student_list):
    if len(student_list) == 0:
        print("Danh sach trong, khong the danh gia.")
        return

    for index in range(len(student_list)):
        student = student_list[index]
        average_score = (student["math_score"] + student["english_score"]) / 2
        rank = get_rank(average_score)
        print(f"Ma: {student['student_id']} | Ten: {student['name']} | DTB: {average_score} | Xep loai: {rank}")

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====")
    print("1. Hiển thị danh sách học viên")
    print("2. Thêm học viên mới")
    print("3. Cập nhật điểm thi theo mã học viên")
    print("4. Đánh giá học lực của toàn bộ học viên")
    print("5. Thoát chương trình")
    print("====================================================")
    choice = input("Chon chuc nang (1-5): ").strip()
    match choice:
            case '1':
                display_students(students)
            case '2':
                add_student(students)
            case '3':
                update_score(students)
            case '4':
                evaluate_students(students)
            case '5':
                print("Cam on ban da su dung he thong!")
                break
            case _:
                print("Lua chon khong hop le, vui long nhap lai!")