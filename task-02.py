import random


def get_numbers_ticket(min, max, quantity):
    try:
        #validating data as per requirements
        if (min < 1) or (min > 999) or (max < 2) or (max > 1000)\
              or (quantity < min) or (quantity > max):
            return [] # Returning an empty list if the parameters are invalid as per task
        else:

            #Initializing the set to make sure the numbers are unique
            set_of_random_numbers = set()

            #running the loop until the set is fully filled
            while len(set_of_random_numbers) < quantity:
                set_of_random_numbers.add(random.randint(min, max))

            #converting the set to a list and sorting the new list as per task 
            return sorted(list(set_of_random_numbers))
        
    #handling all other exceptions just in case
    except Exception:
        return []



#data entry, example from the task

min = 1  #possible range 1 - 999
max = 1000  #possible range 2 - 1000
quantity = 10  #possible range min to nax 

#getting the results using our function

results = get_numbers_ticket(min, max, quantity)
