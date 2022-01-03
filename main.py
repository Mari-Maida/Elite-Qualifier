import random

run_game = True
quit_chat = 'goodbye'
user_input = ""
user_name = "" 
user_mood = ""


def chat_responses(user_input, user_mood):
  positive_responses = [
    "How interesting!",
    "You don't say!",
    "Very cool!",
    "Sounds like a lot of fun!",
    "Wow, thats really cool"
    ]

  negative_responses = [
    "What a shame",
    "That's a bummer.",
    "Darn"  
    ]

  neutral_responses = [
      str(user_input) + "?",
      
  ]

  if user_mood == "unhappy":
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
  "definitely"
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
  "naw"
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
]


ask_question = [
  do_you_have,
  do_you_like,
]

def init_question():
  print("")

def run_game():
  if user_input == quit_chat:
      run_game = False
      return False

  run_game = True
  return True

def init_chat():
  user_name = input("Hi! What is your name? \n")
  print("Hello, " +  user_name + "! Nice to meet you!")

def check_input():
  for keyword in negative_key_word:
    if keyword in user_input:
      return "unhappy"
  for keyword in positive_key_word:
      if keyword in user_input:
        return "happy"
  return "neutral"


init_chat() 

while run_game():
  user_mood = "unhappy"
  user_input = str.lower(input(random.choice(random.choice(ask_question)) + "\n" ))

  if(run_game()):
    user_mood = check_input()
    chat_responses(user_input, user_mood)
