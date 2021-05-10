import math as m


def combinari(n, k):
    return m.factorial(n)/(m.factorial(k) * m.factorial(n-k))


def B_n_k_t(n, k, t):
    return combinari(n, k) * m.pow(t, k) * m.pow(1-t, n-k)


def B_n_k_t_derivat(n, k, t):
    c = combinari(n, k)
    if k > 0:
        c1 = k * m.pow(t, k-1)
    else:
        c1 = 1
    c2 = m.pow(1-t, n-k-1)
    return c * c1 * c2


def puncte_control(n):
    a = []

    for index in range(n+1):
        print("puntcul ", index)
        x = float(input("x = "))
        y = float(input("y = "))
        a.append((x, y))

    return a


def punct_k(lista, k):
    return lista[k-1]


def curba_bezier(n, t, puncte):
    curba_x = 0
    curba_y = 0

    for k in range(n):
        p = punct_k(puncte, k)
        curba_x += B_n_k_t(n, k, t) * p[0]
        curba_y += B_n_k_t(n, k, t) * p[1]

    return curba_x, curba_y


def curba_derivata(n, t, puncte):
    curba_derivata_x = 0
    curba_derivata_y = 0

    for k in range(n):
        p = punct_k(puncte, k)
        curba_derivata_x += B_n_k_t_derivat(n, k, t) * p[0]
        curba_derivata_y += B_n_k_t_derivat(n, k, t) * p[1]

    return curba_derivata_x, curba_derivata_y


def main():
    n = int(input("Gradul curbei Bezier : "))
    puncte = puncte_control(n)
    t = 0
    while t < 1.0:
        r = curba_bezier(n, t, puncte)
        print("r(", t, ") = ", r)
        r_d = curba_derivata(n, t, puncte)
        print("r'(", t, ") = ", r_d)
        t += 1/10


main()
