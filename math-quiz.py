#!/usr/bin/env python3

#
# A math game for young kids
#

import cmd
import os
import random

class AddQuiz(cmd.Cmd):
  intro = 'Welcome to the Addition Quiz!\n'
  prompt = '(Press Enter to start) '
  
  a = None
  b = None
  answer = None
  tries = None
  
  correct = 0
  incorrect = 0
  questions = 0
  
  def emptyline(self):
    if self.answer == None:
      self.do_start(None)
  
  def do_start(self, arg):
    'Start the Addition Quiz:  START'
    self.tries = 3
    self.a = random.randint(0,10)
    self.b = random.randint(0,10)
    self.answer = self.a + self.b
    self.prompt = "{} + {} = ? ".format(self.a, self.b)
    self.do_reset(None)
    
  def precmd(self, line):
    try:
      int(line)
      line = "answer {}".format(line)
    except ValueError:
      pass
    return line
  
  def do_answer(self, arg):
    'Submit an answer:  ANSWER'
    if int(arg) == self.answer:
      print("Correct!")
      self.answer = None
      self.prompt = '(Press Enter to continue) '
      self.correct += 1
      self.questions += 1
    else:
      self.tries -= 1
      if self.tries >= 0:
        print("{} tries remaining".format(self.tries))
      if self.tries == 0:
        self.incorrect += 1
        self.questions += 1
        print()
        print("Answer: {} + {} = {}".format(self.a, self.b, self.answer))
        print()
        self.answer = None
        self.prompt = '(Press Enter to continue) '
  
  def do_score(self, arg):
    'Show the score:  SCORE'
    print("Addition score:")
    print("  {} correct".format(self.correct))
    print("  {} incorrect".format(self.incorrect))
    print("  {} questions".format(self.questions))
    print()
  
  def preloop(self):
    self.do_reset(None)
  
  def do_reset(self, arg):
    'Clear the screen:  RESET'
    os.system('clear')  
  
  def do_quit(self, arg):
    'Close the Addition Quiz, and return:  QUIT'
    self.do_reset(None)
    print("Thanks for playing Addition Quiz!")
    print()
    self.do_score(None)
    return True


class SubtractQuiz(cmd.Cmd):
  intro = 'Welcome to the Subtraction Quiz!\n'
  prompt = '(Press Enter to start) '
  
  a = None
  b = None
  answer = None
  tries = None
  
  correct = 0
  incorrect = 0
  questions = 0
  
  def emptyline(self):
    if self.answer == None:
      self.do_start(None)
  
  def do_start(self, arg):
    'Start the Subtraction Quiz:  START'
    self.tries = 3
    self.a = random.randint(0,10)
    self.b = random.randint(0,10)
    # Ensure that a is always greater than b
    if (self.b > self.a):
      self.a, self.b = (self.b, self.a)
    self.answer = self.a - self.b
    self.prompt = "{} - {} = ? ".format(self.a, self.b)
    self.do_reset(None)
    
  def precmd(self, line):
    try:
      int(line)
      line = "answer {}".format(line)
    except ValueError:
      pass
    return line
  
  def do_answer(self, arg):
    'Submit an answer:  ANSWER'
    if int(arg) == self.answer:
      print("Correct!")
      self.answer = None
      self.prompt = '(Press Enter to continue) '
      self.correct += 1
      self.questions += 1
    else:
      self.tries -= 1
      if self.tries >= 0:
        print("{} tries remaining".format(self.tries))
      if self.tries == 0:
        self.incorrect += 1
        self.questions += 1
        print()
        print("Answer: {} - {} = {}".format(self.a, self.b, self.answer))
        print()
        self.answer = None
        self.prompt = '(Press Enter to continue) '
  
  def do_score(self, arg):
    'Show the score:  SCORE'
    print("Subtraction score:")
    print("  {} correct".format(self.correct))
    print("  {} incorrect".format(self.incorrect))
    print("  {} questions".format(self.questions))
    print()
  
  def preloop(self):
    self.do_reset(None)
  
  def do_reset(self, arg):
    'Clear the screen:  RESET'
    os.system('clear')  
  
  def do_quit(self, arg):
    'Close the Subtraction Quiz, and return:  QUIT'
    self.do_reset(None)
    print("Thanks for playing Subtraction Quiz!")
    print()
    self.do_score(None)
    return True


class MathQuiz(cmd.Cmd):
  intro = "Welcome to the Math Quiz!\n"
  prompt = '(add, subtract or quit) '
  
  def do_add(self, arg):
    'Do the addition quiz:  ADD'
    try:
      AddQuiz().cmdloop()
    except KeyboardInterrupt:
      print()
      print("Thanks for playing Addition Quiz")
  
  def do_subtract(self, arg):
    'Do the subtraction quiz:  SUBTRACT'
    try:
      SubtractQuiz().cmdloop()
    except KeyboardInterrupt:
      print()
      print("Thanks for playing Subtraction Quiz")
  
  def emptyline(self):
    pass
  
  def preloop(self):
    self.do_reset(None)
  
  def do_reset(self, arg):
    'Clear the screen:  RESET'
    os.system('clear')
  
  def do_quit(self, arg):
    'Close the Math Quiz, and exit:  QUIT'
    print("Thanks for playing Math Quiz!")
    return True


if __name__ == '__main__':
  try:
    MathQuiz().cmdloop()
  except KeyboardInterrupt:
    print()
    print("Thanks for playing Math Quiz!")
