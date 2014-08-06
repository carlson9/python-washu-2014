import bob
import unittest

class BobTest(unittest.TestCase):
    def test_addressBob_question(self):
        self.assertEqual(bob.responseBob("hey how are ya?"), 'Sure.')
        self.assertEqual(bob.responseBob("don't you hate pants?  I sure do.    "), 'Sure.')

    def test_addressBob_yell(self):
        self.assertEqual(bob.responseBob("WHAT THE HELL MAN!"), 'Woah, chill out!')
        self.assertEqual(bob.responseBob("   YOU'RE STUPID!!! "), 'Woah, chill out!')
        self.assertEqual(bob.responseBob("I DON'T WANT 7 CHILDREN!  "), 'Woah, chill out!')

    def test_addressBob_nothing(self):
        self.assertEqual(bob.responseBob(), 'Fine. Be that way!')
        self.assertEqual(bob.responseBob(""), 'Fine. Be that way!')

    def test_addressBob_other(self):
        self.assertEqual(bob.responseBob("2343"), 'Whatever.')
        self.assertEqual(bob.responseBob("You're a jerk."), 'Whatever.')
        self.assertEqual(bob.responseBob("/4?"), 'Whatever.')
        self.assertEqual(bob.responseBob(435), 'Whatever.')

if __name__ == '__main__':
    unittest.main()
