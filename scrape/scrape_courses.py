from bs4 import BeautifulSoup
import requests
from major_requirements import request_websites, scrape_courses
from Course import Course
import json
import time

ALL_TERMS = {}

def get_courses_websites():
    """
    get_courses_websites scrapes all of the websites that can be redirected from the main UCI
    course website. 
    """

    all_websites = set()
    soup = request_websites("http://catalogue.uci.edu/allcourses/")
    for elem in soup.find_all('a'):
        get_href = elem.get('href')
        if '/allcourses' in str(get_href):
            all_websites.add('http://catalogue.uci.edu' + get_href)

    all_websites = [elem for elem in all_websites]
    return sorted(all_websites)[1:]


def get_all_terms():
    """
    get_all_terms sends an API request to PeterPortal API and retrieve all information
    regarding UCI courses and save past terms that offered the course
    """
    
    try:
        response = requests.get("https://api.peterportal.org/rest/v0/courses/all")
        all_info = response.json()
        for course in all_info:
            ALL_TERMS[course['id']] = course['terms']

    except:
        print("Failed to attain API Request")


def get_courses(url):
    """
    get_courses takes in each invidiual website and scrape all courses provided in the url
    and their information (course id, course name, units, description, restriction, and prereq).
    All the information is organized in a dictionary: id: Course Object
    """
    
    course_dict = {}
    soup = request_websites(url)
    for elem in soup.find_all('div', class_='courseblock'):
        header = elem.find('p', class_='courseblocktitle')
        section = elem.find('div', class_='courseblockdesc')
        get_info = section.find_all('p')
        course_info = Course()
        
        course_info.set_header_info(header)

        for x in range(len(get_info)):
            info = get_info[x].text
            ge = get_info[x].find('strong')
            if x == 0:
                course_info.set_description(info)
            elif 'Repeatability:' in info and 'Restriction:' not in info:
                course_info.set_repeatability(info)
            else:
                course_info.set_information(info)

            course_info.set_ge(ge)
            course_info.set_terms(ALL_TERMS[course_info.course_key.replace(' ', '')])

        course_dict[course_info.course_key] = course_info
    return course_dict


def write_courses():
    """
    write_courses calls get_courses_websites to collect all current UCI courses from UCI General Catalogue.
    Using those collected websites, get_courses will be called to scrape all of the courses offered at UCI by departments.
    All information regarding courses will be saved in uci_courses.sql.
    All information regarding GE courses will be saved in alll_GEs.sql.
    """

    websites = get_courses_websites()
    course_names = []
    write_ge = open('../database/all_GEs.sql', 'w')

    with open('../database/uci_courses.sql', 'w') as f:
        for each_url in websites:
            uci_course = get_courses(each_url)
            for key,value in uci_course.items():
                course_names.append(key)
                f.write('INSERT INTO courses VALUES ("' + key + '","' + value.name.strip() +  '","' + value.department + '","' + 
                        value.units + '","' + value.description + '","' + value.prerequisite + '","' + 
                        value.restriction + '","' + value.repeatability + '","' + value.corequisite + '","' + 
                        value.ge_string + '","' + value.past_terms + '");' + '\n')
                for cat in value.ge_list:
                    write_ge.write('INSERT INTO courses_in_ges (courseId, geId) VALUES ("' + key + '","' + cat + '");' + '\n')
    
    write_ge.close()

    with open('../data/data.json', 'w') as f: 
        json.dump(course_names, f,indent=4)


if __name__ == "__main__":

    get_all_terms()
    write_courses()
