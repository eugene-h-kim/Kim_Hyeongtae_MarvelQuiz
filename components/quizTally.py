from components import vars


def total(value):
    vars.answerCount += value

    # keep adding totals until you get the final tally
    # then do some logic to see which character you selected

    if vars.answerCount > 10:
        vars.character = vars.characters[0]

        print("It's " + vars.character)

        # add some emoji icons, or show the character image using the Pillow package

    