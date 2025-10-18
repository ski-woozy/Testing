#Project Title
print("\nProject Title: Find Longest Word\n")

#Function to count the number of trailing zeros in an integer
def end_zeros(a: int) -> int:
    count = 0
    a = str(a)[::-1]
    for num in a:
        if num == '0':
            count += 1
            continue
        else:
            break
    return count

#User-Program Interaction
user_Input = int(input("Type an integer to find the number of trailing zeros it has\n> "))
print("The number of trailing zeros is:", end_zeros(user_Input), "\n")