import random
import time

opp = ['Pain', 'Kisame', 'Deidara', 'Sasori', 'Hidan']


def opponent():
    opponent.n = random.choice(opp)


def intro():
    print('                 ##############################################')
    print('                 #                                            #')
    print('                 #     WELCOME TO THE WORLD OF NARUTO         #')
    print('                 #                                            #')
    print('                 ##############################################')
    time.sleep(2)
    print('\nA powerful fox(Kurama) known as the Nine-Tails attacks Konoha, the hidden leaf village in the Land of Fire,')
    time.sleep(1)
    print('one of the Five Great Shinobi Countries in the Ninja World. In response, the leader of Konoha and the ')
    time.sleep(1)
    print('Fourth Hokage, Minato Namikaze (with his wife Kushina Uzumaki) seals the fox inside the body of his ')
    time.sleep(1)
    print('newborn son, Naruto Uzumaki, making Naruto a host of the beast')
    time.sleep(2)
    print('\nAn organization called Akatsuki wants to destroy the village hidden in leaves.')
    time.sleep(1)
    print('and wants to capture the 9 tail fox to rule the world.')
    time.sleep(1)
    print('You have to protect the village Konoha by defeating the Akatsuki.')
    time.sleep(3)
    print('\nWould you like to play game (y or n): ')
    Answer = input('>>>').lower()

    if Answer == 'y':
        start_game()
    elif Answer == 'n':
        GameOver('----Not interested in playing game----')
    else:
        GameOver('--You don`t know how to type y or n--')


def start_game():
    opponent()
    time.sleep(1)
    print(opponent.n, 'one of the Akatsuki member attacked the village')
    time.sleep(2)
    print('Do you want to know more about', opponent.n, ':(y or n)')
    ans = input('>>>').lower()
    if ans == 'y':
        introQtns()
    elif ans == 'n':
        hero()
    else:
        print('Select properly y or n')
        start_game()


def hero():
    time.sleep(1)
    print('Select your Character to fight against', opponent.n, ' \n[ Naruto\t\tShikamaru\t\tSasuke\t\tRockLee ]\n')
    hero.select = input('>>>')
    if hero.select == 'Naruto':
        Naruto()
    elif hero.select == 'Shikamaru':
        Shikamaru()
    elif hero.select == 'Sasuke':
        Sasuke()
    elif hero.select == 'RockLee':
        RockLee()
    else:
        print('Select the Character mentioned in the list.')
        hero()
    time.sleep(5)
    askforFight()


def Naruto():
    print('______NARUTO-UZUMAKI________')
    print('Power level: 7\n')
    time.sleep(1)
    print('The main character of the game. He can create hundreds of shadow clones. Rasengan is one of his \n'
          'strongest attack. His next most powerful form is the use of the Nine-Tailed Cloak. By accessing \n'
          'the chakra of the nine-tailed fox named Kurama sealed inside him, Naruto can surround himself in a\n '
          'boiling aura of chakra that gives him beast-like abilities.\n')


def Sasuke():
    print('______SASUKE-UCHIHA________')
    print('Power level: 7\n')
    time.sleep(1)
    print('Sasuke has the Sharingan eyes.Abilities Genjutsu,chidori,fire ball justsu,with his sharingan eyes\n '
          'he can use susano,amaterasu(Black flame)\n')


def Shikamaru():
    print('______SHIKAMARU-NARA________')
    print('Power level: 5\n')
    time.sleep(1)
    print('The  genius of the Hidden Leaf Village.His main technique Shadow Possession Jutsu, an ability that\n '
          'allows him to control his opponent`s bodies by connecting his chakra to their shadow. Deriving from \n'
          'that are the Shadow Strangle Jutsu, which Shikamaru could use to physically grab his enemies once they\n '
          'were possessed\n')


def RockLee():
    print('______ROCK-LEE________')
    print('Power level: 6\n')
    time.sleep(1)
    print('Taijutsu user. abilities leaf Gale,strong fist,front lotus,drunken fist.\n'
          'Rock lee`s strongest attack is 8 inner gates he is capable of opening 5th inner gate(Gate of limit).\n')


def askforFight():
    time.sleep(1)
    print('Select one of the following option.\n'
          '1:Fight against ', opponent.n,
          '\n2:Train your character and then fight.')
    ans = input('>>>')
    if ans == '1':
        fightwithouttraining()
    elif ans == '2':
        trainingQtns()
    else:
        print('Select properly 1 or 2')
        askforFight()


def fightwithouttraining():
    time.sleep(2)
    if hero.select == 'Naruto':
        if opponent.n == 'Pain':
            print('----------oops! Pain defeated Naruto-----------------\n')
            GameOver1()
        elif opponent.n == 'Kisame':
            print('----------oops! Kisame defeated Naruto-----------------\n')
            GameOver1()
        elif opponent.n == 'Deidara':
            print('\n---------------Naruto defeated Deidara---------------\n')
            victory()
        elif opponent.n == 'Sasori':
            print('---------------Naruto defeated Sasori---------------\n')
            victory()
        elif opponent.n == 'Hidan':
            print('---------------Naruto defeated Hidan---------------\n')
            victory()

    elif hero.select == 'Sasuke':
        if opponent.n == 'Pain':
            print('----------oops! Pain defeated Sasuke-----------------\n')
            GameOver1()
        elif opponent.n == 'Kisame':
            print('----------oops! Kisame defeated Sasuke-----------------\n')
            GameOver1()
        elif opponent.n == 'Deidara':
            print('---------------Sasuke defeated Deidara---------------\n')
            victory()
        elif opponent.n == 'Sasori':
            print('---------------Sasuke defeated Sasori---------------\n')
            victory()
        elif opponent.n == 'Hidan':
            print('---------------Sasuke defeated Hidan---------------\n')
            victory()

    elif hero.select == 'Shikamaru':
        if opponent.n == 'Pain':
            print('Pain is far stronger than Shikamaro\n')
            GameOver('----------oops! Pain defeated Shikamaro-----------------\n')
        elif opponent.n == 'Kisame':
            print('Pain is far stronger than Shikamaro\n')
            GameOver('----------oops! Kisame defeated Shikamaro-----------------\n')
        elif opponent.n == 'Deidara':
            GameOver('----------oops! Deidara defeated Shikamaro-----------------\n')
        elif opponent.n == 'Sasori':
            print('----------oops! Sasori defeated Shikamaro-----------------\n')
            GameOver1()
        elif opponent.n == 'Hidan':
            print('----------oops! Hidan defeated Shikamaro-----------------\n')
            GameOver1()

    elif hero.select == 'RockLee':
        if opponent.n == 'Pain':
            print('Pain is far stronger than RockLee')
            GameOver('----------oops! Pain defeated RockLee-----------------\n')
        elif opponent.n == 'Kisame':
            print('----------oops! Kisame defeated RockLee-----------------\n')
            GameOver1()
        elif opponent.n == 'Deidara':
            print('----------oops! Deidara defeated RockLee-----------------\n')
            GameOver1()
        elif opponent.n == 'Sasori':
            print('---------------RockLee defeated Sasori---------------\n')
            victory()
        elif opponent.n == 'Hidan':
            print('---------------RockLee defeated Hidan---------------\n')
            victory()


def fightwithtraining():
    time.sleep(2)
    if hero.select == 'Naruto':
        print('\nAfter training under Jiraya sensei Naruto mastered the sage mode and Naruto`s power level:15\n')
        if opponent.n == 'Pain':
            print('---------------Naruto defeated Pain---------------\n')
            victory()
        elif opponent.n == 'Kisame':
            print('---------------Naruto defeated Kisame---------------\n')
            victory()
        elif opponent.n == 'Deidara':
            print('---------------Naruto defeated Deidara---------------\n')
            victory()
        elif opponent.n == 'Sasori':
            print('---------------Naruto defeated Sasori---------------\n')
            victory()
        elif opponent.n == 'Hidan':
            print('---------------Naruto defeated Hidan---------------\n')
            victory()

    elif hero.select == 'Sasuke':
        print('\nAfter training under Orochimaru Sasuke mastered the sage mode and Sasuke`s power level:15\n')
        if opponent.n == 'Pain':
            print('---------------Sasuke defeated Pain---------------\n')
            victory()
        elif opponent.n == 'Kisame':
            print('---------------Sasuke defeated Kisame---------------\n')
            victory()
        elif opponent.n == 'Deidara':
            print('---------------Sasuke defeated Deidara---------------\n')
            victory()
        elif opponent.n == 'Sasori':
            print('---------------Sasuke defeated Sasori---------------\n')
            victory()
        elif opponent.n == 'Hidan':
            print('---------------Sasuke defeated Hidan---------------\n')
            victory()

    elif hero.select == 'Shikamaru':
        print('\nAfter training under Asuma sensei Shikamaru`s power:7\n')
        if opponent.n == 'Pain':
            print('Pain is far stronger than Shikamaru')
            GameOver('----------oops! Pain defeated Shikamaru-----------------\n')
        elif opponent.n == 'Kisame':
            print('Kisame is far stronger than Shikamaru')
            GameOver('----------oops! Kisame defeated Shikamaru-----------------\n')
        elif opponent.n == 'Deidara':
            print('Deidara is stronger than Shikamaru')
            GameOver('----------oops! Deidara defeated Shikamaru-----------------\n')
        elif opponent.n == 'Sasori':
            print('---------------Shikamaru defeated Sasori---------------\n')
            victory()
        elif opponent.n == 'Hidan':
            print('---------------Shikamaru defeated Hidan---------------\n')
            victory()

    elif hero.select == 'RockLee':
        print('\nAfter taking Tai Jutsu training under Guy Sensei Rocklee`s power level: 9 ')
        if opponent.n == 'Pain':
            print('Pain is far stronger than RockLee')
            GameOver('----------oops! Pain defeated RockLee-----------------\n')
        elif opponent.n == 'Kisame':
            print('---------------RockLee defeated Kisame---------------\n')
            victory()
        elif opponent.n == 'Deidara':
            print('---------------RockLee defeated Deidara---------------\n')
            victory()
        elif opponent.n == 'Sasori':
            print('---------------RockLee defeated Sasori---------------\n')
            victory()
        elif opponent.n == 'Hidan':
            print('---------------RockLee defeated Hidan---------------\n')
            victory()


def GameOver(reason):
    time.sleep(.5)
    print('\n', reason, )
    time.sleep(.5)
    print('############################################')
    print('#                                          #')
    print('#          G A M E   O V E R               #')
    print('#                                          #')
    print('############################################')
    time.sleep(1)
    print('\n Would you like to play again(y or n)')
    ans = input('>>>')
    if ans == 'y':
        start_game()
    elif ans == 'n':
        print('---------Come Again---------')


def GameOver1():
    time.sleep(.5)
    print('############################################')
    print('#                                          #')
    print('#           Y O U  L O O S E               #')
    print('#                                          #')
    print('############################################')
    time.sleep(1)
    print('\n Would you like to train your character and then fight.(y or n)')
    ans = input('>>>')
    if ans == 'y':
        trainingQtns()
    elif ans == 'n':
        GameOver('Not interested in game.')
    else:
        print('Select properly (y or n)')
        GameOver1()


def victory():
    time.sleep(1)
    print('Congratulations you saved the Konoha village.')
    time.sleep(.5)
    print('############################################')
    print('#                                          #')
    print('#          Y O U    W I N                  #')
    print('#                                          #')
    print('############################################')
    time.sleep(1)
    print('\n Would you like to play again(y or n)')
    ans = input('>>>')
    if ans == 'y':
        start_game()
    elif ans == 'n':
        print('---------Come Again---------')


def AkatsukiInfo():
    time.sleep(3)
    if opponent.n == 'Pain':
        print('--------------------PAIN-------------------------------')
        time.sleep(1)
        print('----------------Difficulty level:10 -------------------')
        time.sleep(1)
        print('Abilities:Pain is from the village hidden in rain. he posses Rinnegan eyes which allows him to use \n'
              'wide variety of abilities. He can control gravity and is capable of using the Six Paths, which allow\n '
              'him to summon powerful animals, summon the God of Death, pull out people`s souls, turn his body \n'
              'cybernetic\n')
        time.sleep(1)
        print('HINT:--Pain Can be defeated only by the use of SAGE mode--\n')

    elif opponent.n == 'Kisame':
        print('--------------------KISAME--------------------')
        time.sleep(1)
        print('------------Difficulty level:8----------------')
        time.sleep(1)
        print('Abilities: Kisame is from the village hidden in mist.he holds the ability of shark. He is having a '
              'sword named "Samehada" which absorbs the energy of opponent constantly during the battle\n')
        time.sleep(1)
        print('Hint:-- Kisame can be defeated by the use of TAIJUTSU or Sage mode--\n')

    elif opponent.n == 'Deidara':
        print('--------------------DEIDARA---------------------------')
        time.sleep(1)
        print('----------------Difficulty level:7 -------------------')
        time.sleep(1)
        print('Abilities:Deidara is from the hidden stone village an explosives expert who specializes in widespread\n '
              'destruction. Combining earth and lighting elements to uses explosion techniques, Deidara uses the \n'
              'various mouths on his body  to turn ordinary clay into moving explosives he controls with his chakra.\n')

    elif opponent.n == 'Sasori':
        print('--------------------SASORI---------------------------')
        time.sleep(1)
        print('----------------Difficulty level:6 -------------------')
        time.sleep(1)
        print('Abilities:Sasori is from the hidden sand.The greatest puppet master.He can summon an army of upwards \n'
              'of a hundred puppets made from humans that all retain their abilities, as well as numerous hidden \n'
              'weapons.Sasori is also immune to all manner of poisons\n')

    elif opponent.n == 'Hidan':
        print('--------------------HIDAN-----------------------------')
        time.sleep(1)
        print('----------------Difficulty level:5 -------------------')
        time.sleep(1)
        print('Abilities:Hidan is from the village hidden in hot water. Hidan isn’t so much a powerful ninja,\n'
              'as he is a durable one. He really only has two tricks, his exceptional immortality and a technique\n'
              'that turns him into a voodoo doll that harms anyone who attacks him so long as he’s within a special\n'
              'symbol.\n')
        print('HINT:--As he is immortal you need good strategy to defeat him.')
    time.sleep(5)
    hero()


def introQtns():
    time.sleep(.5)
    a = 0
    print('\nYou need to Answer 3 Questions correctly out of 5 to get the details about:', opponent.n, '\n')
    time.sleep(2)

    print('1:Name of the organization that attacked the village is......')
    time.sleep(2)
    print('A:Akatsuki\nB:Momoshiki\nC:Uchiha')
    ans1 = input('>>>').upper()

    if ans1 == 'A':
        time.sleep(1)
        print('****Right Answer****')
        a = a + 1
    else:
        time.sleep(1)
        print('****Wrong Answer****')

    print('\n2:What is the name of the village.....')
    time.sleep(2)
    print('A:konago\nB:Konoha\nC:noha')
    ans2 = input('>>>').upper()
    if ans2 == 'B':
        time.sleep(1)
        print('****Right Answer****')
        a = a + 1
    else:
        time.sleep(1)
        print('****Wrong Answer****')

    print('\n3:Name of the 4th Hokage is.......')
    time.sleep(2)
    print('A:Itachi\nB:Minato\nC:Gara')
    ans3 = input('>>>').upper()
    if ans3 == 'B':
        time.sleep(1)
        print('****Right Answer****')
        a = a + 1
    else:
        time.sleep(1)
        print('****Wrong Answer****')

    print('\n4:Name of the 9 tail fox is.....')
    time.sleep(2)
    print('A:shukaku\nB:Gyuki\nC:Kurama')
    ans4 = input('>>>').upper()
    if ans4 == 'C':
        time.sleep(1)
        print('****Right Answer****')
        a = a + 1
    else:
        time.sleep(1)
        print('****Wrong Answer****')

    print('\n5:Name of Naruto`s mother is....')
    time.sleep(2)
    print('A:Kushina\nB:Ino\nC:Sakura')
    ans5 = input('>>>').upper()
    if ans4 == 'C':
        time.sleep(1)
        print('****Right Answer****')
        a = a + 1
    else:
        time.sleep(1)
        print('****Wrong Answer****')

    if a >= 3:
        AkatsukiInfo()
    else:
        time.sleep(1)
        print('Answered less than 3 questions correctly therefore no info about ', opponent.n)
        hero()


def trainingQtns():
    b = 0
    time.sleep(.6)
    print('You need to answer atleast 2 questions correctly out of 3.To train your character: ',hero.select)
    time.sleep(1)

    if opponent.n == 'Pain':
        print('1:Pain posses ...... eye`s.')
        time.sleep(2)
        print('A:Rinnegan\nB:Byakugan\nC:Sharingan')
        ans1 = input('>>>').upper()

        if ans1 == 'A':
            time.sleep(1)
            print('****Right Answer****')
            b = b + 1
        else:
            time.sleep(1)
            print('****Wrong Answer****')

        print('\n2:Pain can be defeated only by the.....')
        time.sleep(2)
        print('A:Amatirasu\nB:Sage mode\nC:Tai jutsu')
        ans2 = input('>>>').upper()
        if ans2 == 'B':
            time.sleep(1)
            print('****Right Answer****')
            b = b + 1
        else:
            time.sleep(1)
            print('****Wrong Answer****')

        print('\n3:Pain belongs to ..... village')
        time.sleep(2)
        print('A:hidden leaf\nB:hidden rain\nC:hidden mist')
        ans3 = input('>>>').upper()
        if ans3 == 'B':
            time.sleep(1)
            print('****Right Answer****')
            b = b + 1
        else:
            time.sleep(1)
            print('****Wrong Answer****')

        if b >= 2:
            time.sleep(1)
            print('Good you answered the questions correctly.')
            time.sleep(1)
            print(hero.select, ' is training hard to fight against ', opponent.n)
            fightwithtraining()
        else:
            time.sleep(1)
            print('Answered only 1 question correctly therefore no training for ', hero.select)
            fightwithouttraining()

    elif opponent.n == 'Kisame':
        print('1:Name of kisame`s sword is.....')
        time.sleep(2)
        print('A:Kubikiribōchō\nB:Kabutowari \nC:Samehada')
        ans1 = input('>>>').upper()

        if ans1 == 'C':
            time.sleep(1)
            print('****Right Answer****')
            b = b + 1
        else:
            time.sleep(1)
            print('****Wrong Answer****')

        print('\n2:Kisame belongs to ......village')
        time.sleep(2)
        print('A:hidden rain\nB:hidden mist\nC:hidden leaf')
        ans2 = input('>>>').upper()
        if ans2 == 'B':
            time.sleep(1)
            print('****Right Answer****')
            b = b + 1
        else:
            time.sleep(1)
            print('****Wrong Answer****')

        print('\n3:Kisame can be defeated by the......')
        time.sleep(2)
        print('A:Shadow clone jutsu\nB:Amatirasu\nC:Tai Jutsu')
        ans3 = input('>>>').upper()
        if ans3 == 'C':
            time.sleep(1)
            print('****Right Answer****')
            b = b + 1
        else:
            time.sleep(1)
            print('****Wrong Answer****')

        if b >= 2:
            time.sleep(1)
            print('Good you answered the questions correctly.')
            time.sleep(2)
            print(hero.select,' is training hard to fight against ',opponent.n)
            fightwithtraining()
        else:
            time.sleep(1)
            print('Answered only 1 question correctly therefore no training for ', hero.select)
            fightwithouttraining()

    elif opponent.n == 'Deidara':
        print('1:Deidara is an ........ expert')
        time.sleep(2)
        print('A:ninJutsu\nB:explosive\nC:art')
        ans1 = input('>>>').upper()

        if ans1 == 'B':
            time.sleep(1)
            print('****Right Answer****')
            b = b + 1
        else:
            time.sleep(1)
            print('****Wrong Answer****')

        print('\n2:Difficulty level of Deidara is...')
        time.sleep(2)
        print('A:5\nB:7\nC:6')
        ans2 = input('>>>').upper()
        if ans2 == 'B':
            time.sleep(1)
            print('****Right Answer****')
            b = b + 1
        else:
            time.sleep(1)
            print('****Wrong Answer****')

        print('\n3:Diedara is from .... village')
        time.sleep(2)
        print('A:hidden leaf\nB:hidden mist\nC:hidden stone')
        ans3 = input('>>>').upper()
        if ans3 == 'C':
            time.sleep(1)
            print('****Right Answer****')
            b = b + 1
        else:
            time.sleep(1)
            print('****Wrong Answer****')

        if b >= 2:
            time.sleep(1)
            print('Good you answered the questions correctly.')
            time.sleep(2)
            print(hero.select, ' is training hard to fight against ', opponent.n)
            fightwithtraining()
        else:
            time.sleep(1)
            print('Answered only 1 question correctly therefore no training for ', hero.select)
            fightwithouttraining()


    elif opponent.n == 'Sasori':
        print('1:Difficulty level of Sasori...')
        time.sleep(2)
        print('A:6\nB:8\nC:9')
        ans1 = input('>>>').upper()

        if ans1 == 'A':
            time.sleep(1)
            print('****Right Answer****')
            b = b + 1
        else:
            time.sleep(1)
            print('****Wrong Answer****')

        print('\n2:Sasori is from ....village ')
        time.sleep(2)
        print('A:hiden mist\nB:hiden stone\nC:hidden sand')
        ans2 = input('>>>').upper()
        if ans2 == 'C':
            time.sleep(1)
            print('****Right Answer****')
            b = b + 1
        else:
            time.sleep(1)
            print('****Wrong Answer****')

        print('\n3:Sasori is a ....... master')
        time.sleep(2)
        print('A:explosive\nB:puppet\nC:poison')
        ans3 = input('>>>').upper()
        if ans3 == 'B':
            time.sleep(1)
            print('****Right Answer****')
            b = b + 1
        else:
            time.sleep(1)
            print('****Wrong Answer****')

        if b >= 2:
            time.sleep(1)
            print('Good you answered the questions correctly.')
            time.sleep(2)
            print(hero.select, ' is training hard to fight against ', opponent.n)
            fightwithtraining()
        else:
            time.sleep(1)
            print('Answered only 1 question correctly therefore no training for ', hero.select)
            fightwithouttraining()

    elif opponent.n == 'Hidan':
        print('1:Difficulty level of hidan is...')
        time.sleep(2)
        print('A:4\nB:5\nC:8')
        ans1 = input('>>>').upper()

        if ans1 == 'B':
            time.sleep(1)
            print('****Right Answer****')
            b = b + 1
        else:
            time.sleep(1)
            print('****Wrong Answer****')

        print('\n2:Hidan is from village hidden in ....')
        time.sleep(2)
        print('A:sand\nB:mist\nC:hot water')
        ans2 = input('>>>').upper()
        if ans2 == 'C':
            time.sleep(1)
            print('****Right Answer****')
            b = b + 1
        else:
            time.sleep(1)
            print('****Wrong Answer****')

        print('\n3:Hidan is ......')
        time.sleep(2)
        print('A:Strongest\nB:Immortal\nC:Mortal')
        ans3 = input('>>>').upper()
        if ans3 == 'B':
            time.sleep(1)
            print('****Right Answer****')
            b = b + 1
        else:
            time.sleep(1)
            print('****Wrong Answer****')

        if b >= 2:
            time.sleep(1)
            print('Good you answered the questions correctly.')
            time.sleep(2)
            print(hero.select, ' is training hard to fight against ', opponent.n,'\n')
            fightwithtraining()
        else:
            time.sleep(1)
            print('Answered only 1 question correctly therefore no training for ', hero.select)
            fightwithouttraining()
intro()