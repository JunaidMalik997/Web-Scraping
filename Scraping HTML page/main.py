from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    #print(content)

    soup = BeautifulSoup(content, 'lxml')           #create instance of BeautifulSoup
    #print(soup.prettify())
    
    #grab all the html tags
    # tags = soup.find('h5')     #find method searches for the first element
    # print(tags) 

    courses_html_tags = soup.find_all('h5')
    print(courses_html_tags)                 #return type --> list
    for course in courses_html_tags:
        print(course.text)