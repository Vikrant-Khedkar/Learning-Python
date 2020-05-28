def pig_latin(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        word= word+'ay'
        print(word)
    else:
        x = word[0]
        word = word[1::1]
        word = word + x +'ay'
        print(word)
s= input("Enter a word:\t")
pig_latin(s)
input("Bye!")    