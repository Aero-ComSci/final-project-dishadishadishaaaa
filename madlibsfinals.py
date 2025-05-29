propernoun = []
noun = []
adj = []
verb = []
number = []

def printmadlibs():
    i = 0
    while i < 3:
        x = input("Enter a noun: ").strip(" ").replace(" ","")
        if x == "":
            x = "[nothing entered]"
        noun.append(x)
        i += 1

    i = 0
    while i < 1:
        x = input("Enter a proper noun: ").strip(" ").replace(" ","")
        if x == "":
            x = "[nothing entered]"
        propernoun.append(x)
        i += 1

    i = 0
    while i < 2:
        x = input("Enter an adjective: ").strip(" ").replace(" ","")
        if x == "":
            x = "[nothing entered]"
        adj.append(x)
        i += 1

    i = 0
    while i < 5:
        x = input("Enter a verb: ").strip().replace(" ","")
        if x == "":
            x = "[nothing entered]"
        verb.append(x)
        i += 1

    i = 0
    while i < 1:
        x = input("Enter a number: ").strip(" ").replace(" ","")
        if x == "":
            x = "[nothing entered]"
        number.append(x)
        i += 1

    story = (
        "I decided to go on a vacation during the summer break to Australia with " + propernoun[0] + 
        ". We got to the airport " + number[0] + " hours early. When we went through security, I got stopped because I forgot to take " +
        noun[0] + " out of my pocket. We got some " + noun[1] + " for the flight and arrived at the gate. Once we boarded the plane, I was sitting next to a very " +
        adj[0] + " man. He spent the entire flight " + verb[0] + " and talking about his job doing " + verb[1] +
        ". Whenever I tried to sleep, he would step around me to go to the " + noun[2] + 
        ". I was so " + verb[2] + ". Since I couldn't sleep, I decided to " + verb[3] + " and " + verb[4] +
        " instead. Finally, we arrived in Australia. All in all, the flight was " + adj[1] + "!"
    ).strip()

    print("\nYour Summer Vacation Mad Libs Story\n")
    print(story)

printmadlibs()