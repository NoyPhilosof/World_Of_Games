
def add_scores(difficulty):
    """
    this func calculates how many points a user just won and tries to add them to Scores.txt
    if this file does not exist, it creates it with the number of points just calculated
    if this file exists, the value in it is added to the "just won" value and the file is re-written
    :param difficulty: an integer representing the difficulty of the game just won
    :return: user's current number of points
    """
    points_of_winning = (difficulty * 3) + 5
    try:
        with open('Scores.txt', 'r') as scores:
            content = scores.readlines()
    except FileNotFoundError:
        with open('Scores.txt', 'w') as scores:
            scores.write(str(points_of_winning))
            return points_of_winning
    else:
        total_points = (int(content[0]) + points_of_winning)
        some_kind_of_comment = content[1]
        all = str(f'{total_points} \n{some_kind_of_comment}')
        with open('Scores.txt', 'w') as scores:
            scores.write(all)
        return total_points


print(add_scores(1))
