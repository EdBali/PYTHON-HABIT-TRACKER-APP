# Habits Tracker
I built the backend of a habit tracking app that is designed to help users keep track of their daily, weekly, and monthly habits. I built it using Python and it has six main components: Habit, Streak, HabitStore, HabitApplication,FileHandler and Analysis module. I created Each component in a separate python file. The app is designed to be a simple and flexible tool that is easy for you to use. It can also be easily extended to include additional features customized to suit individual needs.

## Installation
* Download the app’s repository
* Open your command prompt.
* Navigate to the app's directory using the 'cd' command. The app directory name is
“habit_app”
* Run the command, ``` "pip install -r requirements.txt” ``` to install the required packages.
* Run the following command to start the app:
```python main.py ``` .
This will launch the user interface of the app.

## How the app works(from a user's perspective)
When you add a habit. You will be asked to provide a habit name and the periodicity of the habit i.e. is it a daily or weekly habit. Make sure to complete the new habit before you save it or decide to quit out of the application. All the data you provide is automatically saved when you quit out of the application. If you want to do some analytics after registering new info, make sure to first save the new info you have just registered.

When you ‘complete’ a habit, the date on which you’ve completed the habit is registered. If it is a daily habit, the app will only allow you to complete the habit once a day, and if it is a weekly habit, then you can only complete it once a week.

A weekly streak is established when you complete a daily habit for seven consecutive days. A monthly streak is established when you complete a weekly habit for four consecutive weeks. If a day ends without you completing a habit, the habit is considered broken and the count for that habit is set to zero, hence failure to establish a weekly streak. You will have to be consistent for another seven days to establish the next streak. The number of times you break a habit run is also recorded.

The app gives analysis made on a selected habit. You can also get a summary analyis of all habits registered in the app.

## APP components

### Habit Class
The Habit class represents an individual habit, which is defined by a name and a period (daily, weekly). Each habit also has a counter that tracks the number of times the habit has been completed and a dictionary that stores the dates of completed habits. The class includes a made_streak method that checks if the habit has been completed enough times to qualify as a streak. The class also consists of a mechanism that prevents a daily streak from being completed twice a day(and twice a week for a weekly habit). It also keeps track of how many times a habit run is broken. This mechanism is made possible by the can_complete() and check_for_reset() methods

### Streak Class
The Streak class represents a streak of completed habits for a given habit and period. It is defined by a habit and a period (daily, weekly, or monthly), and it includes a count and a dictionary that stores the dates of completed habits. The class includes an increase_count method that increments the count of streaks established by the habit.

### HabitStore Class
The HabitStore class serves as a store for all the habits and streaks. It includes methods for adding and deleting habits, completing habits, and adding streaks. The store also maintains a dictionary of all the streaks, keyed by the habit that the streak is associated with.

### FileHandler Class
The FileHandler class handles reading and writing data to files in JSON format. This class is used to save the state of the HabitStore between sessions.

### Analyse.py
The analyse.py handles the analysis of the habits using functional programming paradigm. It provides; list of daily habits, list of weekly habits, shows currently active habits, daily Habit with highest number of streaks, weekly Habit with highest number of streaks, daily Habit with lowest number of streaks, weekly Habit with lowest number of streaks, habits with zero streaks.

### HabitApp Class
This class handles user input and data storage. This is where all the magic happens. It is the class that is used to execute the habit tracker application.


## Conclusion
In terms of interactions between the classes, the HabitApplication class interacts with the HabitStore class and the FileHandler class to manage the habits and their streaks, as well as loading and saving the habit and streak data. The HabitStore class interacts with the Habit and Streak classes to create and manage habits and their streaks. The Habit class interacts with the Streak class to create and manage streaks for a habit. Finally, the FileHandler class interacts with the HabitStore class to load and save habit and streak data to files

## Contributing
Contributions to the Habit Tracker are welcome! If you find a bug or have an idea for a new feature, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and submit a pull request with your changes.




