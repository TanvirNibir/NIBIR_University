def get_season(month):
    seasons = ("Winter", "Spring", "Summer", "Autumn")

    winter = {12, 1, 2}
    spring = {3, 4, 5}
    summer = {6, 7, 8}
    autumn = {9, 10, 11}

    if month in winter:
        return seasons[0]
    elif month in spring:
        return seasons[1]
    elif month in summer:
        return seasons[2]
    elif month in autumn:
        return seasons[3]
    else:
        return "Invalid month"


month = int(input("Enter the number of the month (1-12): "))

season = get_season(month)
print(f"The season is: {season}")
