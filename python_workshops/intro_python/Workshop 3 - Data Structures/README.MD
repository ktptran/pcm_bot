# Python Course - Week Three: Data Structures
Lecture: https://docs.google.com/presentation/d/1JbPlmeAEeFPsQqao-LG6mqbP5HfuoKrm5BwgaKsLLjU/edit#slide=id.g83d258b0b1_0_54

Recording: Uploading soon.


# Lecture Concepts
Today we will be covering lists, tuples, sets, and dictionaries. These are data structures to allow you to
sort your data.

For content, you can find them on the lecture slide above.


# Practice problems
* Lists
  1. Make a list containing the values 3, 4, 6, 8, and 9 in this order.
  2. Remove the value 8 from the list.
  3. Add in the value 10.
  4. Sort the list.
  5. Reverse the list.
  6. Sort the list in reverse order.
  7. Iterate through the list using and print out the "index: value"
  8. Print out the value from index 3 to the end.
  9. Print out the value from index 1 to 2.
  10. Print out the value from the start to index 3 (including index 3).
  11. What is the value at index 1?
  12. Write a statement to print out if there is a value of 1 in the list.
  13. Insert the values within the list2 into your list. list2 = [20, 25, 30]
  14. Remove the value 25 from the list.
  15. Find the min, max, and sum value of the list.
  17. Convert the list to a tuple.
* Tuple
  1. Reverse the following tuple: aTuple = (10, 20, 30, 40, 50)
  2. Create a tuple with a single item 50.
  3. Unpack aTuple = (10, 20, 30, 40) into four variables.
* Set
  1. Enter 3, 4, 6, 8, and 9 into a set.
  2. Make another set 1, 2, 3, 4.
  3. Find the union of these two sets.
  4. Find the difference between these two sets for both sets.
  5. Input the values 1, 2, 3, and 4 into the first set. How many values do you have?
* Dictionaries
  1. Navigate to Riot Games API: https://developer.riotgames.com/
  2. Login/create an account.
  3. Generate an API key.
  4. Use the code to enter into the value below to access some information and play around with the code to see what you can find.

```
import requests, json
key = 'RGAPI-f9198d1f-ce93-4d35-bd6e-5707e65ff8bb'
response = requests.get('https://na1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_FLEX_SR?api_key=' + key)
r1 = response.json()
json.dumps(r1)
r1["entries"][1]
```

All programs can be programmed in multiple ways. ![Solutions](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%203%20-%20Data%20Structures/Practice%20Problems.ipynb)
