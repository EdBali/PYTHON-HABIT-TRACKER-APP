import inspect
from habit import Habit
def print_error(error):
    calling_frame = inspect.currentframe().f_back
    method_name = calling_frame.f_code.co_name
    instance_name = calling_frame.f_locals.get('self').__class__.__name__
    print(f"Something went wrong in the '{method_name}' method of {instance_name}:\n{error}")
    return

class Streak:
    """
    This class represents a streak established for a given habit

    Args:
        habit (Habit): Habit instance for which a streak has been established
        

    Attributes:
        _habit (Habit): The name of the habit
        _period (str): The periodicity of the streak("week","month","year")
        _count (int): Tracks the number of times the streak is established for the habit attached to it.
        dates (dict): Stores the dates on which the streak was established;  ----Key = count"-------   -----Value = date-------

    Methods:
        habit(): Returns the Habit instance attached to the streak
        period(): Returns the value of the period attribute
        increase_count(): Increases count by one when called
        count(): Returns the value of the count attribute
        assign_period(): Assigns a periodicity to the period attribute basing on what the habit's periodicity is
        
    Raises:
        .

    Examples:
        >>> s = Streak("Workout")
        >>> print(s.habit())
        Habit("Workout")
        
    """

    def __init__(self,habit_name):
        try:
            self._habit = Habit(habit_name)
            self._period = None
            self._count = 0
            self.dates = {}
        except Exception as error:
            print_error(error)

    def increase_count(self):
        try:
            self._count += 1
        except Exception as error:
            print_error(error)

    def assign_period(self):
        try:
            habit = self._habit
            
            self._period = "weekly" if habit.period() == "daily" else "monthly" 
            
        except Exception as error:
            print_error(error)

    def period(self):
        return self._period
    
    def count(self):
        return self._count
    
    def habit(self):
        return self._habit