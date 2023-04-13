import inspect
from habit import Habit
from streak import Streak
from datetime import datetime
def print_error(error):
    calling_frame = inspect.currentframe().f_back
    method_name = calling_frame.f_code.co_name
    instance_name = calling_frame.f_locals.get('self').__class__.__name__
    print(f"Something went wrong in the '{method_name}' method of {instance_name}:\n{error}")
    return

class HabitStore:
    """
    This class serves as a store for all the habits and streaks

    Args:
        -
        

    Attributes:
        habits (dict): {Key = habit name,  Value = Habit instance}
        streaks (dict): {Key = habit instance,  Value = Streak instance}
        

    Methods:
        ==> add_habit(name,period): Creates a new habit object if it doesnt exist in the habits dictionary
        ==> deletehabit(name): Deletes the selected key value pair from the habits dictionary
        ==> complete_habit(name): Increments the counter of the selected Habit object,and adds the date of completion to the habit's Dates dictionary. Checks if a streak has been established. If a streak has been established, it creates a new Streak object or increments an existing one.
        ==> __add_streak(habit,period): Creates a new streak object if it doesnt exist in the dictionary, and assigns a period to the new streak. If it exists, it just calls the increase_count() method of the Streak class. Lastly, it adds the date on which this was done.
                                
    Raises:
        .

    Examples:
        >>> hs = HabitStore()
        >>> hs.add_habit()
        
        
    """

    def __init__(self):
        try:
            self.habits = {}
            self.streaks = {}
        except Exception as error:
            print_error(error)





    def add_habit(self,name,period):
        """
        Adds a new habit to the habits dictionary of the HabitStore object. 
        If the habit already exists, an error message will be printed and the habit will not be added.
        
        Args:
        - name (str): The name of the new habit.
        - period (str): The period of the habit. Can be "daily" or "weekly".
        
        Returns:
        - None.
        """
        try:
            periods = ["daily","weekly"]
            if name in self.habits:
                print(f"A habit with name '{name}' already exists in the HabitsTracker.")
                return
            if not period in periods:
                print("The period should be 'daily' or 'weekly'")
                return
            
            self.habits[name] = Habit(name)
            self.habits[name]._period = period
             
        except Exception as error:
            print_error(error)
    






    def get_habit(self,name):
        """
        Returns the Habit object with the given name. 
        If the habit does not exist in the HabitStore object, None will be returned.
        
        Args:
        - name (str): The name of the habit to retrieve.
        
        Returns:
        - Habit object with the given name or None if the habit is not found.
        """
        if not name in self.habits:
            return None 
        return self.habits[name]





    def delete_habit(self,name):
        """
        Deletes a habit from the habits dictionary of the HabitStore object. 
        If the habit does not exist in the HabitStore object, an error message will be printed and nothing will be deleted.
        If the habit has an associated streak, the streak will also be deleted from the streaks dictionary.
        
        Args:
        - name (str): The name of the habit to delete.
        
        Returns:
        - None.
        """
        try:
            if name in self.habits:
                self.habits.pop(name)
                if name in self.streaks:
                    self.streaks.pop(name)
            else:
               print("This habit is not in the database")
        except Exception as error:
            print_error(error)






    def complete_habit(self,name):
        """
        Increments the counter of a habit and adds the date of completion to the habit's dates dictionary.
        Checks if a streak has been established. If a streak has been established, 
        it creates a new Streak object or increments an existing one.
        
        Args:
        - name (str): The name of the habit to complete.
        
        Returns:
        - None.
        """
        # try:
        if name in self.habits:
                habit = self.habits[name]
                if habit.can_complete():
                    habit.check_for_reset()
                    if habit.check_for_reset():
                        habit.habit_break_count += 1
                    habit.increase_count()
                    habit.last_completed = datetime.today().strftime('%Y-%m-%d')
                    
                    today = datetime.today().strftime('%Y-%m-%d')
                    # first check if a streak for this habit has been established. If not the key in the dates dictionary is "s0-habit.counter"
                    if name in self.streaks:
                        streak_count = self.streaks[name].count()
                        habit.dates[f's{streak_count}-{habit.counter()}'] = today
                        
                    else:
                        
                        habit.dates[f's0-{habit.counter()}'] = today

                    if habit.made_streak():
                        habit.reset_counter()
                        self.__add_streak(name)
                else:
                    print(f"You already completed this {habit._period} task.")
        else:
                print("This habit is not in the database")
        # except Exception as error:
        #     print_error(error)






    def __add_streak(self,name):
        """
        Creates a new streak object if it does not exist in the streaks dictionary and assigns a period to the new streak. 
        If the streak object already exists in the streaks dictionary, it just calls the increase_count() method of the Streak class.
        Lastly, it adds the date on which this was done to the streak's dates dictionary.
        This method is only intended to be called from within the HabitStore class.
        
        Args:
        - name (str): The name of the habit to create or increment a streak for.
        
        Returns:
        - None.
        """
        try: 
            if name in self.streaks:
                streak = self.streaks[name]
            else:
                streak = Streak(name)
                self.streaks[name] = streak
                streak.assign_period()
            streak.increase_count()
            
            today = datetime.today().strftime('%Y-%m-%d')
            streak.dates[streak.count()] = today
        except Exception as error:
            print_error(error)





    def get_streak(self,name):
        """
        Returns the Streak object associated with the given habit name. 
        If no Streak object is associated with the habit name, None will be returned.
        
        Args:
        - name (str): The name of the habit to retrieve the Streak object for.
        
        Returns:
        - Streak object associated with the given habit name or None if no streak is found.
        """
        if not name in self.streaks:
            print("A streak has not been established for this habit.")
            return None
        return self.streaks[name]



    