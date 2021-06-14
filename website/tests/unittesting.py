import  unittest
from main import app
from website.Models import models


def user_can_access_homepage(s):
    tester = app.test_client(s)
    response = tester.get("/")
    statuscode = response.status_code
    return statuscode

def contenttype_of_loginpage(s):
    tester = app.test_client(s)
    response = tester.get("/login")
    return response.content_type

def data_of_note():
    note = models.Note()
    note.data = "niti"
    return note.__str__()

def check_password_length():
    user = models.User()
    user.password="123"
    return len(user.password)




class FlaskTestCase(unittest.TestCase):

    def test_home(self):
        self.assertEqual(user_can_access_homepage(self),200)

    def test_content(self):
        self.assertEqual(contenttype_of_loginpage(self),"text/html; charset=utf-8")

    def test_data_of_note(self):
        self.assertEqual(data_of_note(), "ni")

    def test_check_password_length(self):
        self.assertEqual(7,check_password_length())


    if __name__ == '__main__':
        unittest.main()