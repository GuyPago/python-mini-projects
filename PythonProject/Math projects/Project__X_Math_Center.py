import sys
sys.path.append('guypago/PythonProject/GeneralProjects/')
from GeneralProjects import project_3_guyhub


def mat_hub():
    while True:
        user_input = input("Welcome to Guy's Math center\n\n's' --> Series" +
                           "q --> Back to hub")
        if (user_input == 'q'):
            print("Going back to hub..")
            time.sleep(2)
