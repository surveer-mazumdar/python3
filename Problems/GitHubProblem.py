#
# You are part of a team that is building a social dashboard for open source developers. You have been assigned to build and test a C# class that returns the score for a programmer by looking at certain metrics on github. 
#
#
# 1. Input will be the github username - for example 'antirez'
#
# 1. Date is an optional input, and will default to current date
#
# 1. The score depends on two parts - what actions the user has take on that day, and how many interactions other users have had with this user.
#
# 1. To find out actions taken by a user, call the /users/<userid>/events/public API. For example - https://api.github.com/users/antirez/events/public
#
# 1. To find out interactions with other users, call /users/<userid>/received_events API. For example - https://api.github.com/users/antirez/received_events
#
# 1. For now, we will use a simple formula for the score
#
#     Score = count of public events for the day + count of received events for the day
#
# 1. Over time, the formula will evolve - possibly by introducing weights to different type of events
#
#
#
# You are required to make this a production quality API, with the following characteristics - 
#
#
# 1. Unit tests are mandatory - including one positive and one negative test case
#
# 1. Must have logging and exception handling
#
# 1. Use any third party libraries that will simplify your task
#
#
#
# Important:
#
# =========
#
# Create a personal access token to access github apis. Create an access token from this page - https://github.com/settings/tokens/new, and then pass the access token to the API you are invoking. See https://developer.github.com/v3/#authentication for more information.

#help: https://stackoverflow.com/questions/17622439/how-to-use-github-api-token-in-python-for-requesting
#9149e77ded89f2dace6cfd6a62f406c0df9087f3

import requests
import logging

logging.basicConfig(filename='./files/myapp.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)


class GitHubWrapper:

    __baseUrl = "https://api.github.com/"
    __token = "9149e77ded89f2dace6cfd6a62f406c0df9087f3"
    __headers = ""
    __publicEvents = []
    __eventsRecieved = []
    __githubUser = ""

    def __init__(self):
        #githubObj = Github("9149e77ded89f2dace6cfd6a62f406c0df9087f3")
        self.__headers = {'Authorization': 'token ' + self.__token}
        self.getInputsFromUser()
        self.getUserEventsRecieved()
        self.getUserPublicEvents()
        self.getScore()

    def getInputsFromUser(self):

        githubUserName = input("Enter Github User Name: ");

        if githubUserName.isdigit() is True:
            self.getInputsFromUser()
        else:
            self.__githubUser = githubUserName

    def getUserPublicEvents(self):
        try:
            responseObj = requests.get(self.__baseUrl+"users/"+self.__githubUser+"/events/public", headers=self.__headers)
            if responseObj.status_code == 200:
                response = responseObj.json()
            else:
                response = []

            self.__publicEvents = response
        except Exception as e:
            logger.exception(e)

    def getUserEventsRecieved(self):
        try:
            responseObj = requests.get(self.__baseUrl + "users/"+self.__githubUser+"/received_events", headers=self.__headers)
            if responseObj.status_code == 200:
                response = responseObj.json()
            else:
                response = []

            self.__eventsRecieved = response
        except Exception as e:
            logger.exception(e)

    def getScore(self):
        score = len(self.__eventsRecieved) + len(self.__publicEvents)
        print("Score is "+ str(score))


classObj = GitHubWrapper()