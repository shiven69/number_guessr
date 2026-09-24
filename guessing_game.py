{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9ad0b56b-8d05-4457-83b4-03178b2a3f09",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to the Number Guessing Game!\n",
      "I am thinking of a number between 1 and 100.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Enter your guess:  6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Too low! Try again.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Enter your guess:  60\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Too high! Try again.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Enter your guess:  30\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Too high! Try again.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Enter your guess:  10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Too low! Try again.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Enter your guess:  20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Too high! Try again.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Enter your guess:  15\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Too low! Try again.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Enter your guess:  17\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Too low! Try again.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Enter your guess:  18\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Too low! Try again.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Enter your guess:  19\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🎉 Congratulations! You guessed the exact number!\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "print(\"Welcome to the Number Guessing Game!\")\n",
    "print(\"I am thinking of a number between 1 and 100.\")\n",
    "\n",
    "# The computer picks a random number\n",
    "secret_number = random.randint(1, 100)\n",
    "guess = 0\n",
    "\n",
    "# Keep asking until the user guesses correctly\n",
    "while guess != secret_number:\n",
    "    guess = int(input(\"\\nEnter your guess: \"))\n",
    "    \n",
    "    if guess < secret_number:\n",
    "        print(\"Too low! Try again.\")\n",
    "    elif guess > secret_number:\n",
    "        print(\"Too high! Try again.\")\n",
    "    else:\n",
    "        print(\"🎉 Congratulations! You guessed the exact number!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "802fd543-44d3-411c-a63a-674fb3ef41fd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
