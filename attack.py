#!/usr/bin/env python3

class WeinerAttack:
    expansions = []
    den = 0
    num = 0

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def continued_fraction(self):
        num = self.num
        den = self.den
        while (num != 1):
            expansion = num // den
            remainder = num % den
            self.expansions.append(expansion)
            num = den
            den = remainder

    def convergent_expansion(self):
        k = [1, 0]
        h = [0, 1]
        for i, expansion in enumerate(self.expansions):
            k_new = self.expansions[i] * k[i+1] + k[i]
            h_new = self.expansions[i] * h[i+1] + h[i]
            k.append(k_new)
            h.append(h_new)
            yield k_new, h_new

def main():
    attack = WeinerAttack(17993, 90581)
    attack.continued_fraction()

    for k, h in attack.convergent_expansion():
        print(k)
        print(h)

if __name__ == '__main__':
    main()
