# creating a class called school with four main functions for training, registration, gpa calculation  and testing
import random
from tabulate import tabulate

class School:
    def __init__(self):
        self.name = input('What is your name : ')
        self.major = input('What is your major : ')
        self.level = input('What grade level are you in : ')
        self.department = input('What department are you in : ')
        self.phone_number = input('What is your phone number : ')
        # while loop to authenticate the user email and make sure it is a valid emaail
        while True:
            self.email = input('What is your email : ')
            if '@' in self.email and '.com' in self.email:
                break
            else:
                print('Please enter a valid email address.')
        self.password = input('What is your password : ')
        while len(self.password) < 8 or not self.password.isalnum():
            self.password = input('Password should be at least 8 characters long and contain only alphanumeric characters. Please try again: ')
        self.location = input('What is your location : ')
        self.graduation_year = input('When do you plan to graduate : ')
        while True:
            self.password = input('Input your password : ')
            if len(self.password) >= 8 and self.password.isalnum():
                break
            else:
                print('Password should be at least 8 characters long and contain only alphanumeric characters.')
        self.location = input('What is your location : ')
        self.graduation_year = input('when do you plan to graduate : ')
        self.students = []
        self.courses = []
        self.faculty = []
        self.grades = []
        self.score = 0
        self.total_score = 0
    # creating the function to handle the training but with multiple loops depending on the students convinience and mode of study .
    def training(self):
        while True:
            print('\nChoose your training mode:')
            print('1. Online')
            print('2. In-person')
            print('3. Both')
            print('4. Return to main menu')
            mode = input('Enter your choice: ')
            if mode == '1':
                print('Redifining your path to the online Web Development and web infrastructural development ')
                self.html_content()
            elif mode == '2':
                self.create_school_content()
                self.html_content()
            elif mode == '3':
                print('Redifining your path to the online Web Development and web infrastructural development ')
                self.html_content()
                self.create_school_content()
            # closing the while loop
            elif mode == '4':
                return
    #  function to handle the html , css and javascript content , beign displayed in the tupple or list 
    def html_content(self):
        while True:
            print('\nChoose your course content:')
            print('1. HTML')
            print('2. CSS')
            print('3. JavaScript')
            print('4. Return to main menu')
            course = input('Enter your choice: ')
            if course == '1':
                self.courses.append('HTML')
                print('HTML content:\n- Hypertext Markup Language (HTML) is the standard markup language used to create web pages.')
                print('- HTML documents consist of elements, attributes, and text content.')
                print('- HTML elements are the building blocks of HTML documents.')
                print('- HTML tags are used to define the structure of a document.')
            elif course == '2':
                self.courses.append('CSS')
                print('CSS content:\n- Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in HTML or XML.')
                print('- CSS is used to add style to a web page by linking it to an HTML document.')
                print('- CSS rules define')
                print('- how HTML elements should be displayed on screen, on paper, or in other media.')
                print('- CSS selectors select HTML elements to style.')
                print('- CSS properties define the appearance and behavior of selected HTML elements.')
            elif course == '3':
                self.courses.append('JavaScript')
                print('JavaScript content:\n- JavaScript is a high-level, interpreted programming language.')
                print('- JavaScript is a client-side scripting language.')
                print('- JavaScript can be embedded in HTML pages or in external .js files.')
                print('- JavaScript is used to make web pages interactive and dynamic.')
                print('- JavaScript is widely used for client-side scripting, as it allows web pages to respond to user actions.')
                print('- JavaScript is used for handling events, validating forms, and creating dynamic content.')
            elif course == '4':
                break
            else:
                print('Invalid choice. Please try again.')
            # creating a loop to ask the user if they want to continue with the same course or move to another one
            while True:
                print('\nDo you want to continue with this course?')
                print('1. Yes')
                print('2. No')
                choice = input('Enter your choice: ')
                if choice == '1':
                    self.recap_quiz()
                    break
                elif choice == '2':
                    break
                else:
                    print('Invalid choice. Please try again.')
            # closing the while loop
            print('Your training has been completed.')
            return
    # creating a recap quiz function for the students , making it simple but interactive to cover the student studies  and givving the final score for each student out of 10
    def recap_quiz(self):
        total_score = 0
        max_score = 0
        while True:
            # a 10 question recap quiz with a question then prompting for the user input and if the user input is corect , score is chansged 
            print('\nRecap Quiz:')
            print('Question 1: What does the term HTML mean ? ')
            print('A. Hypertext Markup Language')
            print('B. Hypertext Transfer Protocol')
            print('C. Hypertext Markup Language')
            print('D. Hyper text Markup Language module')
            answer = input('Enter your answer(eg  A,B,C,D): ')

            if answer == 'C. Hypertext Markup Language' or answer == 'C':
                total_score += 1
                print('Correct!')
            else:
                print('Incorrect!')
                print('The correct answer is C. Hypertext Markup Language')
            print('Question 2: What does CSS stand for?')
            print('A. Cascading Styling  Sheets')
            print('B. Cascading Style Sheets')
            print('C. Colorful Style Sheets')
            print('D. Computer Style Sheets')
            answer = input('Enter your answer(eg  A,B,C,D): ')
            if answer == 'B. Cascading Style Sheets' or answer == 'B':
                total_score += 1
                print('Correct!')
            else:
                print('Incorrect!')
                print('The correct answer is B. Cascading Style Sheets')
            print('Question 3: Which of the following is a client-side scripting language?')
            print('A. Java')
            print('B. JavaScript')
            print('C. Python')
            print('D. Ruby')
            answer = input('Enter your answer(eg  A,B,C,D): ')
            if answer == 'B. JavaScript' or answer == 'B':
                total_score += 1
                print('Correct!')
            else:
                print('Incorrect!')
                print('The correct answer is B. JavaScript')
            print('Question 4: Which of the following is a clossing tag? ')
            print('A. </p> ')
            print('B. <div> ')
            print('C. <span> ')
            print('D. <html> ')
            answer = input('Enter your answer(eg  A,B,C,D): ')
            if answer == 'A. </p> ' or answer == 'A':
                total_score += 1
                print('Correct!')
            else:
                print('Incorrect!')
                print('The correct answer is A. </p> ')
            # questions to test their knowledge in css and javeascripts as a language 
            print('Question 5: Which CSS property allows you to control the background color of an element?')
            print('A. background-color')
            print('B. back-color')
            print('C. color-background')
            print('D. background')
            answer = input('Enter your answer(eg  A,B,C,D): ')
            if answer == 'A. background-color' or answer == 'A':
                total_score += 1
                print('Correct!')
            else:
                print('Incorrect!')
                print('The correct answer is A. background-color')
            print('Question 6: Which of the following is a tag used to define a section in an HTML document?')
            print('A. <section> ')
            print('B. <div> ')
            print('C. <h1> ')
            print('D. <p> ')
            answer = input('Enter your answer(eg  A,B,C,D) : ').strip
            if answer == 'A. <section> ' or answer == 'A':
                total_score += 1
                print('Correct!')
            else:
                print('Incorrect!')
                print('The correct answer is A. <section> ')
            print('Question 7: Which of the following is a CSS property used to center align text?')
            print('A. text-align: center;')
            print('B. text-align: justify;')
            print('C. text-align: left;')
            print('D. text-align: right;')
            answer = input('Enter your answer(eg  A,B,C,D): ')
            if answer == 'A. text-align: center;' or answer == 'A':
                total_score += 1
                print('Correct!')
            else:
                print('Incorrect!')
                print('The correct answer is A. text-align: center;')
            print('Question 8: Which of the following is a CSS property used to define the font size of an element?')
            print('A. font-size: 16px;')
            print('B. font-size: 16;')
            print('C. font-size: medium;')
            print('D. font-size: 16;')
            answer = input('Enter your answer(eg  A,B,C,D): ')
            if answer == 'A. font-size: 16px;' or answer == 'A':
                total_score += 1
                print('Correct!')
            else:
                print('Incorrect!')
                print('The correct answer is A. font-size: 16px;')
            print('Question 9: Which of the following is a CSS property used to define the font weight of an element?')
            print('A. font-weight: bold;')
            print('B. font-weight: normally;')
            print('C. font-weight: lighter;')
            print('D. font-weight: " normal";')

            answer = input('Enter your answer(eg  A,B,C,D): ')
            if answer == 'A. font-weight: bold;' or answer == 'A':
                total_score += 1
                print('Correct!')
            else:
                print('Incorrect!')
                print('The correct answer is A. font-weight: bold;')
            print('Question 10: Which of the following is a CSS property used to define the font family of an element?')    
            print('A. font-family: Arial, sans-serif;')
            print('B. font-family: english;')
            print('C. font-family: french;')
            print('D. font-family: "Arial, lemon green ";')
            answer = input('Enter your answer(eg  A,B,C,D): ')
            if answer == 'A. font-family: Arial, sans-serif;' or answer == 'A':
                total_score += 1
                print('Correct!')
            else:
                print('Incorrect!')
                print('The correct answer is A. font-family: Arial, sans-serif;')
                max_score = (total_score /10)* 100
                print('\nRecap Quiz Results:')
                if max_score == 100:
                   print('Congratulations! You have mastered all the subjects!')
                   print('Your grade is A+')
                   # offer to give the students a chance to go to a css or advanced html course 
                   while True:
                        print('\nDo you want to take a CSS or advanced HTML course?')
                        print('1. CSS Course')
                        print('2. Advanced HTML Course')
                        choice = input('Enter your choice: ')
                        if choice == '1':
                           self.css_course()
                           break
                        elif choice == '2':
                         self.advanced_html_course()
                         break
                        else:
                          print('Invalid choice. Please try again.')
                elif max_score == 90:
                  print('You are a very good and briliant student!')
                elif 80<max_score>90 :
                   print('You have passed!')
                elif 70<max_score<80 :
                   print('You have a good performance!')
                elif max_score < 50:
                   print('You need to study more!')
                print(f'\nYour final score is {total_score}/{max_score}')
                print('Thank you for playing the quiz!')
                break
    # creating a very interestingAPI(application programming interface) game for the students to play while taking breaks from learning but for which should be api related questions
    def api_game(self):
        print('\nAPI Game:')
        print('You will be asked to guess a movie title based on its release year.')
        print('To win, you must guess the movie title within 3 attempts.')
        attempts = 3
        while attempts > 0:
            year = random.randint(1900, 2021)
            movie_title = self.get_movie_title_by_year(year)
            print(f'What movie was released in {year}? (Attempt {attempts}):')
            guess = input('Enter your guess: ').strip()
            if guess.lower() == movie_title.lower():
                print('Congratulations! You guessed the movie title correctly.')
                break
            else:
                attempts -= 1
                print('Sorry, that is incorrect. Try again.')
        if attempts == 0:
            print('You have used up all your attempts. Better luck next')
            # creating a very interesting game based on general computer knowledge
            print('\nGeneral Computer Knowledge Game:')
            print('You will be asked to guess the type of computer component based on its description.')
            print('To win, you must guess the component type within 5 attempts.')
            attempts = 5
            while attempts > 0:
                component_type = random.choice(['CPU', 'RAM', 'Motherboard', 'GPU', 'Storage'])
                description = self.get_computer_component_description(component_type)
                print(f'What is the type of the computer component described below? (Attempt {attempts}):')
                print(description)
                guess = input('Enter your guess: ').strip()
                if guess.lower() == component_type.lower():
                    print('Congratulations! You guessed the component type correctly.')
                    break
                else:
                    attempts -= 1
                    print('Sorry, that is incorrect. Try again.')
            if attempts == 0:
                print('You have used  the component type correctly before  you were able to complete  the game')
    def create_school_content(self):
        school_info = [
            ["Week 1", "Introduction to HTML, CSS, and JavaScript"],
            ["Week 2", "HTML, CSS, and JavaScript continued"],
            ["Week 3", "Introduction to web development frameworks and libraries"],
            ["Week 4", "Web development frameworks and libraries continued"],
            ["Week 5", "Introduction to web security and privacy"],
            ["Week 6", "Web security and privacy continued"],
            ["Week 7", "Introduction to web performance optimization"],
            ["Week 8", "Web performance optimization continued"],
            ["Week 9", "Project planning and execution"],
            ["Week 10", "Project planning and execution continued"],
            ["Week 11", "Final project presentation and evaluation"],
            ["Week 12", "Final project presentation and evaluation continued"],
         ]

        teachers_info = [
           ["John Doe", "Grade 9"],
           ["Jane Smith", "Grade 10"],
           ["Mark Johnson", "Grade 11"],
           ["Sarah Wilson", "Grade 12"],
         ]

        print('\nCreating School Content:')
        print('This will include information about the school, its curriculum, and the subjects taught.')
        print('Redefining your path to the in-person Web Development and web infrastructural development.')

    # Displaying training schedule
        print('\nGrade 9-12 training schedule:')
        print(tabulate(school_info, headers=["Week", "Topic"], tablefmt="grid"))

    # Displaying teachers
        print('\nGrade 9-12 teachers:')
        print(tabulate(teachers_info, headers=["Teacher", "Grade"], tablefmt="grid"))

    # Closing the function
        print('\nThis is the end of the school content creation.')
        print('Please review and make any necessary adjustments.')
# calling now the function in order to make more sense 

school = School()
School.create_school_content()
School.quiz_game()
School.api_game()
School.recap_quiz()
School.general_knowledge_game()


