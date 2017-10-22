#!/usr/bin/env python3
from sympy.solvers import solve
from sympy import Symbol

class WeinerAttack:
    expansions = []
    e = 0
    N = 0

    def __init__(self, e, N):
        self.e = e
        self.N = N

    def continued_fraction(self):
        num = self.e
        den = self.N
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

    def phi(self):
        c = self.convergent_expansion()
        next(c)
        for k, h in c:
            yield self.e * k - 1 // h


    def solve_poly(self):
        x = Symbol('x')
        for phi in self.phi():
            p = [1, (self.N - phi + 1), self.N]
            roots = solve(p[0]*x**2 -  p[1]*x + p[2], x)

            if roots[0] * roots[1] == self.N:
                print(roots)



def main():
    e = 165528674684553774754161107952508373110624366523537426971950721796143115780129435315899759675151336726943047090419484833345443949104434072639959175019000332954933802344468968633829926100061874628202284567388558408274913523076548466524630414081156553457145524778651651092522168245814433643807177041677885126141
    n = 380654536359671023755976891498668045392440824270475526144618987828344270045182740160077144588766610702530210398859909208327353118643014342338185873507801667054475298636689473117890228196755174002229463306397132008619636921625801645435089242900101841738546712222819150058222758938346094596787521134065656721069
    attack = WeinerAttack(e, n)
    attack.continued_fraction()

    attack.solve_poly()



if __name__ == '__main__':
    main()
