def trip_planner_welcome(name):
    print("Welcome to SuperNagivator tripplanner " + name)


def estimated_time_rounded(estimated_time):
    rounded_time = round(estimated_time)
    return rounded_time


trip_planner_welcome("Gul")

estimate = estimated_time_rounded(3.5)
print(estimate)


def destination_setup(origin, destination, estimated_time, stop_points, mode_of_transport="Car"):
    print("Your trip begins at: " + origin)
    print("And your destination is: " + destination)
    print("It will take approximately " + str(estimated_time) + " hours")
    print("You will be traveling by: " + mode_of_transport)
    print("The stops between your destination are: " + stop_points)


destination_setup("London ", "Rome ", estimate, "Paris", "Plane")
