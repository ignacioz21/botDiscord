import discord
from wordsHangman import words
import random
from discord.ext import commands


async def hangman(ctx):
    hangmanWord = random.choice(words)
    lenghtHangmanWord = len(hangmanWord)
    (hangmanWord)
    lettersHangman = list(hangmanWord)
    print(lettersHangman)
    underscores = "_" * lenghtHangmanWord
    underscoresList = list(underscores)
    print(underscores)
    on = True
    intents = random.randint(3, 8)


    while on:
        await ctx.send('Tienes', intents, 'intentos')
        letterInputUser = input("Introduce una letra\n")

        if letterInputUser in hangmanWord:
            for index, letter in enumerate(hangmanWord):
                if letter == letterInputUser:
                    underscoresList[index] = ''.join(letterInputUser)

            underscores = ''.join(underscoresList)
            await ctx.send(underscores)
        else:
            intents -= 1
        
        if intents == 0:
            on = False
            await ctx.send('Game over')
        else:
            pass
        if underscores == hangmanWord:
            await ctx.send('HAZ GANADO!!!')
            on = False
        else:
            pass