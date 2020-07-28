import datetime
class men:

    def __init__(self,id, f_name, l_name, byear, bmonth, bday, eye_color, hair_color, num_of_kids):
        self.id=id
        self.first_name = f_name
        self.last_name = l_name
        self.birth_year = byear
        self.birth_month = bmonth
        self.birth_day = bday
        self.eye_color = eye_color
        self.hair_color= hair_color
        self.num_of_kids= num_of_kids

    def return_b_day(self):
        return self.birth_day,self.birth_month,self.birth_year

    def return_age(self):
        return (int (datetime.date.year)- int (self.birth_year)),"years old"

    def all_info(self):
        return self.id,self.first_name,self.last_name,self.birth_day,self.birth_month,self.birth_year,self.eye_color,self.hair_color