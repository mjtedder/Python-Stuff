prices = {
  "Banana": 4,
  "Apple": 2,
  "Orange": 1.5,
  "Pear": 3
}

stock = {
  "Banana": 6,
  "Apple": 0,
  "Orange": 32,
  "Pear": 15
}

print ("=" * 30)
print ("Welcome to Python Supermarket!")
print ("=" * 30)
print("")

for food in prices:
    print (food)
    print ("Price: %s" % prices[food])
    print ("Stock: %s" % stock[food])
    print("")

## Compute Bill Function ##

def compute_bill(food):
  total = 0
  for item in food:
    total = total + prices[item]
  return total


