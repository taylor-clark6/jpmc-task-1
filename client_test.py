from unittest import TestCase

import client

def test_get_ratio(self, priceA, priceB):
    test = self.getRatio(priceA, priceB)
    if (priceB != 0 and test != priceA/priceB):
        self.fail()
    elif (test == None):
        print("Test passed")
    else:
        print("Test passed")

print("Testing case 1: ")
test_get_ratio(client, 2, 1)

print("Testing case 2: ")
test_get_ratio(client, 1, 2)

print("Testing case 3: ")
test_get_ratio(client, 1, 0)

print("Testing case 4:")
test_get_ratio(client, 0, 2)