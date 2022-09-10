def guessing_numbers():
    print("Think the number from 0 to 1000 and I will guess this in max 10 tries ")
    print("Press enter to start")
    input()
    min_numb = 0
    max_numb = 1000
    guess_numb = ""
    while guess_numb != "you win":
        guess = int((max_numb - min_numb) // 2) + min_numb
        print(f"Your number {guess}")
        guess_numb = input().lower()
        if guess_numb == "to small":
            min_numb = guess
        elif guess_numb == "to big":
            max_numb = guess
    print("You win")


guessing_numbers()
