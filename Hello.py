#!/use/bin/evn python
# _*_ coding:utf-8 _*_
import random
from typing import Any, Union

secret = random.randint(1, 100)
guess = 0
trie = 0

print("AHOY! I am the Dread priate Robers, and I have a secret!")
print("It is a number from 1 to 99, I'll give you 6 tries")

while guess != secret and trie < 6:
    guess = int(input("what's you guess?"))
    if guess < secret:
        print("TOO LOW, ye scurvy dog!")
    elif guess > secret:
        print("TOO HIGH, landlubber")
    trie = trie + 1
if guess == secret:
    print("ye got it ! FOND my secret ,ye did!")
    print("The secret number was ", secret)
else:
    print("NO more guess ! Better luck next time matey!!")
    print("The secret number was ", secret)
