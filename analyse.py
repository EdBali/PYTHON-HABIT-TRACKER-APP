from habit_store import HabitStore

def get_all_habits(habit_store):
    """
    Return a list of all the habit names.
    """
    """
    Return a list of all the habit names.
    """
    # Get a list of all habit names and corresponding Habit objects
    habit_names = [(habit_name,habit) for habit_name, habit in habit_store.habits.items()]
    
    # Print a header for the list of habits
    print("")
    print("-----List of habits-------")
    print("")
    
    # Loop through each habit and print its name and periodicity
    for habit_name, habit in habit_names:
        print(f"Habit name: {habit_name.upper()}")
        print(f"Periodicity: {habit.period()}")
        print("")




def get_daily_habits(habit_store):
    """
    Return a list of all the daily habits names.
    """
    # Filter the habit store to get all habits with a period of "daily"
    daily_habits = filter(lambda habit: habit[1].period() == "daily", habit_store.habits.items())
    
    
    print("")
    print("-----List of daily habits-------")
    print("")
    for habit_name, habit in daily_habits:
        # Print the name of the daily habit and its periodicity
        print(f"Habit name: {habit_name.upper()}")
        print(f"Periodicity: {habit.period()}")
        print("")





def get_highest_weekly_streak_count(habit_store):
    """
    Returns the information about the habits that have established a weekly streak the highest number of times.
    """
    # Create a filtered list of streaks whose periodicity is "weekly"
    weekly_streaks = filter(lambda streak: streak[1].period() == "weekly", habit_store.streaks.items())

    # Create a sorted list of (habit_name, streak) pairs
    sorted_streaks = sorted(weekly_streaks,key=lambda streak: streak[1].count(), reverse= True )

    # Get the maximum number times a weekly streak was established
    
    if sorted_streaks:
        max_streak_count = sorted_streaks[0][1].count()
    else:
        max_streak_count = 0
    
    # Create a list of all habits that have the highest number of established streaks.
    habits = []
    for habit_name, streak in sorted_streaks:
        if streak.count() < max_streak_count:
            break
        habits.append(habit_name.upper())

    print("")
    print("-----List of daily habits that established maximum number of weekly streaks-------")
    print("")
    for habit_name in habits:
        print(f"-> {habit_name}")
    print("")







def get_highest_monthly_streak_count(habit_store):
    """
    Returns the information about the habits that have established a monthly streak the highest number of times.
    """
    # Create a filtered list of streaks whose periodicity is "weekly"
    monthly_streaks = filter(lambda streak: streak[1].period() == "monthly", habit_store.streaks.items())

    # Create a sorted list of (habit_name, streak) pairs
    sorted_streaks = sorted(monthly_streaks,key=lambda streak: streak[1].count(), reverse= True )

    # Get the maximum number times a weekly streak was established
    if sorted_streaks:
        max_streak_count = sorted_streaks[0][1].count()
    else:
        max_streak_count = 0

    
    # Create a list of all habits that have the highest number of established streaks.
    habits = []
    for habit_name, streak in sorted_streaks:
        if streak.count() < max_streak_count:
            break
        habits.append(habit_name)

    print("")
    print("-----List of weekly habits that established maximum number of monthly streaks-------")
    print("")
    for habit_name in habits:
        print(f"-> {habit_name.upper()}")
    print("")







def get_lowest_weekly_streak_count(habit_store):
    """
    Returns the information about the habits that have established a weekly streak the lowest number of times.
    """
    # Create a filtered list of streaks whose periodicity is "weekly"
    weekly_streaks = filter(lambda streak: streak[1].period() == "weekly", habit_store.streaks.items())

    # Create a sorted list of (habit_name, streak) pairs
    sorted_streaks = sorted(weekly_streaks,key= lambda streak: streak[1].count() )

    if sorted_streaks:
        min_streak_count = sorted_streaks[0][1].count()
    else:
        min_streak_count = 0

    
    # Create a list of all habits that have the lowest number of established streaks.
    habits = []
    for habit_name, streak in sorted_streaks:
        if streak.count() > min_streak_count:
            break
        habits.append(habit_name)

    print("")
    print("-----List of daily habits that established minimum number of weekly streaks-------")
    print("")
    for habit_name in habits:
        print(f"-> {habit_name.upper()}")
    print("")








def get_lowest_monthly_streak_count(habit_store):
    """
    Returns the information about the weekly habits that have established a monthly streak the lowest number of times.
    """
    # Create a filtered list of streaks whose periodicity is "monthly"
    weekly_streaks = filter(lambda streak: streak[1].period() == "monthly", habit_store.streaks.items())

    # Create a sorted list of (habit_name, streak) pairs
    sorted_streaks = sorted(weekly_streaks,key=lambda streak: streak[1].count() )

    # Get the minimum number of times a monthly streak was established
    if sorted_streaks:
        min_streak_count = sorted_streaks[0][1].count()
    else:
        min_streak_count = 0

    
    # Create a list of all habits that have the lowest number of established streaks.
    habits = []
    for habit_name, streak in sorted_streaks:
        if streak.count() > min_streak_count:
            break
        habits.append(habit_name)

    print("")
    print("-----List of weekly habits that established minimum number of monthly streaks-------")
    print("")
    for habit_name in habits:
        print(f"-> {habit_name.upper()}")
    print("")








def get_weekly_habits(habit_store):
    """
    Return a list of all the weekly habits names.
    """
    # Get a list of all weekly habits
    weekly_habits = filter(lambda habit: habit[1].period() == "weekly", habit_store.habits.items())
    print("")
    print("-----List of weekly habits-------")
    print("")
    for  habit_name,habit in weekly_habits:
        print(f"Habit name: {habit_name.upper()}")
        print(f"Periodicty: {habit.period()}")
        print("")







def get_habit_info(habit_store, name):
    """
    Print the statistics for the habit with the given name.

    Parameters:
    habit_store (HabitStore): The habit store to search for the habit.
    name (str): The name of the habit to get information about.

    Returns:
    None
    """
    # Get the habits dictionary from the habit store
    habits = habit_store.habits

    # Check if the given habit name exists in the habits dictionary
    if not name in habits:
        print("This habit does not exist in the database")
        return

    # Get the habit object corresponding to the given name
    habit = habits[name]

    # Get the current streak count for the habit
    if habit_store.get_streak(name) != None:
        streaks_count = habit_store.get_streak(name).count()
    else:
        streaks_count = "0"

    # Print the statistics for the habit
    print("")
    print(f"----Statistics for {name.upper()}----")
    print("")
    print(f"Habit name: {name.upper()}")
    print(f"Periodicity: {habit.period()}")
    print(f"Habit Count: {habit.counter()}")
    print(f"Streak Count: {streaks_count}")
    print(f"Number of times this habit has been broken: {habit.habit_break_count}")



