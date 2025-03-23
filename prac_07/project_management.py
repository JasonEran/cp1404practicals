"""
Project Management
Estimate: 60 minutes
Actual:   110 minutes
"""
import datetime
from prac_07.project import Project

WELCOME_MESSAGE = "Welcome to Pythonic Project Management"
FILENAME = "projects.txt"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

def main():
    """Run the project management program."""
    print(WELCOME_MESSAGE)
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    choice = get_user_choice()
    while choice != "q":
        if choice == 'l':
            projects = load_from_user_file()
        elif choice == 's':
            save_to_user_file(projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_by_date(projects)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid choice")
        choice = get_user_choice()
    exit_with_save_option(projects, FILENAME)
