import random
patient_name = input("Mời nhập tên bệnh nhân")
gender = input("Mời nhập giới tính")
birth_year = input("Mời nhập năm sinh")
phone_number = input("Mời nhập sdt")
email = input("Mời nhập email")
symptom = input("Mời nhập triệu chứng")
cost = float(input("Mời nhập chi phí khám"))

random_num = random.randint(100,999)
id = f"BN{birth_year}{random.randint(random_num)}"

print(f"Mã bệnh nhân:{id} ({type(id).__name__})")
print(f"giới tính:{gender}({type(gender).__name__})")
print(f"năm sinh:{birth_year}({type(birth_year).__name__})")
print(f"sdt:{phone_number}({type(phone_number).__name__})")
print(f"email:{email}({type(email).__name__})")
print(f"triệu chứng:{symptom}({type(symptom).__name__})")
print(f"Chi phí:{cost}({type(cost).__name__})")