"""Alap python program"""
import math


class EgyenletMegoldo:
    """Egyenletmegoldó osztály"""

    def masodfoku_egyenlet_megoldo(self, a, b, c):
        """Másodfokú megoldó algoritmus"""
        if (type(a) not in [int, float] or
                type(b) not in [int, float] or
                type(c) not in [int, float]):
            raise TypeError('Csak számokat fogadunk el')

        d = math.pow(b, 2) - (4 * a * c)

        if d < 0:
            return None, None

        return (-b + math.sqrt(d)) / 2 * a, (-b - math.sqrt(d)) / 2 * a

    def feladatmegoldo(self, a, b, c):
        """Megoldó függvény"""
        e = EgyenletMegoldo()
        x1, x2 = e.masodfoku_egyenlet_megoldo(a, b, c)
        print(f'{a}^2 + {b}x + {c} = 0')
        if x1 is None and x2 is None:
            print('Nincs megoldás')
        elif x1 == x2:
            print(f'Egy megoldás: {x1}')
        else:
            print(f'Kettő megoldás:{x1} és {x2}')


if __name__ == '__main__':
    megoldo = EgyenletMegoldo()
    megoldo.feladatmegoldo(1, 2, 8)
    megoldo.feladatmegoldo(1, -14, 49)
    megoldo.feladatmegoldo(1, 6, 8)
