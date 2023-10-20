def dog_years_to_human_years(dog_years):
    if dog_years == 1:
        human_years = 15
    elif dog_years == 2:
        human_years = 15 + 9
    else:
        human_years = 15 + 9 + 5 * (dog_years - 2)
    return human_years

dog_years = int(input("Enter dog's age in dog years: "))
human_years = dog_years_to_human_years(dog_years)
print(f"The dog's age in human years is approximately {human_years} years.")
