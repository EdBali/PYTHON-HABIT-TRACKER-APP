import pytest
# from pytest import capsys
from datetime import datetime, timedelta
from habit import Habit
from streak import Streak
from habit_store import HabitStore


@pytest.fixture
def habit():
    return Habit("Workout")

def test_init(habit):
    'This test checks that the Habit instance is initialized with the correct attributes and values. '
    assert habit.name() == "Workout"
    assert habit.period() == ""
    assert habit.counter() == 0
    assert habit.dates == {}
    assert habit.last_completed == None
    assert habit.habit_break_count == 0

def test_can_complete_daily(habit):
    habit._period = "daily"
    habit.last_completed = datetime.today().strftime('%Y-%m-%d')
    assert habit.can_complete() == False
    habit.last_completed = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    assert habit.can_complete() == True

def test_can_complete_weekly(habit):
    habit._period = "weekly"
    habit.last_completed = datetime.today().strftime('%Y-%m-%d')
    assert habit.can_complete() == False
    habit.last_completed = (datetime.today() - timedelta(days=8)).strftime('%Y-%m-%d')
    assert habit.can_complete() == True

def test_check_for_reset_daily(habit):
    habit._period = "daily"
    habit.last_completed = (datetime.today() - timedelta(days=2)).strftime('%Y-%m-%d')
    habit._counter = 2
    assert habit.check_for_reset() == True
    assert habit.counter() == 0

def test_check_for_reset_weekly(habit):
    habit._period = "weekly"
    habit.last_completed = (datetime.today() - timedelta(days=9)).strftime('%Y-%m-%d')
    habit._counter = 2
    assert habit.check_for_reset() == True
    assert habit.counter() == 0

def test_made_streak_daily(habit):
    habit._period = "daily"
    habit._counter = 6
    assert habit.made_streak() == False
    habit._counter = 7
    assert habit.made_streak() == True

def test_made_streak_weekly(habit):
    habit._period = "weekly"
    habit._counter = 3
    assert habit.made_streak() == False
    habit._counter = 4
    assert habit.made_streak() == True

def test_increase_count(habit):
    habit.increase_count()
    assert habit.counter() == 1

def test_reset_counter(habit):
    habit.reset_counter()
    assert habit.counter() == 0

@pytest.fixture
def streak():
    return Streak("workout")

def test_init(streak):
    'This test checks that the Streak instance is initialized with the correct attributes and values. '
    assert isinstance(streak.habit(),Habit)
    assert streak.habit().name() =="workout"
    assert streak.period() == None
    assert streak.count() == 0
    assert streak.dates == {}

def test_count_increase(streak):
    streak.increase_count()
    assert streak.count() == 1

def test_assign_period_weekly_to_daily_ahbit(streak):
    streak.habit()._period = "daily"
    streak.assign_period()
    assert streak.period() == "weekly"

@pytest.fixture
def habit_store():
    return HabitStore()

def test_init(habit_store):
    assert habit_store.habits == {}
    assert habit_store.streaks == {}

def test_add_habit(habit_store,capsys):
    

    habit_store.add_habit("Drink water", "daily")
    assert "Drink water" in habit_store.habits
    assert habit_store.habits["Drink water"]._period == "daily"
    
    # Test adding a new weekly habit
    habit_store.add_habit("Go for a run", "weekly")
    assert "Go for a run" in habit_store.habits
    assert habit_store.habits["Go for a run"]._period == "weekly"
    
    # Test adding an existing habit
    habit_store.add_habit("Drink water", "daily")
    assert "Drink water" in habit_store.habits
    assert habit_store.habits["Drink water"]._period == "daily"
    captured = capsys.readouterr()
    assert "A habit with name 'Drink water' already exists" in captured.out
    
    # # Test adding a habit with an invalid period
    habit_store.add_habit("Read a book", "monthly")
    assert "Read a book" not in habit_store.habits
    captured = capsys.readouterr()
    assert "The period should be 'daily' or 'weekly'" in captured.out


def test_get_habit(habit_store):
    habit_store.add_habit("Jump rope","weekly")

    result = habit_store.get_habit("Jump rope")
    assert isinstance(result,Habit)
    

    # Test getting a habit that does not exist in the habits dictionary
    false_result = habit_store.get_habit("Smash")
    assert false_result == None

def test_delete_habit(habit_store,capsys):
    habit_store.add_habit("Eat fene","weekly")
    assert "Eat fene" in habit_store.habits
    habit_store.delete_habit("Eat fene")
    assert "Eat fene" not in habit_store.habits

    # Test deleting a habit that doesnt exist in the dictionary
    habit_store.delete_habit("Eat apple")
    captured = capsys.readouterr()
    assert "This habit is not in the database" in captured.out


def test_complete_habit(habit_store):
    habit_store.add_habit("Exercise", "daily")
    habit_store.complete_habit("Exercise")
    assert habit_store.habits["Exercise"].counter() == 1
    assert habit_store.habits["Exercise"].last_completed == datetime.today().strftime('%Y-%m-%d')

def test_complete_habit_with_invalid_name(habit_store):
    habit_store.add_habit("Wash dog", "daily")
    habit_store.complete_habit("Study")
    assert habit_store.habits["Wash dog"].counter() == 0

def test_complete_habit_twice_in_same_day(habit_store):
    habit_store.add_habit("Wash car", "weekly")
    habit_store.complete_habit("Wash car")
    habit_store.complete_habit("Wash car")
    assert habit_store.habits["Wash car"].counter() == 1

def test_complete_habit_reset_streak():
    hs = HabitStore()
    hs.add_habit("Exercise", "daily")
    hs.habits["Exercise"]._counter = 4
    hs.habits["Exercise"].last_completed = "2023-04-11"
    assert hs.habits["Exercise"].counter() == 4
    hs.complete_habit("Exercise")
    assert hs.habits["Exercise"].counter() == 1


    
