def drink_coffee():
    global drink_c
    drink_c = True

def study(minutes):
    global current_time
    global knols
    global too_much_coffee
    global coffee_count
    global cofftime1
    global cofftime2
    global cofftime3
    if drink_c:
        coffee_count = coffee_count + 1
        if coffee_count == 1:
            knols = knols + minutes * 10
            cofftime1 = current_time
        if coffee_count == 2:
            knols = knols + minutes * 10
            cofftime2 = current_time
        if coffee_count == 3:
            cofftime3 = current_time
        print(knols)
    else:
        if too_much_coffee:
            knols = knols
            print(knols)
        else:
            knols = knols + minutes * 5
            print(knols)
    current_time = current_time + minutes

def initialize():
    global drink_c
    global too_much_coffee
    global current_time
    global knols
    global coffee_count
    global cofftime1
    global cofftime2
    global cofftime3
    drink_c = False
    too_much_coffee = False
    current_time = 0
    knols = 0
    coffee_count = 0
    cofftime1 = 0
    cofftime2 = 0
    cofftime3 = 0

if __name__ == '__main__':
    initialize() # start the simulation
    study(60) # knols = 300
    study(20) # knols = 400
    drink_coffee() # knols = 400
    study(10) # knols = 500
    drink_coffee() # knols = 500
    study(10) # knols = 600
    drink_coffee() # knols = 600, 3rd coffee in 20 minutes
    study(10) # knols = 600




