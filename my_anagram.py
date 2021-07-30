def anagram(text1, text2):
    text1 = text1.strip().replace(" ", "").lower()
    text2 = text2.strip().replace(" ", "").lower()

    if text1 == "" or text2 == "":
        print("Not anagrams")
    elif sorted(text1) == sorted(text2):
        print("Anagrams")
    else:
        print("Not anagrams")


anagram("Listen", "Silent")
anagram("modern", "norman")
anagram("", "")
anagram(" ", " ")
