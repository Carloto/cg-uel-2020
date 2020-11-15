import argparse


class bresenham:
    """Classe que contém as funções para o cálculo dos pontos"""

    def __init__(self, p0, p1):
        """Inicializa os valores"""

        self.initial = True  # True se for o ponto inicial
        self.end = False  # True se for o ponto final
        self.p0 = p0
        self.p1 = p1
        self.x0 = p0[0]
        self.y0 = p0[1]
        self.x1 = p1[0]
        self.y1 = p1[1]

    def next_point(self):
        """Calcula e retorna o próximo ponto"""
        
        if (self.initial == True):
            self.initial = False
            self.dx = abs(self.x1-self.x0)
            self.dy = abs(self.y1-self.y0)
            self.sx = 1 if (self.x0 < self.x1) else -1
            self.sy = 1 if (self.y0 < self.y1) else -1
            self.err = self.dx-self.dy
            return [self.x0, self.y0]

        if (self.x0 == self.x1) and (self.y0 == self.y1):
            self.end = True
            return [self.x1, self.y1]

        self.err2 = self.err*2

        if (self.err2 > -self.dy):
            self.err = self.err - self.dy
            self.x0 = self.x0 + self.sx

        if (self.err2 < self.dx):
            self.err = self.err + self.dx
            self.y0 = self.y0 + self.sy

        return [self.x0, self.y0]


def main():
    parser = argparse.ArgumentParser(description="Algoritmo de Bresenham")
    parser.add_argument("x1", type=int, help="x inicial")
    parser.add_argument("y1", type=int, help="y inicial")
    parser.add_argument("x2", type=int, help="x final")
    parser.add_argument("y2", type=int, help="y final")
    args = parser.parse_args()
    b = bresenham([args.x1, args.y1], [args.x2, args.y2])
    while not b.end:
        print(b.next_point())


if __name__ == '__main__':
    main()
