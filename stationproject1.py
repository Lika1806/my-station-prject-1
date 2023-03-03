import random


def pick_template():
    """with this function the program checks if the entered text is correct or not and chooses a random pattern if the user wanted it"""
    template = ""
    input_is_valid = False
    while not input_is_valid:
        template = input("Pick one of three templates (1, 2 or 3) or type 0 to get a random template: ")
        if template == "0" or template == "1" or template == "2" or template == "3":
            template = int(template)
            input_is_valid = True
        else:
            print("input is invalid, pleas try again: ")
    if template == "0":
        template = random.randint(1, 3)
    return template


def type_word(self):
    """this function creates template for writing input text to make it easier to work"""
    return input(f"Input {self}: ").lower()


chosen_template = pick_template()
if chosen_template == 1:
    number1 = type_word("number")
    if number1 == "1":
        measure_of_time = type_word("measure of time(second, minute, hour etc.)")
    else:
        measure_of_time = type_word("measure of time(plural)(seconds, minutes, hours etc.)")
    mode_of_transportation = type_word("mode of transportation")
    adjective1 = type_word("adjective")
    adjective2 = type_word("another adjective")
    noun1 = type_word("noun (plural)")
    color = type_word("color")
    part_of_body = type_word("part of body")
    verb = type_word("verb")
    number2 = type_word("number")
    if number2 == "1":
        noun2 = type_word("noun")
    else:
        noun2 = type_word("noun(plural)")
    noun3 = type_word("another noun")
    part_of_body2 = type_word("part of body")
    verb2 = type_word("verb")
    noun4 = type_word("noun")
    adjective3 = type_word("adjective")
    silly_word = type_word("silly word")
    noun5 = type_word("noun")
    print(f"""
    It was about {number1} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}.
    The hospital is a/an {adjective1} place, there are a lot of {adjective2} {noun1} here. There are nurses here who
    have {color} {part_of_body}. If someone wants to come into my room I told them that they have to {verb}
    first. I've decorated my room with {number2} {noun2}. Today I talked to a doctor and they were wearing a {noun3}
    on their {part_of_body2}. I heard that all doctors {verb2} {noun4} every day for breakfast. The most {adjective3}
    thing about being in the hospital is {silly_word} {noun5}!""")
elif chosen_template == 2:
    proper_noun = type_word("person name")
    noun = type_word("noun")
    adjective_1 = type_word("adjective (feeling)")
    verb1 = type_word("verb")
    adjective2 = type_word("adjective")
    animal1 = type_word("animal")
    verb2 = type_word("verb")
    color1 = type_word("color")
    verb3 = type_word("verb")
    adverb = type_word("adverb (ending with ly)")
    number1 = type_word("number")
    if number1 == "1":
        measure_of_time = type_word("measure of time(second, minute, hour etc.)")
    else:
        measure_of_time = type_word("measure of time(plural)(seconds, minutes, hours etc.)")
    color2 = type_word("color")
    animal2 = type_word("animal")
    number2 = type_word("number")
    silly_word = type_word("silly word")
    noun2 = type_word("noun")
    print(f"""
    This weekend I am going camping with {proper_noun}. I packed my lantern, sleeping bag, and {noun}. 
    I am so {adjective_1} to {verb1} in a tent. I am {adjective2} we might see a(n) {animal1}, 
    I hear they're kind of dangerous. While we're camping, we are going to hike, fish, and {verb2}.
    I have heard that the {color1} lake is great for {verb3}. 
    Then we will {adverb} hike through the forest for {number1} {measure_of_time}. 
    If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! 
    At night we will tell {number2} {silly_word} stories and roast {noun2} around the campfire!!
    """)
else:
    proper_noun = type_word("person name")
    adjective1 = type_word("adjective")
    color1 = type_word("color")
    animal1 = type_word("animal")
    place1 = type_word("place")
    adjective2 = type_word("adjective")
    creature1 = type_word("magical creature (Plural)")
    adjective3 = type_word("adjective")
    creature2 = type_word("another magical creature (Plural)")
    room1 = type_word("room in a house")
    noun1 = type_word("noun (plural)")
    noun2 = type_word("another noun")
    noun3 = type_word("another noun (plural)")
    adjective4 = type_word("adjective")
    noun4 = type_word("noun")
    number1 = type_word("number")
    measure_of_time = type_word("measure of time")
    verb1 = type_word("verb (ending in ing)")
    adjective5 = type_word("adjective")
    noun5 = type_word("noun")
    print(f"""
    Dear {proper_noun}, I am writing to you from a {adjective1} castle in an enchanted forest. 
    I found myself here one day after going for a ride on a {color1} {animal1} in {place1}.
    There are {adjective2} {creature1} and {adjective3} {creature2} here! 
    In the {room1} there is a pool full of {noun1}. 
    I fall asleep each night on a {noun2} of {noun3} and dream of {adjective4} {noun4}. 
    It feels as though I have lived here for {number1} {measure_of_time}(s). 
    I hope one day you can visit, although the only way to get here now is {verb1} on a {adjective5} {noun5}!!
    """)
