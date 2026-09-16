# Task: List Comprehension & Filtering
# Instructions: Complete the function to return only even IDs 
# greater than 100, sorted in descending order.


def filter_orders(order_ids):
    a = list()
    for x in order_ids: 
      if ((x % 2) == 0): a.append(x) 
    b = sorted(a,reverse=True)
    return b

# Test Case
test_data = [10, 105, 120, 44, 202, 300, 75, 110]

# Expected Output: [300, 202, 120, 110]
print(filter_orders(test_data))
 
