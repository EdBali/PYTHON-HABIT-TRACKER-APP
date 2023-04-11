import inspect
import json
from datetime import datetime
from habit_store import HabitStore
from habit import Habit
from streak import Streak

def print_error(error):
    calling_frame = inspect.currentframe().f_back
    method_name = calling_frame.f_code.co_name
    instance_name = calling_frame.f_locals.get('self').__class__.__name__
    print(f"Something went wrong in the '{method_name}' method of {instance_name}:\n{error}")
    return

class FileHandler:
    """
    This class handles reading and writing data to files in JSON format.

    Args:
        habit_file_name (str): The name of the file storing the habit data.
        streak_file_name (str): The name of the file storing the streak data.

    Attributes:
        habit_file_name (str): The name of the file storing the habit data.
        streak_file_name (str): The name of the file storing the streak data.
        habit_store (HabitStore): An instance of the HabitStore class.

    Methods:
        load_habit_file(): Loads the habit data from the habit file and returns a dictionary containing Habit objects.
        load_streak_file(): Loads the streak data from the streak file and returns a dictionary containing Streak objects.
        save_files(habits, streaks): Saves the habit and streak data to their respective files.

    Raises:
        Any exception that occurs while reading from or writing to the file is raised.

    Examples:
        file_handler = FileHandler("habit_data.json", "streak_data.json")
        habits = file_handler.load_habit_file()
        streaks = file_handler.load_streak_file()
        file_handler.save_files(habits, streaks)
        
        
    """

    def __init__(self,habit_file_name,streak_file_name):
        self.habit_file_name = habit_file_name
        self.streak_file_name = streak_file_name
        self.habit_store = HabitStore()

    def load_habit_file(self):
            """
            Reads data from the habit file in JSON format and loads the habits data into a HabitStore object.
            The HabitStore object contains Habit objects for each habit in the habit file.


            Args:
                -

            Returns:
                habits (dict): A dictionary containing Habit objects, with the keys being the habit names.

            Raises:
                -

            Examples:
                -


            """
        # try:
            with open(self.habit_file_name, 'r') as habit_file:
                data = json.load(habit_file)
                habits = {}
                for habit_name, habit_data in data.items():
                    habit = Habit(habit_name)
                    habit._period = habit_data['_period']
                    habit._counter = habit_data['_counter']
                    dates = {}
                    for count_str, date_str in habit_data['dates'].items():
                        count = count_str
                        date = date_str
                        dates[count] = date
                    habit.dates = dates
                    habit.last_completed = habit_data['last_completed']
                    habit.habit_break_count = habit_data['habit_break_count']
                    habits[habit_name] = habit
                return habits
        # except Exception as error:
        #     print_error(error)

    def load_streak_file(self):
        
        # try:
            with open(self.streak_file_name, 'r') as streak_file:
                data = json.load(streak_file)
                streaks = {}
                for habit_name, streak_data in data.items():
                    streak = Streak(habit_name)
                    streak._period = streak_data['_period']
                    streak._count = streak_data['_count']
                    dates = {}
                    for count_str, date_str in streak_data['dates'].items():
                        count = count_str
                        date = date_str
                        dates[count] = date
                    streak.dates = dates
                    streaks[habit_name] = streak
                return streaks

        # except Exception as error:
        #     print_error(error)

    def save_files(self,habits,streaks):
        """
        Writes the data from the Habits dictionary and the streaks dictionary to the habit and streak files, respectively,
        in JSON format.

        markdown
        Copy code
            Args:
                habits (dict): A dictionary containing Habit objects, with the keys being the habit names.
                streaks (dict): A dictionary containing Streak objects, with the keys being the habit names.

            Returns:
                -

            Raises:
                -

            Examples:
                -

        """
        # try:
        habit_data = {}
        for habit_name, habit in habits.items():
                habit_data[habit_name] = {
                    '_period': habit._period,
                    '_counter': habit._counter,
                    'dates': {count: date for count, date in habit.dates.items()},
                    'last_completed': habit.last_completed,
                    'habit_break_count': habit.habit_break_count
                }

        streak_data = {}
        for habit_name, streak in streaks.items():
                count_dates = {}
                for count, date in streak.dates.items():
                    count_dates[count] = date
                streak_data[habit_name] = {
                    '_period': streak._period,
                    '_count': streak._count,
                    'dates': count_dates
                }

        with open(self.habit_file_name,"w") as habit_file:
                json.dump(habit_data,habit_file,indent=4)

        with open(self.streak_file_name,"w") as streak_file:
                json.dump(streak_data,streak_file,indent=4)
        # except Exception as error:
        #     print_error(error)