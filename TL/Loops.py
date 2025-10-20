Cars = ["audi", "BMW","Fiat"]

for i,  car in enumerate(Cars):
    car = car.title()
    print(i, car,i)
        
          
    
number_list =[1,2,3,4,5,6,7,8,9]
Sum_of_list = 0
for num in number_list:
    Sum_of_list=Sum_of_list+num

print(Sum_of_list)


Cars_updated = [car + " BB" for car in Cars]
print(Cars_updated)