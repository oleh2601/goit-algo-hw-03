from random import randint


def get_numbers_ticket(min, max, quantity):
    
    #validating data as per requirements
    if (min < 1) or (min > 999) or (max < 2) or (max > 1000) or (min > max) or ((max-min+1) < quantity):
        return [] # Returning an empty list if the parameters are invalid as per task
    else:

        #Initializing the set to make sure the numbers are unique
        set_of_random_numbers = set()

        #running the loop until the set is fully filled
        while len(set_of_random_numbers) < quantity:
            set_of_random_numbers.add(randint(min, max))

        #converting the set to a list and sorting the new list as per task 
        return sorted(list(set_of_random_numbers))
    




#data entry, example from the task

min = 10  #possible range 1 - 999
max = 14  #possible range 2 - 1000
quantity = 5 #no range 

#getting the results using our function

results = get_numbers_ticket(min, max, quantity)

#output test
# print(results)