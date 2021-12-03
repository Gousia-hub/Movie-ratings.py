name = input("Your name pls: ").strip().capitalize()
print("Welcome to our brand new Entertainment Center COOLSTAR , {} !".format(name))
print("we have a variety of  movie collections")
movies = {"English":["Harry Potter And The Order Of The Phoneix , Lie , Joker, Onward"] , 
          "Telugu":["V , Rrr ,Nishabdham , Eega" ], 
          "Hindi":["Street Dancer 3, Lootcase , Shakuntala Devi , Bhoot Part One"]}

status = {"Harry Potter And The Order Of The Phoneix":[98.9],"Lie":[77.3],"Joker":[98.85],
               "Onward":[90.6],"V":[82.2],"Rrr":[97.9],"Eega":[96.8],"Nishabdham":[79.7],
               "Street Dancer 3":[91.8],"Lootcase ":[93.5],"Shakuntala Devi":[90.0],
               "Bhoot Part One":[88.8]}
while True:
    lang = input("enter your language: ").strip().title()
    
    if lang in movies :
       mov_ava = str(movies[lang][0:3])
       print("movies available are:" + mov_ava)
    else:
        print("Error")
        break 
    rats = input("movie name to know the ratings?: ").strip().title()  
    if rats in status:
        print(status[rats])
        print("Enjoy your movie , Thanks for connecting with COOLSTAR")
        
    else:
        print("wrong input!")
        

    
