import unittest
from stack_array import *

class MyTestCase(unittest.TestCase):
    def test1_Basic(self):
        S = StackArray(5)
        S.push(35)
        S.push(55)
        x = S.pop()
        self.assertEqual(x, 55)
        self.assertEqual(S.size(), 1)

    def test2_Full_Empty(self):
        S = StackArray(5)
        S.push(10)
        S.push(10)
        S.push(10)
        S.push(10)
        S.push(10)
        self.assertTrue(S.is_full())
        self.assertEqual(S.size(),5)
        S.pop()
        S.pop()
        S.pop()
        S.pop()
        S.pop()
        self.assertTrue(S.is_empty())
        self.assertEqual(S.size(),0)
    def test3_Push_Pop_Peek(self):
        S = StackArray(5)
        S.push(35)
        S.push(55)
        S.pop()
        S.push(80)
        S.push(90)
        S.pop()
        S.pop()
        S.push(76)
        S.push(12)
        self.assertEqual(S.peek(), 12)
        self.assertEqual(S.size(), 3)
        self.assertFalse(S.is_empty())
        S.pop()
        S.pop()
        self.assertEqual(S.peek(), 35)
        self.assertEqual(S.size(), 1)


    def test4_Value_Error_Push(self):
        S = StackArray(5)
        S.push(10)
        S.push(10)
        S.push(10)
        S.push(10)
        S.push(10)
        with self.assertRaises(IndexError):
            S.push(10)

    def test5_Value_Error_Pop(self):
        S = StackArray(5)
        with self.assertRaises(IndexError):
            S.pop()


if __name__ == '__main__':
    unittest.main()
