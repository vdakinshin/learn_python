user_info = {"first_name" : "Василий", "last_name" : "Акиньшин"}
new_first_name = str(input("Введите своё имя!"))
user_info["first_name"] = new_first_name
new_last_name = str(input("Введите свою фамилию!"))
user_info["last_name"] = new_last_name
print(user_info.get("first_name") +" "+ user_info.get("last_name"))

