from exact_change import exact_change

testing_vals = [
       [100, (0,0,0,4)],
       [0, (0,0,0,0)],
       [41, (1,1,1,1)],
       [2500,(0,0,0,100)],
       [-1, None],
       ["Hello", None]
   ]

print(f"Testing Return Type, Expecting: {type(())} Actual: {type(exact_change(0))}")
if type(()) == type(exact_change(0)):
   print("Test Succeeded!\n")
else:
   print("Test Failed!\n")

print(f"Testing Return Type, Expecting lenght: {len((0,0,0,0))} Actual: {len(exact_change(0))}")
if len((0,0,0,0)) == len(exact_change(0)):
   print("Test Succeeded!\n")
else:
   print("Test Failed!\n")

for val in testing_vals:
   print(f"Testing Input:{val[0]} Expecting: {val[1]} Actual: {exact_change(val[0])}")
   if (val[1] == exact_change(val[0])):
      print("Test Succeeded!\n")
   else:
      print("Test Failed!\n")
   