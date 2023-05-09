# Task 3 - Hero Story
"""
Your going to write a story, cut it into section, store the section in a python dictionary!

Tasks:
- Define a dictionary
- Add your content as values for keys
- Follow the instruction in the pseudocode below:

Acceptance Criteria:
- All 7 tasks are done
- Runs with no errors
"""

# 1 - Define a dictionary call story1, it should have the following keys: "start", "middle" and "end"
story1 = {
    "start": "There was once a young boy named Bradley was once stung by a scorpion, it gave him superpowers: the "
             "ability to sting from a stinger which grew from his body.",
    "middle": "The boy grew up to be a hero called ScorpioBrad, using his sting he was able to fight crime. One day, "
              "an evil villain named The Bat, flew into town and terrorised the people of the town.",
    "end": "Initiating a battle against his archenemy, The Bat, he was able to fight his way and inflict a sting so strong it "
           "knocked The Bat out, and was able to save thousands of people."
}

# 2 - Print the entire dictionary
print("2 - Print the entire dictionary")
print(story1)

# 3 - Print the type of your dictionary
print("\n3 - Print the type of your dictionary")
print(type(story1))

# 4 - Print only the keys
print("\n4 - Print only the keys")
print(story1.keys())

# 5 - Print only the values
print("\n5 - Print only the values")
print(story1.values())

# 6 - Print the individual values using the keys (individually, lots of print commands)
print("\n6 - Print the individual values using the keys")
print(story1["start"])
print(story1["middle"])
print(story1["end"])

# 7 - Now let's add a new key:value pair: "hero": "yourSuperHero"
print("\n7 - Now let's add a new key:value pair: \"hero\": \"yourSuperHero\"")
story1["hero"] = "ScorpioBrad"
print(story1)
