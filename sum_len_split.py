try:
    numbers = input("Enter numbers separated by space: ")
    nums = list(map(int, numbers.split()))
    
    avg = sum(nums) / len(nums)
    print("Average:", avg)

except ValueError:
    print("Please enter only numbers!")
except ZeroDivisionError:
    print("No numbers entered!")