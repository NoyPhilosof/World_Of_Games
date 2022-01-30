
def add_scores(difficulty):
    """
    this func calculates how many points a user just won and tries to add them to Scores.txt
    if this file does not exist, it creates it with the number of points just calculated
    if this file exists, the value in it is added to the "just won" value and the file is re-written
    :param difficulty: an integer representing the difficulty of the game just won
    :return: user's current number of points
    """
    points_of_winning = (difficulty * 3) + 5

    try:    # try to open Scores.txt, read all lines and write them into 'content' variable (list)
        with open('Scores.txt', 'r') as scores:
            content = scores.readlines()

    except FileNotFoundError:    # in case Scores.txt doesn't exist, create it and write 'points_of_winning' into it
        with open('Scores.txt', 'w') as scores:
            scores.write(str(points_of_winning))
            return points_of_winning

    else:    # if Scores.txt exists read the first line as existing number of points
        total_points = int(content[0]) + points_of_winning

        # if there are two or more lines in Scores.txt, write the second one into future_comment variable
        if len(content) >= 2:
            future_comment = content[1]
            to_be_written = str(f'{total_points} \n{future_comment}')
            with open('Scores.txt', 'w') as scores:
                scores.write(to_be_written)
                return total_points

        # if there's only one line in the file, add the numbers and write to file
        elif len(content) == 1:
            with open('Scores.txt', 'w') as scores:
                scores.write(str(total_points))
                return total_points
