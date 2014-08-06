import unittest
import lab3

class PigTest(unittest.TestCase):

    def test_shout(self):
        self.assertEqual(lab3.shout("hello"),"HELLO!")
        self.assertEqual(lab3.shout("I hate Dino? "),"I HATE DINO!")
        self.assertEqual(lab3.shout("I HATE DINO!"), "I HATE DINO!")
        self.assertEqual(lab3.shout(3),"3!")
        self.assertEqual(lab3.shout("i hate dino."), "I HATE DINO!")
        self.assertEqual(lab3.shout("i hate dino!?    "), "I HATE DINO!")

    def test_reverse(self):
        self.assertEqual(lab3.reverse("aardvark"), "kravdraa")
        self.assertEqual(lab3.reverse("3245 4478"), "8744 5423")
        self.assertEqual(lab3.reverse(32454478), "")
        self.assertEqual(lab3.reverse("I HATE DINO!!!  "), "  !!!ONID ETAH I")
        
    def test_reversewords(self):
        self.assertEqual(lab3.reversewords("I hate Dino!"), "!Dino hate I")
        self.assertEqual(lab3.reversewords("I hate Dino! I also hate Myunghoon. I hate myself too?"),"!Dino hate I .Myunghoon hate also I ?too myself hate I")


 #   def test_reversewordletters(self):

 #   def test_piglatin(self):


if __name__ == '__main__':
    unittest.main()
