
import random

rannum = random.randint(1, 100)
attempt = 7
count = []

for i in range(attempt):
    while True:
        try:
            usernum = int(input("Enter your guess number: "))

            if usernum < 1 or usernum > 100:
                print("Enter a number between 1 and 100.")
                continue

            break

        except ValueError:
            print("Invalid input! Please enter an integer.")

    count.append(usernum)

    if usernum == rannum:
        print(f"You Won! Attempts: {len(count)}")
        break
    elif usernum > rannum:
        print("Too High")
        print(f"Attempt remaining: {attempt - len(count)}")
    else:
        print("Too Low")
        print(f"Attempt remaining: {attempt - len(count)}")

else:
    print(f"Game Over! The number was: {rannum}")
