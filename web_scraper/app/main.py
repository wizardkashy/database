from export.build_tree import build_trees, export_trees
from scraper.scrape_courses import scrape_courses
from export.courses import export_courses
from export.ap_exams import export_ap_exam

root_sql = '../../data/postDeployment/'
root_json = '../../store/'

def menu():
    print("\n------------------Scraping---------------\n")      
    print("Courses: 1\n")
    print("Program urls: 2\n")
    print("Course urls: 3")
    print("\n------------------Export File------------\n")
    print("courses.sql: 4\n\n"
            + "courses_in_ge.sql: 5\n\n"
            + "programs.sql: 6")
    print("\n------------------Other------------------\n")
    print("Build Prerequisite/Corequisite Tree: 7\n")
    print("Export Prerequisite/Corequisite Tree: 8\n")
    print("Export AP exams: 9")
    print("\n-----------------------------------------\n")
    print("Exit: 0\n")      

def validate_option(option: str) -> bool:
    return option.isnumeric() and 0 <= int(option) < 10 

def execute_option(option: chr):
    if option == '1':
        scrape_courses()
    elif option == '2':
        print('Program\'urls: todo')
    elif option == '3':
        print('Course\'urls: todo')
    elif option == '4':
        export_courses(root_sql + 'courses.sql')
    elif option == '5':
        file_path = root_sql + 'courses_in_ge.sql'
        print('todo')
    elif option == '6':
        file_path = root_sql + 'programs.sql'
        print('todo')
    elif option == '7':       
        build_trees(root_json + 'courses.json')
    elif option == '8':       
        export_trees(root_json + 'trees.json')
    elif option == '9':       
        export_ap_exam(root_json + 'ap_exam.sql')
        
if __name__ == "__main__":
    menu()       
    option = input("Enter your option: ")
    while not validate_option(option) :
        option = input("Invalid option\n" + "Enter again: ")
    
    if option != '0':
        execute_option(option)

