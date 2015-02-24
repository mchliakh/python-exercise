import emailchecker
import unittest

class TestSequenceFunctions(unittest.TestCase):

  def test_existing_email(self):
    self.assertTrue(emailchecker.check_if_email_exists('justin.bieber@gmail.com'))

  def test_invalid_email(self):
    self.assertRaises(Exception, emailchecker.check_if_email_exists, 'hello')

  def test_non_existent_email(self):
    self.assertFalse(emailchecker.check_if_email_exists('definitely.not.an@existing.email'))

if __name__ == '__main__':
    unittest.main()
