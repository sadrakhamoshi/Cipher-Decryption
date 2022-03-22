import math


class NgramScore:
    def __init__(self, filepath='quadrams.txt'):
        self.ngrams = {}
        with open(filepath, 'r') as f:
            lines = f.readlines()
            self.ngrams_len = len(lines)
            for l in lines:
                key, score = l.split(' ')
                self.ngrams[key] = int(score)

        # compute probabilities
        total = sum(self.ngrams.values())
        self.floor = math.log10(0.01 / total)
        for k in self.ngrams.keys():
            self.ngrams[k] = math.log10((self.ngrams[k] / total))

    def compute(self, text: str):
        score = 0
        text_len = len(text)
        keys = self.ngrams.keys()
        for i in range(text_len - 3):
            sub_text = text[i:i + 4]
            if sub_text in keys:
                score += self.ngrams[sub_text]
            else:
                score += self.floor
        return score


if __name__ == '__main__':
    ngram = NgramScore('quadrams.txt')
    print(ngram.compute('SDRGGFYTVDFE'))
