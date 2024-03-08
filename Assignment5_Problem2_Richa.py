{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5156beec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "first number: 1\n",
      "second number: 2\n",
      "The sum is: 3\n"
     ]
    }
   ],
   "source": [
    "class Calculator:\n",
    "    def add(self, num1, num2):\n",
    "        return num1 + num2\n",
    "\n",
    "def main():\n",
    "    num1 = int(input(\"first number: \"))\n",
    "    num2 = int(input(\"second number: \"))\n",
    "    calc = Calculator()\n",
    "    print(\"The sum is:\", calc.add(num1, num2))\n",
    "\n",
    "main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c328bcb1",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
