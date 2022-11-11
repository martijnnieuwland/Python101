# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

opinion = input("What's your opinion? ")
reply = ""

for c in opinion:
    if opinion.index(c) % 2 == 0:
        reply += c.upper()
    else:
        reply += c
        
print(reply)
