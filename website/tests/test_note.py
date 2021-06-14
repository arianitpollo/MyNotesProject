import unittest
import flask.testing
from base import BaseTestCase


class NotePostTests(flask.testing):

    # Ensure a logged in user can add a new post
    def test_user_can_post(self):
        flask.testing.Client
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ap@gmail.com", password="1234567"),
                follow_redirects=True
            )
            response = self.client.post(
                '/',
                data=dict(data="data1"),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'New entry was successfully posted. Thanks.',
                          response.data)


if __name__ == '__main__':
    unittest.main()