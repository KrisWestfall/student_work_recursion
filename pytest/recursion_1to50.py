


def recursive_guess(low, high, correct_num):
    print("Making guess:")
    mid = (high + low)//2
    if correct_num == mid:
        print("Your number is: ", mid)
    elif correct_num > mid:
        print(mid)
        print("Too Low")
        low = mid + 1
        recursive_guess(low, high, correct_num)
    else:
        print(mid)
        print("Too High")
        high = mid
        recursive_guess(low, high, correct_num)

user_guess = int(input("Choose a number between 1 and 50: "))
recursive_guess(1, 50, user_guess)