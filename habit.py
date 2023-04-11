import inspect
from datetime import datetime, timedelta
def print_error(error):
    calling_frame = inspect.currentframe().f_back
    method_name = calling_frame.f_code.co_name
    instance_name = calling_frame.f_locals.get('self').__class__.__name__
    print(f"Something went wrong in the '{method_name}' method of {instance_name}:\n{error}")
    return

class Habit:
    """
    This class represents a single habit.

    Args:
        name (str): The name of the habit.
        

    Attributes:
        _name (str): The name of the habit
        _period (str): The periodicity of the habit("daily","weekly")
        _counter (int): Tracks the number of times the habit has been completed
        dates (dict): Stores the dates of completed habits;  ----Key = f"s{streak_count}{counter}"-------   -----Value = date-------
        last_completed (str): Stores the date on which the habit was last completed
        habit_break_count(int): Keeps track of how many times a habit run is broken.

    Methods:
        can_complete(): Checks whether a habit can be completed on specific date. This is to avoid instances where a habit is completed twice
        check_for_reset(): Checks whether a habit run has been broken and resets its counter value if  True.
        made_streak(): Checks if the habit has been completed enough times to qualify as a streak
        period(): Returns the value of the period attribute
        name(): Returns the value of the name attribute
        increase_count(): Increases counter by one when called
        reset_counter(): Resets value of counter when called
        
    Raises:
        .

    Examples:
        >>> h = Habit("Workout")
        >>> h.name()
        Workout
        
    """
    def __init__(self,name: str):
        try:
            self._name = name
            self._period = ""
            self._counter = 0
            self.dates = {}
            self.last_completed = None
            self.habit_break_count = 0
        except Exception as error:
            print_error(error)

    def can_complete(self):
        today = datetime.today()
        if self._period == "daily":
            if self.last_completed is None or datetime.strptime(self.last_completed, '%Y-%m-%d').date() < today.date():
                return True
            else:
                print("You already completed this task today.")
                return False
        elif self._period == "weekly":
            if self.last_completed is None or datetime.strptime(self.last_completed, '%Y-%m-%d') + timedelta(days=7) <= today:
                return True
            else:
                print("You already completed this task this week.")
                return False
        else:
            print("Periodicity is not set for the habit.")
            return False
        
    def check_for_reset(self):
        today = datetime.today()
        if self.last_completed is None:
            if self._counter != 0:
                self._counter = 0
        elif self._period == "daily":
            if (today - datetime.strptime(self.last_completed, '%Y-%m-%d')).days > 1:
                self._counter = 0
                return True
        elif self._period == "weekly":
            if (today - datetime.strptime(self.last_completed, '%Y-%m-%d')).days > 8:
                self._counter = 0
                return True
        else:
            print("Invalid periodicity specified")

    def made_streak(self):
        """
        Checks if the habit has been completed enough times to qualify as a streak.

        Args:
            None.

        Raises:
            None.

        Returns:
            bool: True if the habit qualifies as a streak, False otherwise.
        """
        try:
            if self._period == "daily" and self._counter == 7:
                return True
            elif self._period == "weekly" and self._counter == 4:
                return True
            elif self._period == "monthly" and self._counter == 4:
                return True
            else: 
                return False
        except Exception as error:
            print_error(error)

    def increase_count(self):
        """
        Increases the counter attribute by one.

        Args:
            None.

        Raises:
            None.

        Returns:
            None.
        """
        try:
            self._counter += 1
        except Exception as error:
            print_error(error)

    def reset_counter(self):
        """
        Resets the counter attribute to zero.

        Args:
            None.

        Raises:
            None.

        Returns:
            None.
        """
        try:
            self._counter = 0
        except Exception as error:
            print_error(error)

    def period(self):
        """
        Returns the value of the period attribute.

        Args:
            None.

        Raises:
            None.

        Returns:
            str: The value of the period attribute.
        """
        return self._period
    
    def name(self):
        """
        Returns the value of the name attribute.

        Args:
            None.

        Raises:
            None.

        Returns:
            str: The value of the name attribute.
        """
        return self._name
    
    def counter(self):
        """
        Returns the value of the counter attribute.

        Args:
            None.

        Raises:
            None.

        Returns:
            int: The value of the counter attribute.
        """
        return self._counter
        
     