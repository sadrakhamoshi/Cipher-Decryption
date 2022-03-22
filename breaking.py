import random
from typing import List
import wordninja
from score import NgramScore
from pycipher.simplesubstitution import SimpleSubstitution


class Decryption:
    def __init__(self, cipher_text: str, alphabets: str = None):
        self.cipher_text = cipher_text
        self.top_candidates = []
        self.alphabets = alphabets
        self.score = NgramScore()

    def run(self, max_tries=5):
        print('Decrypting ...\n')
        for i in range(max_tries):
            winner_key, score = self.choose_winner()
            print('itr {} ->\t winner_key : {} | Score : {} | plaintext : {}\n'.format(str(i),
                ''.join(winner_key), score, self.get_plaintext(winner_key)[:10]
            ))
            self.top_candidates.append((winner_key, score))
            self.top_candidates.sort(key=lambda i: i[1], reverse=True)
        print('Finished ...\n')

        return

    def write_result(self, filepath='result.txt'):
        with open(filepath, 'w') as f:
            key, score = self.top_candidates[0]
            plain_txt = self.get_plaintext(key=key)
            f.write(' '.join(wordninja.split(plain_txt)))
            
            print('> you can see result in result.txt file 😃')
            
    
    def get_plaintext(self, key: list):
        sub = SimpleSubstitution(''.join(key))
        return sub.decipher(self.cipher_text)

    def swap(self, key: list):
        a, b = random.randint(0, 25), random.randint(0, 25)
        new_key = list(key)
        new_key[a], new_key[b] = new_key[b], new_key[a]
        return new_key

    def choose_winner(self):
        old_key = list(self.alphabets)
        random.shuffle(old_key)
        plain_text = self.get_plaintext(old_key)
        old_score = self.score.compute(plain_text)
        j = 0
        while j < 1000:
            new_key = self.swap(old_key)
            new_plain_text = self.get_plaintext(new_key)
            new_score = self.score.compute(new_plain_text)
            if new_score > old_score:
                old_score = new_score
                old_key = new_key
                j = 0
            j += 1
        return old_key, old_score
