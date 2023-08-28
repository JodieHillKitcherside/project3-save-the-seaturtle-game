def slowprint(all_strings):
    """
    Runs all string in python terminal
    """
    for each_character in all_strings + "\n":
            sys.stdout.write(each_character)
            sys.stdout.flush()
            time.sleep(1/17)