import datetime
import unittest as un
from cc import CC

class MyTestCase(un.TestCase):
	def test_dbd(self):
		d = datetime.datetime.strptime('07/03/23', '%d/%m/%y').date()
		d1 = datetime.datetime.strptime('05/03/23', '%d/%m/%y').date()
		self.assertEqual(CC('orange', 'black').days_bet_dates(d, d1), 2)


if __name__ == '__main__':
	un.main()