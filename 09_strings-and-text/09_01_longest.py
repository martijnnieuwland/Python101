# Which of the following strings is the longest?
# Use the len() function to find out.


words = dict(
    longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle",
    longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért",
    longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas",
    strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"
)

for word, val in words.items():
    print(word, len(val))
    
longest = max(words.values(), key=len)
word = [word for word in words if words[word]==longest]
print(f'The longest string is "{word[0]}"')