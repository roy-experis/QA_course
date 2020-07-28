# class parking:
    # def __init__(self,parking_id,adress,adress_number,date_avileble,start_time_avileble,end_time_avileble,price_per_hour,parking_owner):
    #     self.parking_id=parking_id
    #     self.adress=adress
    #     self.adress_number=adress_number
    #     self.date_avileble=date_avileble
    #     self.start_time_avileble=start_time_avileble
    #     self.end_time_avileble=end_time_avileble
    #     self.price_per_hour=price_per_hour
    #     self.parking_owner=parking_owner
    #
    # def set_adress(self,new_adress,new_adress_number):
    #     self.adress=new_adress
    #     self.adress_number=new_adress_number
    #
counter=0
counter=counter+1
class parking_lot:
    def __init__(self,adress,adress_number,date_avileble,start_time_avileble,end_time_avileble,num_of_places,places_avileble,price_per_hour,parking_owner):
        self.parking_id= counter
        self.adress = adress
        self.adress_number=adress_number
        self.date_avileble = date_avileble
        self.start_time_avileble = start_time_avileble
        self.end_time_avileble = end_time_avileble
        self.num_of_places=num_of_places
        self.places_avileble=places_avileble
        self.price_per_hour=price_per_hour
        self.parking_owner=parking_owner

    # def set_adress(self,new_adress,new_adress_number):
    #     self.adress=new_adress
    #     self.adress_number=new_adress_number

class park_klayent:
    def __init__(self,id,passworld,bank_acount,viecle_number):
        self.id=id
        self.passworld=passworld
        self.bank_acount=bank_acount
        self.viecle_number=viecle_number

class parking_owner:
    def __init__(self,id,passworld,bank_acount):
        self.id=id
        self.passworld=passworld
        self.bank_acount=bank_acount