def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''
    global cur_hedons, cur_health
    global cur_time
    global last_activity, last_activity_duration
    global last_finished
    global bored_with_stars
    cur_hedons = 0
    cur_health = 0
    cur_star = None
    cur_star_activity = None
    bored_with_stars = False
    last_activity = None
    last_activity_duration = 0
    cur_time = 0
    last_finished = -1000
    global tiredness
    tiredness = False
    global star_textbooks
    global star_resting
    global star_running
    global star_clock
    star_textbooks = False
    star_resting = False
    star_running = False
    star_clock = 0
    global running_rested
    global textbooks_rested
    running_rested = False
    textbooks_rested = False

def star_can_be_taken(activity):
    pass


def perform_activity(activity, duration):
    global cur_hedons
    global cur_health
    global tiredness
    global star_textbooks
    global star_resting
    global star_running
    global star_clock
    if activity == "running":
        if star_running:#if the user is given star for running
            if duration <= 180:
                cur_health = cur_health + duration * 3
                if tiredness:#if is tired
                    if duration <= 10:#if duration is less than 10
                        cur_hedons = cur_hedons + duration
                    else:
                        cur_hedons = cur_hedons + duration * 1
                else:
                    if duration <= 10:
                        cur_hedons = cur_hedons + duration * 5
                    if duration > 10:
                        cur_hedons = cur_hedons + 50 - (duration - 10) * 2
            if duration > 180:
                cur_health = cur_health + 180 * 3 + (duration - 180) * 1
                if tiredness:#if is tired
                    cur_hedons = cur_hedons + duration * 1
                else:
                    cur_hedons = cur_hedons + 50 - (duration - 10) * 2
            tiredness = True
            star_clock = star_clock + duration

        else:
            if duration <= 180:
                cur_health = cur_health + duration * 3
                if tiredness:#if is tired
                    cur_hedons = cur_hedons - duration * 2
                else:
                    if duration <= 10:
                        cur_hedons = cur_hedons + duration * 2
                    if duration > 10:
                        cur_hedons = cur_hedons + 20 - (duration - 10) * 2
            if duration > 180:
                cur_health = cur_health + 180 * 3 + (duration - 180) * 1
                if tiredness:#if is tired
                    cur_hedons = cur_hedons - duration * 2
                else:
                    cur_hedons = cur_hedons + 20 - (duration - 10) * 2
            tiredness = True


    elif activity == "textbooks":
        if star_textbooks:#if textbook is given stars
            cur_health = cur_health + duration * 2
            if tiredness:#if is tired
                cur_hedons = cur_hedons - duration * 2 + duration * 3
            else:
                if  duration <= 20:
                    cur_hedons = cur_hedons + duration * 1 + duration * 3 #given by the star
                if duration > 20:
                    cur_hedons = cur_hedons + 80 + (duration - 20) * 2
            tiredness = True
            star_clock = star_clock + duration
        else:
            cur_health = cur_health + duration * 2
            if tiredness:#if is tired
                cur_hedons = cur_hedons - duration * 2
            else:
                if  duration <= 20:
                    cur_hedons = cur_hedons + duration * 1
                if duration > 20:
                    cur_hedons = cur_hedons + 20 - (duration - 20)
            tiredness = True


    elif activity == "resting":
        if duration >= 120:
            tiredness = False
        else:
            tiredness = True

    else:
        pass


def get_cur_hedons():
    global cur_hedons
    return cur_hedons

def get_cur_health():
    global cur_health
    return cur_health

def offer_star(activity):
    global star_textbooks
    global star_resting
    global star_running
    global star_clock
    if star_clock <= 120:
        if activity == "running":
            star_running = True
        elif activity == "resting":
            star_resting = True
        elif activity == "textbooks":
            star_textbooks = True
        else:
            pass
    else:
        star_running = False
        star_resting = False
        star_textboos = False

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
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10