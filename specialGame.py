# A Journey Through - Simulated Existence, or Not?
# Explore the Order of the Elementis to find out!

# Import necessary py-modules and libraries:

import random

def programme_start():
    player_name = ''
    player_name = input ('--> Hello and welcome to a very special secret game.  What is your name? ')
    while player_name.lower() != 'emily':
        player_name = input ('--> Hmm this game is not for you, try again. What is your name? ')
    else:
        return player_name.title()

# Create class for Player in game:

class Player:
    
    def __init__(self, name):
        self.player = 'Player 1'
        self.name = name
        self.life = 3
        self.item_container = []
        
    def __repr__(self):
        return ('''
        --> Welcome {name} thank chwod you have arrived.  Nick has been kidnapped by mormons and we need your help to free him!
            The mormons don't believe in monogomous love.  You must answer all these chwestions correctly to save Nick.
            You have been given {life} hearts to complete the game. If you lose them all then Nick chwies.
            Your Chwackpack currently contains {number} items.  Collect them all to save his life!
        '''.format(name = self.name, life = self.life, number = len(self.item_container)))

    def get_reward(self, elementis):
        print('--> Your reward for this is {reward}'.format(reward = elementis.reward))
        player_1.item_container.append(elementis.reward)
        print('--> Your item container now holds {items}.'.format(items = player_1.item_container))
        if len(self.item_container) == 5:
            Game.win_game(self)

    def store_reward(self, elementis_reward):
        self.items.append(elementis_reward)

    def lose_a_life(self):
        self.life -= 1
        if self.life > 0:
            print('''
            --> That is not the correct answer.
                You now have {lives} hearts remaining.'''.format(lives = self.life))
        else:
            print('''
            --> That was your last heart.  You lose and the mormons kill Nick.
                Better luck next time, Bye!''')

# Create class for Elementis:
class Elementis:
    
    def __init__(self, elementis):
        self.name = elementis_dict[elementis]['name']
        self.question = elementis_dict[elementis]['question']
        self.answers = elementis_dict[elementis]['answers']
        self.correct_answer = elementis_dict[elementis]['correct answer']
        self.reward = elementis_dict[elementis]['reward']
    
    def __repr__(self):
        return ('--> This Elementis is the {name}.'.format(name = str(self.name)))

# Create class for Game - will contain main bulk of code:

class Game:
    
    def __init__(self, player):
        self.game_elementis_list = ['cosmos', 'flame', 'aqua', 'mystic', 'chaos']
        self.correctly_answered = []
        print(player)
        Game.game_init(self, player)

    def __repr__(self):
        pass

    def game_init(self, player):
        print('--> Are you ready to begin?')
        y_n = input ('--> Type Y/N and press enter: ')
        while y_n.lower() != 'y' and y_n.lower() != 'n':
             y_n = input ('--> Type Y/N and press enter: ')
        if y_n.lower() == 'n':
            print ('--> Okay Nick will go die then, bye.')
            quit()
        else:
            Game.ask_question(self, chaos)
        
    def win_game(player):
        print('''
        --> Congratulations you have answered all the questions correctly and recovered all the plush animals.
            Nick has been saved from the mormons.  Hooray your reward is a 15 minute soak.  Love prevails and you win!''')
        quit()

    def ask_question(self, elementis):
        print ('--> {question}'.format(question = elementis.question))
        print('''
        -->> 1) {answer_1}
        -->> 2) {answer_2}
        -->> 3) {answer_3}
        -->> 4) {answer_4}
        '''.format(answer_1 = elementis.answers[1],
                   answer_2 = elementis.answers[2],
                   answer_3 = elementis.answers[3],
                   answer_4 = elementis.answers[4]))
        answer = input ('--> Choose a number and press enter: ')
        while answer == '':
            answer = input ('--> Choose a number and press enter: ')
        if answer == elementis.correct_answer:
            Game.correct_answer(self, elementis)
        else:
            Game.wrong_answer(self, elementis)

    def correct_answer(self, elementis):
        print('--> Well done! You have chosen the correct answer!')
        player_1.get_reward(elementis)
        self.correctly_answered.append(elementis.name)
        self.game_elementis_list.remove(elementis.name.lower())
        next_elementis = Game.elementis_rand_select(self)
        Game.ask_question(self, next_elementis)

    def wrong_answer(self, elementis):
        print('--> Oh no! You have chosen the wrong answer!')
        player_1.lose_a_life()
        next_elementis = elementis
        Game.ask_question(self, next_elementis)

    def elementis_rand_select(self):
        next_elementis = random.choice(self.game_elementis_list)
        if next_elementis == 'cosmos':
            return cosmos
        elif next_elementis == 'flame':
            return flame
        elif next_elementis == 'aqua':
            return aqua
        elif next_elementis == 'mystic':
            return mystic
        elif next_elementis == 'chaos':
            return chaos
        

#Creat dict of Elementis for object inits:

elementis_dict = {
                        'cosmos' : {
                            'name' : 'Cosmos',
                            'question' : 'Using modern sciences, is it possible to quantify the Cosmos completely?',
                                    'answers' : {1 : 'Yes, with the right instruments',
                                                2 : 'Only partially',
                                                3 : 'Impossible to quantify limitless',
                                                4 : 'No, but one day'},
                                    'correct answer': '3',
                                    'reward' : 'Bernardo'},
                        'flame' : {
                            'name' : 'Flame',
                            'question' : 'Can one find the source of the Healing Flame?',
                                    'answers' : {1 : 'Yes, by exploring the cosmos',
                                                2 : 'It is not found, but achieved',
                                                3 : 'No',
                                                4 : 'Yes, can be created by craftsman'},
                                    'correct answer' : '2',
                                    'reward' : 'Maritza'},
                        'aqua' : {
                            'name' : 'Aqua',
                            'question' : 'In the Waters of Forever, how does one survive?',
                                    'answers' : {1 : 'No survival, you will become one with it',
                                                2 : 'Learn to breathe inside',
                                                3 : 'Drink it all',
                                                4 : 'Hold your breath'},
                                    'correct answer' : '1',
                                    'reward' : 'Judy'},
                        'mystic' : {
                            'name' : 'Mystic',
                            'question' : 'In the Arcane, is there any limitation true?',
                                    'answers' : {1 : 'Yes, the Rule of Law',
                                                2 : 'No, not according to the rules in place',
                                                3 : 'Yes, spells contained in spellbooks',
                                                4 : 'One can never be restricted if one\'s mind is endless'},
                                    'correct answer' : '4',
                                    'reward' : 'Pineapple Jellycat'},
                        'chaos' : {
                            'name' : 'Chaos',
                            'question' : 'Was there ever truly order in the Expanse?',
                                    'answers' : {1 : 'Yes, all things have order',
                                                2 : 'No, the ever changing cannot be ordered',
                                                3 : 'No, we just believe there is',
                                                4 : 'Yes, but only in the beginning'},
                                    'correct answer' : '2',
                                    'reward' : 'Scarlett'}
                    }
# Base code for dict quick create template - copy and paste.
base_code = {'name' : '', 'question' : '', 'answers' : {1 : '', 2 : '', 3 : '', 4 : ''}, 'correct answer' : '', 'reward' : ''}

# Initiate Elementis and create list - initiate new and add as necessary (if needed):

cosmos = Elementis('cosmos')
flame = Elementis('flame')
aqua = Elementis('aqua')
mystic = Elementis('mystic')
chaos = Elementis('chaos')
elementis_list = [cosmos, flame, aqua, mystic, chaos]


# Object instance creation to run terminal game:

name_start = programme_start()
player_1 = Player(name_start)
new_game = Game(player_1)

