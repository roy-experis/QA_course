from classes.bus import *
palces=int(input("whats the number of places on the bus?"))
line=int(input("whitch line is the bus?"))
bus1=bus(line,palces)
get=int(input("1 to had passenger, 2 to remove passenger,0 to stop"))
name=input("whats the name of the passenger?")
while(get!=0):
    if(get==1):
        bus1.get_on(name)
    else:
        bus1.get_off(name)
    get = int(input("1 to had passenger, 2 to remove passenger,0 to stop"))
    if(get!=0):
        name = input("whats the name of the passenger?")
print(bus1.list)

# bus1=bus(121,10)
# bus1.get_on('roy')
# print(bus1.l)
# print(bus1.get_off('ro'))
# print(bus1.l)
# print(bus1.__str__())