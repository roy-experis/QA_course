class bus:
    def __init__(self,line,num_of_seats,num_of_passengers=0):
        self.num_of_seats=num_of_seats
        self.line = line
        self.num_of_passengers=num_of_passengers
        self.list=['Free' for i in range(num_of_seats)]

    def get_on(self, name_of_passenger):
        i=0
        while(i<len(self.list)):
            if self.list[i]=='Free':
                self.list[i]=name_of_passenger
                self.num_of_passengers=self.num_of_passengers+1
                break
            i=i+1
        else:
            print("the passenger", name_of_passenger,"had no place on the bus")

    def get_off(self, name_of_passenger):
        i=0
        while(i<len(self.list)):
            if self.list[i]==name_of_passenger:
                self.list[i]="Free"
                self.num_of_passengers=self.num_of_passengers-1
                break
            i=i+1
            if (i == len(self.list)):
                return "the passenger", name_of_passenger, "is not on the bus on the bus"

    def __str__(self):
        return self.line, self.list, "num of seats is:",self.num_of_seats,"num of passengers is:",self.num_of_passengers



