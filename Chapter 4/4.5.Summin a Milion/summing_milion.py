'''
4-5. Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.
'''

million_list=list(range(1,1000001))

print("MAX is: ",max(million_list))
print("MIN is: ",min(million_list))
print("SUM items from the million_list: ", sum(million_list))