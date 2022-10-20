Arithmetic Exam Application

Main file: arithmetic.py
Scripts: checks.py, levels.py

How the program works:
  1. The user is offered a choice of one of the difficulty levels. At the moment, only two have been implemented.
  2. After selecting the difficulty, the program generates 5 examples of this complexity.
  3. The user's task is to answer each of the examples.
  4. After each user's response, the program reports whether the answer was correct?
  5. After answering each of the examples, the program reports the number of correct answers and offers to save the result.
  6. If the user agrees, the program requests his name and writes the result to a file "results.txt "

List of future improvements to the program:
  1. Add a complex exam. Increase a difficulty level on the fly. For example, if a person passed the 1st level, start the 2nd one immediately.
  2. Add a correction level: store the tasks with wrong answers and give them next time.
  3. Add more difficulty levels.
  4. Track the time (read about Timer).
  5. Write a more detailed report to a file with the results.
  6. Show previous results inside the app (show lines from results.txt that contains the username)
