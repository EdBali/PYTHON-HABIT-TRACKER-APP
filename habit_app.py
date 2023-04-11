import inspect
import json
from habit_store import HabitStore
from filehandler import FileHandler
from analyse import get_all_habits, get_habit_info, get_daily_habits, get_weekly_habits, get_highest_monthly_streak_count,get_highest_weekly_streak_count,get_lowest_monthly_streak_count,get_lowest_weekly_streak_count
def print_error(error):
    calling_frame = inspect.currentframe().f_back
    method_name = calling_frame.f_code.co_name
    instance_name = calling_frame.f_locals.get('self').__class__.__name__
    print(f"Something went wrong in the '{method_name}' method of {instance_name}:\n{error}")
    return

class HabitApplication:
    """
    This class manages the user interface of the habit tracking application.

    Args:
        -
        

    Attributes:
        habit_store (HabitStore)
        file_handler (FileHandler)
        

    Methods:
        help(): Prints instrctions of what commands the user can execute
        exit(): Saves data to the respective json files
        add_habit(): Calls the add_habit() method of HabitStore
        delete_habit(): Calls the delete_habit() method of HabitStore
        complete_habit(): Calls the complete_habit() method of HabitStore
        analyze_habit(): Gives all info about a habit
        full_analysis(): Gives important habit statistics
        execute():This executes the application.

        
    Raises:
        .

    Examples:
        
        
    """

    def __init__(self):
        self.habit_store = HabitStore()
        self.file_handler = FileHandler("habits.json","streaks.json")

        try:
            for habit_name, habit in self.file_handler.load_habit_file().items():
                self.habit_store.habits[habit_name] = habit
        except (FileNotFoundError, json.JSONDecodeError):
            self.habit_store.habits = {}

        try:
            for habit_name, streak  in self.file_handler.load_streak_file().items():
                self.habit_store.streaks[habit_name] = streak
        except (FileNotFoundError, json.JSONDecodeError):
            self.habit_store.streaks = {}
            

    def help(self):
        try:
            print("Instructions:")
            print("Press 0 to quit out of the application")
            print("Press 1 to add a habit")
            print("Press 2 to delete a habit")
            print("Press 3 to complete a habit")
            print("Press 4 to analyze a habit")
            print("Press 5 to get list of habits")
            print("Press 6 to get list of daily habits")
            print("Press 7 to get list of weekly habits")
            print("Press 8 for summary analysis of habits")
            print("Press 9 to save data")

        except Exception as error:
            print_error(error)


    def exit(self):
        # try:
            self.file_handler.save_files(self.habit_store.habits,self.habit_store.streaks)

            
        # except Exception as error:
        #     print_error(error)

    def add_habit(self):
        try:
            name = input("Habit name: ").lower()
            period = input("Periodicity(daily or weekly): ").lower()
            self.habit_store.add_habit(name,period)
        except Exception as error:
            print_error(error)
    
    def delete_habit(self):
        try:
            name = input("Habit name: ").lower()
            self.habit_store.delete_habit(name)
        except Exception as error:
            print_error(error)

    def complete_habit(self):
        # try:
            name = input("Habit name: ").lower()
            self.habit_store.complete_habit(name)
        # except Exception as error:
        #     print_error(error)

    def analyze_habit(self):
        # try:
            name = input("Habit name: ")
            get_habit_info(self.habit_store,name)
        # except Exception as error:
        #     print_error(error)

    def get_all_habits_app(self):
        try:
            get_all_habits(self.habit_store)
        except Exception as error:
            print_error(error)

    def get_daily_habits_app(self):
        try:
            get_daily_habits(self.habit_store)
        except Exception as error:
            print_error(error)

    def get_weekly_habits_app(self):
        try:
            get_weekly_habits(self.habit_store)
        except Exception as error:
            print_error(error)        
    
    def full_analysis(self):
        # try:
            get_highest_weekly_streak_count(self.habit_store)
            get_highest_monthly_streak_count(self.habit_store)
            get_lowest_weekly_streak_count(self.habit_store)
            get_lowest_monthly_streak_count(self.habit_store)
        # except Exception as error:
        #     print_error(error)

    def execute(self):
        self.help()
        while True:
            
            print("")
            command = input("Command: ")

            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_habit()
            elif command == "2":
                self.delete_habit()
            elif command == "3":
                self.complete_habit()
            elif command == "4":
                self.analyze_habit()
            elif command == "5":
                self.get_all_habits_app()
            elif command == "6":
                self.get_daily_habits_app()
            elif command == "7":
                self.get_weekly_habits_app()
            elif command == "8":
                self.full_analysis()
            elif command == "9":
                self.exit()