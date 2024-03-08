{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "30407b69",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[5], line 9\u001b[0m\n\u001b[1;32m      6\u001b[0m     \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mgreet\u001b[39m(\u001b[38;5;28mself\u001b[39m):\n\u001b[1;32m      7\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mHello, \u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mfirst_name\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m \u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlast_name\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m, have a wonderful day!\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m----> 9\u001b[0m F \u001b[38;5;241m=\u001b[39m \u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mWhat is your first name? \u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m     10\u001b[0m L \u001b[38;5;241m=\u001b[39m \u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mWhat is your last name? \u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m     13\u001b[0m greeter \u001b[38;5;241m=\u001b[39m Greet(F, L)\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.11/site-packages/ipykernel/kernelbase.py:1202\u001b[0m, in \u001b[0;36mKernel.raw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m   1200\u001b[0m     msg \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mraw_input was called, but this frontend does not support input requests.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m   1201\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m StdinNotImplementedError(msg)\n\u001b[0;32m-> 1202\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_input_request(\n\u001b[1;32m   1203\u001b[0m     \u001b[38;5;28mstr\u001b[39m(prompt),\n\u001b[1;32m   1204\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_parent_ident[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mshell\u001b[39m\u001b[38;5;124m\"\u001b[39m],\n\u001b[1;32m   1205\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mget_parent(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mshell\u001b[39m\u001b[38;5;124m\"\u001b[39m),\n\u001b[1;32m   1206\u001b[0m     password\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mFalse\u001b[39;00m,\n\u001b[1;32m   1207\u001b[0m )\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.11/site-packages/ipykernel/kernelbase.py:1245\u001b[0m, in \u001b[0;36mKernel._input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m   1242\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m:\n\u001b[1;32m   1243\u001b[0m     \u001b[38;5;66;03m# re-raise KeyboardInterrupt, to truncate traceback\u001b[39;00m\n\u001b[1;32m   1244\u001b[0m     msg \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInterrupted by user\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m-> 1245\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m(msg) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m   1246\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m:\n\u001b[1;32m   1247\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlog\u001b[38;5;241m.\u001b[39mwarning(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInvalid Message:\u001b[39m\u001b[38;5;124m\"\u001b[39m, exc_info\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "class Greet:\n",
    "    def __init__(self, first_name, last_name):\n",
    "        self.first_name = first_name\n",
    "        self.last_name = last_name\n",
    "\n",
    "    def greet(self):\n",
    "        return f\"Hello, {self.first_name} {self.last_name}, have a wonderful day!\"\n",
    "\n",
    "F = input(\"What is your first name? \")\n",
    "L = input(\"What is your last name? \")\n",
    "\n",
    "\n",
    "greeter = Greet(F, L)\n",
    "print(greeter.greet())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b1864ba",
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
