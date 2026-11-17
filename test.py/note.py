def odd_sum(numbers:list)-> int:
    total=0
    for i in numbers:
        if i %  2!= 0:
            total+=i
    return total
print(odd_sum([3,6,8,1,5,10]))
def reverse_words(sentence: str) -> str:
    words = sentence.split()        # Step 1
    words.reverse()                 # Step 2
    return " ".join(words)          # Step 3
print(reverse_words('my name is winner,winner is joyful'))

#note on number lenghr and counting of numbers
#def count_numbers(numbers: list):
    # Count total numbers entered
   # total_count = len(numbers)

    # Count frequency of each number
   # frequency = {}
    #for num in numbers:
     #   frequency[num] = frequency.get(num, 0) + 1

    # Find repeated numbers
  #  repeated = {num: count for num, count in frequency.items() if count > 1}

   # return total_count, repeated

# Ask the user for numbers
#user_input = input("Enter numbers separated by spaces: ")
#numbers_list = [int(x) for x in user_input.split()]

# Get counts
#total, repeated_nums = count_numbers(numbers_list)

# Display results
#print(f"Total numbers entered: {total}")
#if repeated_nums:
  #  print("Repeated numbers and their counts:", repeated_nums)
#else:
   # print("No repeated numbers.")
#1. Common String Methods in Python
#These are built-in functions for string manipulation.

#Method	What it does	Example
#.upper()	Converts string to uppercase	"hello".upper() → "HELLO"
#.lower()	Converts string to lowercase	"HELLO".lower() → "hello"
#.capitalize()	First letter uppercase, rest lowercase	"python".capitalize() → "Python"
#.title()	Capitalizes first letter of each word	"python is fun".title() → "Python Is Fun"
#.strip()	Removes spaces (or given chars) from start & end	" hello ".strip() → "hello"
#.lstrip() / .rstrip()	Removes spaces (or chars) from left or right	" hi".lstrip() → "hi"
#.replace(old, new)	Replaces part of a string	"I like Java".replace("Java", "Python") → "I like Python"
#.find(sub)	Finds the position of a substring	"banana".find("na") → 2
#.count(sub)	Counts how many times a substring appears	"banana".count("na") → 2
#.startswith(sub)	Checks if string starts with something	"hello".startswith("he") → True
#.endswith(sub)	Checks if string ends with something	"hello".endswith("lo") → True
#.join(list)	Joins elements of a list into a string	" ".join(["Hi", "there"]) → "Hi there"
#.split(delimiter)	Splits a string into list	"a,b,c".split(",") → ['a', 'b', 'c']

#2. List Methods (like .reverse())
#When you split a string into a list, these methods become useful:

#Method	What it does	Example
#.append(x)	Adds an element to the end	nums.append(5)
#.insert(i, x)	Adds element at position i	nums.insert(1, "hi")
#.pop(i)	Removes and returns element at i	nums.pop(2)
#.remove(x)	Removes first occurrence of x	nums.remove("hi")
#.sort()	Sorts list ascending	nums.sort()
#.reverse()	Reverses order in place	nums.reverse()
#sorted(list)	Returns a sorted copy	sorted(nums)

#How to use them in coding
#Let’s mix a few together in an example:

#python
#Copy
#Edit
#sentence = "   python is powerful and fun   "

# Step 1: Remove extra spaces
#cleaned = sentence.strip()  # "python is powerful and fun"

# Step 2: Capitalize each word
#title_case = cleaned.title()  # "Python Is Powerful And Fun"

# Step 3: Split into words
#words = title_case.split()  # ['Python', 'Is', 'Powerful', 'And', 'Fun']

# Step 4: Reverse words
#words.reverse()  # ['Fun', 'And', 'Powerful', 'Is', 'Python']

# Step 5: Join back into string
#final_sentence = " ".join(words)  # "Fun And Powerful Is Python"

#print(final_sentence)
#.get(key, default_value) is a dictionary method:It looks for the key in the dictionary...If the key exists → it returns the value.If the key does not exist → it returns the "default_value" we set (in this case "Not Found").