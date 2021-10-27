{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9c14fa89-ff38-4c6a-bf30-d9bb97deaac9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def intersect(set1, set2):\n",
    "    new_set = set()\n",
    "    for x in set1:\n",
    "        for y in set2:\n",
    "            if x == y:\n",
    "                new_set.add(y)\n",
    "    return new_set"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
