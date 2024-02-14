# A Journey Through - Simulated Existence, or Not?
# Explore the Order of the Elementis to find out!

# Import necessary py-modules and libraries:

import random
import ddbCall

names = ['Emily']
def processName(name):
    if name in names:
        return "Welcome Emily thank chwod you have arrived.  Nick has been kidnapped and we need your help to free him! You must answer all these chwestions correctly to save Nick.  You have been given 3 hearts to complete the game. If you lose them all then Nick dies.  Your Chwackpack currently contains 3 items.  Collect all 5 to save his life! Say Begin to start."
        #return "Shortened for testing.  Say Begin"
    else :
        return "Hmm this game is not for you..."

win_msg = 'That is correct, your reward is Scarlett.  Congratulations you have answered all the questions correctly and recovered all the plush animals.  Nick has been saved from the mormons, hooray!  Love prevails and you win.  Happy Valentines Day!'
lose_msg = 'Oh No, That was your last heart.  You lose and the mormons enslave Nick making him churn butter for all eternity.  Better luck next time, Goodbye!'
elementis_dict = {
                        'q1' : {
                            'name' : 'q1',
                            'question' : 'On your first date at Flacos Tacos where Emily blacked out, what did Nick order?',
                                    'answers' : {1 : 'Carne asada tacos',
                                                2 : 'Chicken tinga tacos',
                                                3 : 'Carne asada Burrito',
                                                4 : 'Chicken Tinga Burrito'},
                                    'correct answer': '3',
                                    'reward' : 'Bernardo'},
                        'q2' : {
                            'name' : 'q2',
                            'question' : 'Durning an early date Nick and Emily went to a drive in movie to see the Blues Brothers.  What are the names of the two main characters?',
                                    'answers' : {1 : 'Elroy and Jeffrey',
                                                2 : 'Jake and Elwood',
                                                3 : 'Elmer and John',
                                                4 : 'Jim and Eric'},
                                    'correct answer' : '2',
                                    'reward' : 'Maritza'},
                        'q3' : {
                            'name' : 'q3',
                            'question' : 'What was the name of the lovely Wisconsin campground where Emily camped for the first time?',
                            'answers' : {
                                        1 : 'Devils Lake',
                                        2 : 'Lake Delvan',
                                        3 : 'Plymouth Rock',
                                        4 : 'Lost Bikini Valley'
                            },
                            'correct answer' : '1',
                            'reward' : 'Judy'},
                        'q4' : {
                            'name' : 'q4',
                            'question' : 'Before you started dating Nick was abroad.  What was the neighborhood in Hong Kong where he lived?',
                            'answers' : {
                                        1 : 'Kowloon',
                                        2 : 'Wan Chai',
                                        3 : 'Mong Kok',
                                        4 : 'Sai Ying Pun'
                                
                            },
                            'correct answer' : '4',
                            'reward' : 'Pineapple Jellycat'},
                        'q5' : {
                            'name' : 'q5',
                            'question' : 'Nick and Emily have celebrated many special nights.  Which event featured a shotstopus?',
                            'answers' : {
                                        1 : 'Nicks 23rd Birthday',
                                        2 : 'One Year anniversary',
                                        3 : 'Valentines day 2022',
                                        4 : 'Two Year anniversary'
                            },
                            'correct answer' : '2',
                            'reward' : 'Scarlett'}
                    }

def getNextQuestion(session):
    sessionInfo = ddbCall.getSessionInfo(session)
    if not sessionInfo['q1']['BOOL']:
        question = 'q1'
    elif not sessionInfo['q2']['BOOL']:
        question = 'q2'
    elif not sessionInfo['q3']['BOOL']:
        question = 'q3'
    elif not sessionInfo['q4']['BOOL']:
        question = 'q4'
    elif not sessionInfo['q5']['BOOL']:
        question = 'q5'
    else:
        question = 'Win'
    
    return question


def askNextQuestion(session):
    question = getNextQuestion(session)
    if question != 'Win':
        message = elementis_dict[question]['question']
        answers = elementis_dict[question]['answers']
        return message + "Your options are, 1 " + answers[1] + " , 2 " + answers[2] + " , 3 " + answers[3] + " ,  or 4 " + answers[4]
    else:
        return win_msg

def checkAnswer(session, answer):
    question = getNextQuestion(session)
    correctAnswer = elementis_dict[question]['correct answer']
    if str(answer) == str(correctAnswer):
        reward = elementis_dict[question]['reward']
        ddbCall.updateQuestion(session, question)
        if question == 'q5':
            return [True, win_msg]
        else:
            return [False,'That is correct, you get a new reward in your Chwackpack! ' + reward + ' . Say Next Question to continue.']
    else:
        correct = False
        resp = ddbCall.loseLife(session)
        if resp == 'Game Over':
            return [True, lose_msg]
        else:
            return [False, 'Sorry that was not the correct answer, you lost a heart.  You have ' + str(resp) + ' hearts remaining']
        

'''
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
            print(
            --> That is not the correct answer.
                You now have {lives} hearts remaining.format(lives = self.life))
        else:
            print(
            --> That was your last heart.  You lose and the mormons kill Nick.
                Better luck next time, Bye!)

        
    def win_game(player):
        print(
        --> Congratulations you have answered all the questions correctly and recovered all the plush animals.
            Nick has been saved from the mormons.  Your reward is a 15 minute soak, hooray!  Love prevails and you win)
        quit()

    def ask_question(self, elementis):
        print ('--> {question}'.format(question = elementis.question))
        print(
        -->> 1) {answer_1}
        -->> 2) {answer_2}
        -->> 3) {answer_3}
        -->> 4) {answer_4}
        .format(answer_1 = elementis.answers[1],
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
        if next_elementis == 'q1':
            return q1
        elif next_elementis == 'q2':
            return q2
        elif next_elementis == 'q3':
            return q3
        elif next_elementis == 'q4':
            return q4
        elif next_elementis == 'q5':
            return q5
        
'''

# Base code for dict quick create template - copy and paste.
base_code = {'name' : '', 'question' : '', 'answers' : {1 : '', 2 : '', 3 : '', 4 : ''}, 'correct answer' : '', 'reward' : ''}
