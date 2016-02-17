from .test_base import TestBaseClass


class TestLoginLogout(TestBaseClass):
	"""Test '/auth/login' url."""

	def test_successful_login(self):
		"""Test successful login attempt."""
		# create user
		self.create_user(self.user1)
		# attempt login
		response = self.client.post('/auth/login/', self.user1)

		self.assertTrue('token' in response.data)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.status_text, 'OK')
		self.assertNotEqual(response.data.get('token'), None)
