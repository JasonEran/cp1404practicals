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

def get_user_choice():
    """Display the menu and get the user's choice."""
    print(MENU)
    return input(">>> ").lower()

def load_projects(filename):
    """Load projects from a tab-delimited file."""
    projects = []
    with open(filename, 'r') as in_file:
        lines = in_file.readlines()
        for line in lines[1:]:  # Skip header
            projects.append(parse_project_line(line))
    return projects

def parse_project_line(line):
    """Parse a single line from the project file into a Project object."""
    parts = line.strip().split('\t')
    name = parts[0]
    start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
    priority = int(parts[2])
    cost_estimate = float(parts[3])
    completion_percentage = int(parts[4])
    return Project(name, start_date, priority, cost_estimate, completion_percentage)

def save_projects(filename, projects):
    """Save projects to a tab-delimited file."""
    with open(filename, 'w') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(format_project_for_file(project))

def format_project_for_file(project):
    """Format a Project object into a string for file writing."""
    start_date_str = project.start_date.strftime("%d/%m/%Y")
    return f"{project.name}\t{start_date_str}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n"

def load_from_user_file():
    """Load projects from a user-specified file."""
    filename = input("Enter filename to load from: ")
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects

def save_to_user_file(projects):
    """Save projects to a user-specified file."""
    filename = input("Enter filename to save to: ")
    save_projects(filename, projects)
    print(f"Saved {len(projects)} projects to {filename}")

def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete = get_incomplete_projects(projects)
    completed = get_completed_projects(projects)
    print("Incomplete projects: ")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects: ")
    for p in completed:
        print(f"  {p}")

def get_incomplete_projects(projects):
    """Return a list of incomplete projects, sorted by priority."""
    incomplete = [p for p in projects if not p.is_complete()]
    incomplete.sort()
    return incomplete

def get_completed_projects(projects):
    """Return a list of completed projects, sorted by priority."""
    completed = [p for p in projects if p.is_complete()]
    completed.sort()
    return completed

def filter_by_date(projects):
    """Filter and display projects starting after a user-specified date."""
    filter_date = get_filter_date()
    filtered = get_projects_after_date(projects, filter_date)
    for p in filtered:
        print(p)

def get_filter_date():
    """Get the filter date from the user."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    return datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

def get_projects_after_date(projects, filter_date):
    """Return projects starting after the given date, sorted by start date."""
    filtered = [p for p in projects if p.start_date > filter_date]
    filtered.sort(key=lambda p: p.start_date)
    return filtered

def add_project(projects):
    """Add a new project to the list based on user input."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = get_start_date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)

def get_start_date():
    """Get the start date from the user."""
    date_string = input("Start date (dd/mm/yy): ")
    return datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

def update_project(projects):
    """Update an existing project's completion percentage and/or priority."""
    display_project_list(projects)
    choice = int(input("Project choice: "))
    selected_project = projects[choice]
    print(selected_project)
    update_project_completion(selected_project)
    update_project_priority(selected_project)

def display_project_list(projects):
    """Display the list of projects with indices."""
    for i, p in enumerate(projects):
        print(f"{i} {p}")

def update_project_completion(project):
    """Update the project's completion percentage if a new value is provided."""
    new_percentage_str = input("New Percentage: ")
    if new_percentage_str:
        project.completion_percentage = int(new_percentage_str)

def update_project_priority(project):
    """Update the project's priority if a new value is provided."""
    new_priority_str = input("New Priority: ")
    if new_priority_str:
        project.priority = int(new_priority_str)

def exit_with_save_option(projects, filename):
    """Exit the program, optionally saving to the default file."""
    save_choice = input(f"Would you like to save to {filename}? ").lower()
    if save_choice.startswith('y'):
        save_projects(filename, projects)
        print(f"Saved {len(projects)} projects to {filename}")
    print("Thank you for using custom-built project management software.")

main()