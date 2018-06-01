import unittest
from robber import expect

from dog import Dog


class DogTest(unittest.TestCase):
    def test_should_have_name_dog(self):
        dog = Dog()

        expect(dog.get_name()).to.eq("scamp")
