import pandas as pd
import numpy as np

wordle_words = pd.read_csv('/Users/brianchen/PycharmProjects/WordleWordFinder22/Word lists in csv/five-letter-words.csv')
df = pd.DataFrame(wordle_words)

def main():
    print("Welcome to Wordle Word Finder!")
    print("------------------------------")
    GLetters = GoodLetters()
    BLetters = BadLetters()
    PLetters = PlacedLetters()
    result(GLetters, BLetters, PLetters)

def GoodLetters():
    GLetters = input("Good Letters: ")
    return GLetters

def BadLetters():
    BLetters = input("Bad Letters: ")
    return BLetters

def PlacedLetters():
    PLetters = input("Placed Letters: ")
    return PLetters

def result(gLetters, bLetters, pLetters):
    word = df['words'].str.contains(pLetters) #check if a dataframe contains pLetters
    print(word)

#5756rows
main()
