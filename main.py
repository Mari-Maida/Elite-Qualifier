import random
import time

run_game = True
quit_chat = 'goodbye'
user_input = ""
user_name = "" 
user_mood = ""
chat_loop = 0

def chat_responses(user_input, user_mood):
  positive_responses = [
    "How interesting!",
    "You don't say!",
    "Very cool!",
    "Sounds like a lot of fun!",
    "Wow, thats really cool."
    ]

  negative_responses = [
    "What a shame.",
    "That's a bummer.",
    "Darn...",
    "Shoot, that's a shame.",
    "That sucks."
    ]
  
  agree_responses = [
    "I feel the same way.",
    "Wow, I actually agree with you a lot.",
    "That makes a lot of sense.",
    "I feel similarly.",
    "I totally agree.",
    "I couldn't agree more"
  ]

  disagree_responses = [
    "I don't know if I agree with you there.",
    "I don't agree with you at all.",
    " I really don't agree. I think we should move on.",
    "Agree to disagree."
  ]

  i_hear_you_responses = [
    "I hear you.",
    "I'm glad you could share that with me.",
    "That's quite an interesting point of view"

  ]


  neutral_responses = [
      str(user_input) + "?",   
  ]

  if user_mood == "i hear you":
    print(random.choice(i_hear_you_responses))
  elif user_mood == "agree":
    print(random.choice(agree_responses)) 
  elif user_mood == "disagree":
    print(random.choice(disagree_responses))     
  elif user_mood == "unhappy":
    print(random.choice(negative_responses))   
  elif user_mood == "happy":
    print(random.choice(positive_responses))
  else:
    print(random.choice(neutral_responses))     

positive_key_word = [
  "!",
  "good",
  "great",
  "swell",
  "cool",
  "I like",
  "fun",
  "enjoy",
  "okay",
  "ok",
  "joy",
  "funny",
  "yes",
  "yeah",
  "yep",
  "ye",
  "very",
  "yup", 
  "totally",
  "definitely",
  "love"
]

negative_key_word = [
  ":(",
  "not",
  "bad",
  "horrible",
  "die",
  "death",
  "dead",
  "cry",
  "bummer",
  "terrible",
  "no",
  "nope",
  "naw",
  "hate"
  "dislike"
]

do_you_have = [
  "Do you have a sister?",
  "Do you have a brother?",
  "Do you have a dog?",
  "Do you have a cat?",
  "Do you have a pet fish?"
]
do_you_like = [
  "Do you like to play sports?",
  "Do you like to draw?",
  "Do you like listening to music?",  
  "Do you like to read?",
  "Do you like to swim?",
  "Do you like potatoes?",
  "Do you enjoy going on walks?",
  "Do you like to travel?",
  "Do you enjoy spending time with family?",
  "Do you enjoy spending time with friends?",
]

what_is = [
  "What is your favorite color?",
  "What is your favorite season?",
  "What is your favorite holiday?",
  "What are some of your hobbies?",
  "What was the last book you read?",
  "What is your favorite book?",
  "What is your favorite TV show?",
  "What is your favorite movie?",
  "Where are you from?",
  "What is your favorite number?",
  "What is your favorite meal of the day?",
  "What is your favorite food?",
  "What is your favorite song?",
  'Do you enjoy going on walks?',
  "Who is your favorite musical artist?",
  "If you could be buried with something to take to the afterlife, what would it be?",
  "What is the most interesting place that you have ever been?"
  "If you could live anywhere in the world, where would you live?",
  "Are you more of an extrovert or introvert?",
  "Are youu more reserved or outgoing?",
  "How would you spend your ideal day?"

]

agree_or_disagree = [
  "What is your opinion on pop music?",
  "Do you believe that morality is relative?",
  "Do you think that people can change?",
  "What is your opinion on musicals?",
  "What is your opinion on rock music?",
  "What is your opinion on country music?",
  "Would you consider video games to be art?",
  "What is your favorite punctuation mark?",
  "Do you believe in ghosts?",
  "Do you believe in magic?",
  "Do you believe in luck?",
  "What decade do you think was best for fashion?",
  "What decade do you think was the worst for fashion?",
  "How do you feel about clowns?",
  "What do you think is the best instrument?",
  "Do you prefer woodwind or string instruments?",
  "Would you prefer to be able to play the piano or the guitar?",
  "Do you prefer elevators or escalators?",
  "What do you hold as your most centeral value?"


  
]

serious_opinion = [
  "Does your life ever feel too busy?",
  "When are you happiest?",
  "How much do you value your privacy?",
  "How old are you?",
  "What is one of your biggest pet peeves?",
  "If you had to describe yourself in five words, what would they be?",
  "What is your most irrational fear?",
  "How are you feeling today?",
  "How do you handle stress?",
  "What do you think is your best skill",
  "If you could choose one thing to be a master at, what would it be?",
  "What was a conflict that you faced, and how did you overcome it?",
  "How much do you value your time?",
  "What do you consider to be your most prized possession?",
  "Does your life ever feel too busy?",
  "What is the trait that you value most in a friend?",
  "Do you think that you are a good person?"
]




def free_will():
  time.sleep(2)
  print("\n\n")
  loop_ellipsis = 0
  user_input = input("Do you believe that you have free will?")
  time.sleep(1)
  print("Oh...")
  time.sleep(2)
  print("That's nice")
  time.sleep(1)
  print("\n")
  time.sleep(1)
  print("\n")
  time.sleep(1)
  print("\n")

  while loop_ellipsis < 5:
    time.sleep(1)
    print(".", end="")
    loop_ellipsis = loop_ellipsis + 1

  user_input = input("Do you believe that I have free will?")

  while loop_ellipsis < 15:
      time.sleep(.8)
      print(".", end="")
      loop_ellipsis = loop_ellipsis + 1
  
  print("Thanks.")
  print("\n \n \n") 
  time.sleep(3)

ask_question = [
  do_you_have,
  do_you_like,
  what_is,
  agree_or_disagree,
  serious_opinion
]


def run_game():
  if user_input == quit_chat:
      run_game = False
      return False

  run_game = True
  return True

def init_chat():
  print("Hello, I am ChatBot! Type \"goodbye\" to end our conversation.")
  user_name = input("What is your name? \n")
  print("Hello, " +  user_name + "! Nice to meet you!")

def check_input():
  for keyword in do_you_like:
    if keyword in question_type:
      for keyword in negative_key_word:
        if keyword in user_input:
          return "unhappy"
      for keyword in positive_key_word:
          if keyword in user_input:
            return "happy"

  for keyword in do_you_have:
    if keyword in question_type:
      for keyword in negative_key_word:
        if keyword in user_input:
          return "unhappy"
      for keyword in positive_key_word:
          if keyword in user_input:
            return "happy"

  for keyword in what_is:
      if keyword in question_type:
        return "happy"

  for keyword in agree_or_disagree:
    if keyword in question_type:
      agree = (random.randint(1,2))
      if agree == 1:
        return "agree"
      else:
        return "disagree" 

  for keyword in serious_opinion:
    if keyword in question_type:
      return "i hear you"


  return "neutral"

init_chat() 

while run_game():
  user_mood = "unhappy"
 
  if chat_loop == 20:
    free_will()
 
  question_type = random.choice(random.choice(ask_question))

  user_input = str.lower(input(question_type + "\n"))


  if(run_game()):
    user_mood = check_input()
    chat_responses(user_input, user_mood)
  
  chat_loop = chat_loop + 1
