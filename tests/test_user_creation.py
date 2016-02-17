from .test_base import TestBaseClass


class TestUserCreation(TestBaseClass):
	"""Test the '/users/' route."""

	def test_successful_user_creation(self):
		"""Test successful post operation on '/users/' url."""
		# create user
		response = self.create_user(self.user1)

		self.assertEqual(self.user1.get('username'), response.data.get('username'))
		self.assertEqual(response.status_code, 201)
		self.assertEqual(response.status_text, 'Created')

	def test_user_creation_no_username(self):
		"""Test post on '/users/' url when username is not provided."""
		# create user
		user = {
			'password': self.fake.password()
		}
		response = self.create_user(user)
		self.assertTrue(
			'This field is required' in response.data.get('username')[0]
		)
		self.assertEqual(response.status_code, 400)
		self.assertEqual(response.status_text, 'Bad Request')

	def test_user_creation_no_password(self):
		"""Test post on '/users/' url when password is not provided."""
		# create user
		user = {
			'username': self.fake.user_name()
		}
		response = self.create_user(user)
		self.assertTrue(
			'This field is required' in response.data.get('password')[0]
		)
		self.assertEqual(response.status_code, 400)
		self.assertEqual(response.status_text, 'Bad Request')
