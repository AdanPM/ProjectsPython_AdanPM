 
print("¿Buscas letras de canciones icónicas? Estás en el lugar correcto")
bandera=1
while bandera==1:
    artista=int(input("\nLista de artistas\n1. Beyoncé\n2. Sia\n3. Rihanna\nElige artisa: "))
    if artista==1:
        print("\nBuena elección, Queen B! ¿Qué canción eliges?")
        cancion=int(input("1. Halo \n2. Love on top \n3. Listen\nElige opcion: "))
        if cancion==1:
            print("Everywhere I'm looking now\nI'm surrounded by your embrace\nBaby, I can see your halo\nYou know you're my saving grace")
            print("You're everything I need and more\nIt's written all over your face\nBaby, I can feel your halo\nPray it won't fade away")
        elif cancion==2:
            print("Baby, it's you\nYou're the one I love\nYou're the one I need\nYou're the only one I see")
            print("Come on, baby, it's you\nYou're the one that gives your all\nYou're the one that gives your all\nYou're the one I can always call")
            print("When I need, you make everything stop\nFinally, you put my love on top")
        elif cancion==3:
            print("Listen, I am alone at a crossroads\nI'm not at home in my own home\nAnd I've tried and tried to say what's on my mind\nYou should have known")
            print("Oh, now I'm done believing you\nYou don't know what I'm feeling\nI'm more than what you made of me\nI followed the voice you gave to me\nBut now I've gotta find my own")
        bandera=int(input("\nMúsica para mis oídos\n¿Quieres otra canción?\n1. Si!\n2. No, gracias"))
    elif artista==2:
        print("\nBuena elección! Sia! ¿Qué canción eliges?")
        cancion=int(input("1. Chandelier \n2. Cheap Thrills\n3. Titanium\nElige opcion: "))
        if cancion==1:
            print("I'm gonna swing from the chandelier\nFrom the chandelier\nI'm gonna live like tomorrow doesn't exist\nLike it doesn't exist")
            print("I'm gonna fly like a bird through the night\nFeel my tears as they dry\nI'm gonna swing from the chandelier\nFrom the chandelier")
        elif cancion==2:
            print(" Baby, I don't need dollar bills to have fun tonight\n(I love cheap thrills)\nBaby, I don't need dollar bills to have fun tonight\n(I love cheap thrills)")
            print("But I don't need no money\nAs long as I can feel the beat\nI don't need no money\nAs long as I keep dancing")
        elif cancion==3:
            print("I'm bulletproof, nothing to lose\nFire away, fire away\nRicochet, you take your aim\nFire away, fire away")
            print("You shoot me down, but I won't fall\nI am titanium\nYou shoot me down, but I won't fall\nI am titanium")
        bandera=int(input("\nMúsica para mis oídos\n¿Quieres otra canción?\n1. Si!\n2. No, gracias"))
    elif artista==3:
        print("Buena elección! Ri - Ri, Rihanna ¿Qué canción eliges?")
        cancion=int(input("1. S&M \n2. Umbrella \n3. Stay \nElige opcion: "))
        if cancion==1:
            print("Love is great, love is fine (oh, oh, oh, oh, oh)\nOut the box, outta line (oh, oh, oh, oh, oh)\nThe affliction of the feeling leaves me wanting more\n(Oh, oh, oh, oh, oh, oh)")
            print("'Cause I may be bad, but I'm perfectly good at it\nSex in the air, I don't care, I love the smell of it\nSticks and stones may break my bones\nBut chains and whips excite me")
        elif cancion==2:
            print("When the sun shines, we'll shine together\nTold you I'll be here forever\nSaid I'll always be your friend\nTook an oath, I'ma stick it out to the end")
            print("Now that it's raining more than ever\nKnow that we'll still have each other\nYou can stand under my umbrella\nYou can stand under my umbrella, ella, ella, eh, eh, eh")
        elif cancion==3:
            print("Not really sure how to feel about it\nSomething in the way you move\nMakes me feel like I can't live without you\nIt takes me all the way")
            print("I want you to stay\nIt's not much of a life you're living\nIt's not just something you take, it's given")
        bandera=int(input("\nMúsica para mis oídos\n¿Quieres otra canción?\n1. Si!\n2. No, gracias"))
print("Gracias, vuelve pronto")