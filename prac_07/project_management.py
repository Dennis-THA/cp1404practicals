import datetime
from prac_07.project import Project

MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n"

=======

=======
FILENAME = "projects.txt"


projects = []


def main():
    print(MENU)
    choice = input(">>>: ").upper()
    while choice != "Q":
        if choice == "L":

=======


            filename = get_valid_name()
            load_projects(filename)
        elif choice == "S":
            filename = get_valid_name()
            save_projects(filename)

=======
=======
            load_projects(FILENAME)
        elif choice == "S":
            save_projects(FILENAME)

        elif choice == "D":
            display_projects()
        elif choice == "F":
            filter_projects()
        elif choice == "A":
            add_projects()
        elif choice == "U":
            update_project()
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>>: ").upper()
    print("Thank you for using custom-built project management software.")


def get_valid_name():
    name = input("Name: ")
    while name == "":
        print("Name must not be empty!")
        name = input("Name: ")
    return name


def add_projects():
    """Add new projects"""
    print(f"Let's add a new project")
    name = get_valid_name()
    start_date = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    project_to_add = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project_to_add)


def filter_projects():
    """Filter and display projects that start after the input date."""
    filtered_date = input("Show projects that start after date (dd/mm/yy): ")
    filtered_date = datetime.datetime.strptime(filtered_date, "%d/%m/%Y").date()
    filtered_projects = []
    for project in projects:
        if project.start_date >= filtered_date:
            filtered_projects.append(project)
    filtered_projects.sort()
    for filtered_project in filtered_projects:
        print(filtered_project)


def display_projects():
    """Display sorted incompleted projects and completed projects nicely"""
    incompleted_projects = [project for project in projects if int(project.completion_percentage) < 100]
    incompleted_projects.sort()
    print("Incomplete projects: ")
    for incompleted_project in incompleted_projects:
        print(f"  {incompleted_project}")
    completed_projects = [project for project in projects if int(project.completion_percentage) == 100]
    completed_projects.sort()
    print("Complete projects: ")
    for completed_project in completed_projects:
        print(f"  {completed_project}")


def save_projects(filename):
    """Save update projects into projects.txt"""
    with open(filename, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}"
                           f"\t{project.cost_estimate:.2f}\t{project.completion_percentage}\n")


def load_projects(filename):
    """Read the file, load projects data, and store as a list."""
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            name, start_date, priority, cost_estimate, completion = line.strip().split("\t")
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion)))


def update_project():
    """Choose a project and update completion percentage and/or priority."""
    for number, project in enumerate(projects):
        print(f"{number} {project}")

    project_choice = input("Project choice: ")
    if project_choice.isdigit():
        project_choice = int(project_choice)
        if 0 <= project_choice < len(projects):
            selected_project = projects[project_choice]
            print(selected_project)

            new_percentage = input("New Percentage: ")
            if new_percentage.isdigit():
                selected_project.completion_percentage = int(new_percentage)

            new_priority = input("New Priority: ")
            if new_priority.isdigit():
                selected_project.priority = int(new_priority)


main()
