def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''

    global cur_hedons
    global cur_health
    global tiredness
    global star_running
    global star_textbooks
    cur_hedons = 0
    cur_health = 0
    tiredness = False
    star_running = False
    star_textbooks = False
    global star_count
    global star_time1
    global star_time2
    global star_time3
    global cur_time
    global running_clock
    star_count = 0
    star_time1 = 0
    star_time2 = 0
    star_time3 = 0
    cur_time = 0
    running_clock = 0
    global prev_running_time
    prev_running_time = 0

def star_can_be_taken(activity):
    pass


def perform_activity(activity, duration):
    global cur_hedons
    global cur_health
    global tiredness
    global star_running
    global star_textbooks
    global running_clock
    global cur_time
    global prev_running_time
    if activity == "running":
        running_clock = running_clock + duration
        if star_running:#if a star is given to running
            if tiredness:#user tired
                #the health algoritm:
                if running_clock <= 180:
                    cur_health = cur_health + 3 * duration
                else:
                    cur_health = cur_health + (180 - prev_running_time) * 3 + (running_clock - 180) * 1
                #the hedon algorithm:
                if duration <= 10:
                    cur_hedons= cur_hedons + duration
                else:
                    cur_hedons = cur_hedons + 10 - 2 * (duration - 10)
                #the mandatory:
                tiredness = True
                cur_time = cur_time + duration
            else:#if the user is not tired
                #the health algoritm:
                if running_clock <= 180:
                    cur_health = cur_health + 3 * duration
                else:
                    cur_health = cur_health + (180 - prev_running_time) * 3 + (running_clock - 180) * 1
                #the hedon algorithm:
                if duration <= 10:
                    cur_hedons = cur_hedons + 5 * duration
                if duration > 10:
                    cur_hedons = cur_hedons + 50 - 2 * (duration)
                #the mandatory
                tiredness = True
                cur_time = cur_time + duration
            star_running = False
        else:#no star
            if tiredness:#user tired
                #the health algoritm:
                if running_clock <= 180:
                    cur_health = cur_health + 3 * duration
                else:
                    cur_health = cur_health + (180 - prev_running_time) * 3 + (running_clock - 180) * 1
                #the hedon algorithm:
                cur_hedons = cur_hedons - duration * 2
                #the mandatory
                tiredness = True
                cur_time = cur_time + duration
            else:#if the user is not tired
                #the health algoritm:
                if running_clock <= 180:
                    cur_health = cur_health + duration * 3
                else:
                    cur_health = cur_health + (180 - prev_running_time) * 3 + (running_clock - 180) * 1
                #the hedon algorithm:
                if duration <= 10:
                    cur_hedons = cur_hedons + duration * 2
                else:
                    cur_hedons = cur_hedons + 20 - (duration - 10) * 2
                #the mandatory
                tiredness = True
                cur_time = cur_time + duration
        prev_running_time = duration

    elif activity == "textbooks":
        if star_textbooks:#if star is given to textbooks
            if tiredness:#user tired
                #the health algoritm:
                cur_health = cur_health + duration * 2
                #the hedon algorithm:
                if duration <= 10:
                    cur_hedons= cur_hedons + duration
                else:
                    cur_hedons = cur_hedons + 10 - 2 * (duration - 10)
                #the mandatory
                tiredness = True
                cur_time = cur_time + duration
            else:#if the user is not tired
                #the health algoritm:
                cur_health = cur_health + duration * 2
                #the hedon algorithm:
                if duration <= 10:
                    cur_hedons = cur_hedons + 4 * duration
                elif 10 < duration <= 20:
                    cur_hedons = cur_hedons + 40 + 1 * (duration - 10)
                elif duration < 20:
                    cur_hedons = cur_hedons + 50 - (duration - 20)
                #the mandatory
                tiredness = True
                cur_time = cur_time + duration
            star_textbooks = False

        else:#if a star is not given to textbook
            if tiredness:#user tired
                #the health algoritm:
                cur_health = cur_health + duration * 2
                #the hedon algorithm:
                cur_hedons = cur_hedons - duration * 2#should run this one
                #the mandatory
                tiredness = True
                cur_time = cur_time + duration
            else:#if the user is not tired
                #the health algoritm:
                cur_health = cur_health + duration * 2
                #the hedon algorithm:
                if duration <= 20:
                    cur_hedons = cur_hedons + duration
                else:
                    cur_hedons = cur_hedons + 20 - (duration - 20)#why run this one??

                #the mandatory
                tiredness = True
                cur_time = cur_time + duration


    elif activity == "resting":
        if duration <= 120:
            tiredness = True
        else:
            tiredness = False
        running_clock = 0




def get_cur_hedons():
    global cur_hedons
    return cur_hedons

def get_cur_health():
    global cur_health
    return cur_health

def offer_star(activity):
    global tiredness
    global star_running
    global star_textbooks
    global star_count
    global star_time1
    global star_time2
    global star_time3
    global cur_time

    if activity == "running":
        star_running = True
    elif activity == "textbooks":
        star_textbooks = True
    elif activity == "resting":
        pass
    star_count = star_count + 1
    if star_count == 1:
        star_time1 = cur_time
    if star_count == 2:
        star_time2 = cur_time
    if star_count == 3:
        star_time3 = cur_time
        if star_time3 - star_time1 <= 120:
            star_running = False
            star_textbooks = False
        else:
            star_count = 1
            star_time2 = 0
            star_time3 = 0
            star_time1 = cur_time




def most_fun_activity_minute():
    global tiredness
    global star_textbooks
    global star_resting
    global star_running

    if star_textbooks:
        return "textbooks"
    elif star_running:
        return "running"
    elif tiredness:
        return "resting"


################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    pass

def get_effective_minutes_left_health(activity):
    pass

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    pass


def estimate_health_delta(activity, duration):
    pass

################################################################################

if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10////
