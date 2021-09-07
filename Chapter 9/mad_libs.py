import re

mad_text = open("madlibs.txt", 'r')
mad_libs = mad_text.read()
print(mad_libs)

adjective_regex = re.compile("ADJECTIVE")
noun_regex = re.compile("NOUN")
adverb_regex = re.compile("ADVERB")
verb_regex = re.compile("VERB")

while adjective_regex.search(mad_libs) is not None:
    adjective = input("Please enter an adjective:\n")
    mad_libs = adjective_regex.sub(adjective, mad_libs, 1)
while noun_regex.search(mad_libs) is not None:
    noun = input("Please enter a noun:\n")
    mad_libs = noun_regex.sub(noun, mad_libs, 1)
while adverb_regex.search(mad_libs) is not None:
    adverb = input("Please enter an adverb:\n")
    mad_libs = adverb_regex.sub(adverb, mad_libs, 1)
while verb_regex.search(mad_libs) is not None:
    verb = input("Please enter a verb:\n")
    mad_libs = verb_regex.sub(verb, mad_libs, 1)

new_text = open('new_madlibs.txt', 'w')
new_text.write(mad_libs)
new_text.close()
mad_text.close()
print(mad_libs)