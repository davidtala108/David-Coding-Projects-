import unittest

from queue_linked_list import *

class MyTestCase(unittest.TestCase):
    def test_queue(self):
        q = QueuekLinkedList(5)
        q.enqueue('thing')
        q.dequeue()
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(),0)

    def test_queue2(self):
        q = QueuekLinkedList(5)
        q.enqueue(1)
        q.enqueue(1)
        q.enqueue(1)
        q.enqueue(1)
        q.enqueue(1)
        self.assertFalse(q.is_empty())
        self.assertTrue(q.is_full())
        self.assertEqual(q.size(), 5)
    def test_queue3(self):
        q = QueuekLinkedList(3)
        q.enqueue(1)
        q.enqueue(1)
        q.enqueue(1)
        self.assertTrue(q.is_full)
        with self.assertRaises(IndexError):
            q.enqueue(1)
    def test_queue4(self):
        q = QueuekLinkedList(3)
        self.assertTrue(q.is_empty())
        with self.assertRaises(IndexError):
            q.dequeue()
    def test_queue5(self):
        q= QueuekLinkedList(9)
        q.enqueue("Hello")
        q.enqueue(49)
        q.enqueue(50)
        q.enqueue([2,4,5,6,7,8])
        x= q.dequeue()
        self.assertEqual(x,"Hello")
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(),3)
    def test_queue6(self):
        q = QueuekLinkedList(10)
        q.enqueue("type beat")
        q.enqueue(49)
        q.enqueue(50)
        q.enqueue([2, 4, 5, 6, 7, 8])
        x = q.dequeue()
        self.assertEqual(x, "type beat")
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 3)

    def test_queue7(self):
        q = QueuekLinkedList(3)
        q.enqueue("Hi")
        q.enqueue(49)
        q.dequeue()
        q.enqueue(50)
        q.dequeue()
        q.enqueue(3)
        q.enqueue(10)
        q.dequeue()
        q.enqueue(12)
        x = q.dequeue()
        self.assertEqual(x, 3)
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 2)

    def test_queue8(self):
        q = QueuekLinkedList(3)
        q.enqueue("Hi")
        q.enqueue(49)
        q.dequeue()
        q.dequeue()
        q.enqueue(3)
        q.enqueue(10)
        q.enqueue(12)
        self.assertFalse(q.is_empty())
        self.assertTrue(q.is_full())
        self.assertEqual(q.size(), 3)
    def test_queue10(self):
        q = QueuekLinkedList(5)
        q.enqueue("Hi")
        q.enqueue(49)
        q.enqueue(3)
        q.enqueue(10)
        q.enqueue(12)
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.dequeue()
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 0)


if __name__ == '__main__':
    unittest.main()
