from unittest import result
import unittest
#from Monty_Hall.monty_hall import s
import monty_hall as mh
class Tests(unittest.TestCase):
    def test_Door_Generator(self):
        doors = mh.Door_Generator(10)
        sum = 0
        for i in doors:
            sum += i
        self.assertEqual(sum, 1, "Shoud be 1")
    def test_Door_Generator_Neg(self):
        self.assertEqual(mh.Door_Generator(-10), "Error", "Shoud be Error")
    def test_Door_Generator_Str(self):
        self.assertEqual(mh.Door_Generator("-10"), "Error", "Shoud be Error")
    def test_Door_Generator_List(self):
        self.assertEqual(mh.Door_Generator([10,11]), "Error", "Shoud be Error")
    def test_Door_Generator_Zero(self):
        self.assertEqual(mh.Door_Generator(0), "Error", "Shoud be Error")
    def test_Door_Generator_One(self):
        self.assertEqual(mh.Door_Generator(1), "Error", "Shoud be Error")
    def test_Door_Generator_Two(self):
        self.assertEqual(mh.Door_Generator(2), "Error", "Shoud be Error")
    def test_Door_Generator_Three(self):
        doors = mh.Door_Generator(3)
        sum = 0
        for i in doors:
            sum += i
        self.assertEqual(sum, 1, "Shoud be 1")

    def test_Door_Check_Right(self):
        self.assertEqual(mh.Door_Check([0,1,0], 1), 1, "Shoud be 1") 
    def test_Door_Check_Right_Zero_Lim(self):
        self.assertEqual(mh.Door_Check([1,0,0], 0), 1, "Shoud be 1")  
    def test_Door_Check_Right_Max_Lim(self):
        self.assertEqual(mh.Door_Check([0,0,1], 2), 1, "Shoud be 1")       
    def test_Door_Check_Wrong(self):
        self.assertEqual(mh.Door_Check([0,1,0], 2), 0, "Shoud be 0") 
    def test_Door_Check_Neg(self):
        self.assertEqual(mh.Door_Check([0,1,0], -1), 0, "Shoud be 0")
    def test_Door_Check_Beyond_Lim(self):
        self.assertEqual(mh.Door_Check([0,1,0], 10), 0, "Shoud be 0")  
    


if __name__ == '__main__':
    unittest.main()