#  Winter break Python Mad libs 
# Create a short mad lib story about your winter break. 
# Your mad lib should include 6 input fields for users to enter data.
# Your mad lib program should prompt the user to enter 2 nouns, 2 verbs, and 2 adjectives. 
# Your mad lib should be written in complete sentences. 
# Once completed, submit your madlib to your github repository by using the source control tool in codespaces. 


def words():
    Noun1 = input("What is your first noun?")


    Verb1 = input("What is your first verb?")


    Adjective1 = input("What is your first adjective?")


    noun2 = input("What is your second noun?")


    verb2 = input("What is your second verb?")


    adjective2 = input("What is your second adjective?")

    story=(f"There was once a {Adjective1},zebra that everyone feared. Everywhere the zebra went everyone screamed that the,{adjective2},zebra was here to wreak havoc.The zebra decide to{Verb1} since nobody knew that she was just the evil zebra's twin sister.The,{Noun1},approached her and asked, why are destroying everything.The zebra then {verb2} at her to tell the world that she was the zebra's twin sister. Afterwards the {noun2} was nice to the zebra and they all lived in peace.")

print(story)