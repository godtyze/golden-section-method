import math


def main():
    a, b, e = input("Введите левую границу: "), input("Введите правую границу: "), input("Введите размер шаг: ")

    r1 = 0.382
    r2 = 0.618
    n = 0

    a, b, e = float(a), float(b), float(e)
    print(f"Входные данные: функция sin(x**2)+5*x+1, отрезок [{a}, {b}], eps {e}\n")
    first_check(a, b, e, r1, r2, n)


def func(x):
    return math.sin(x**2)+5*x+1


def solve_function(x):
    try:
        return round(float(func(x)), 4)
    except:
        return False


def first_check(a, b, e, r1, r2, n):
    delt = b - a
    x = round(a + r1 * delt, 4)
    y = round(a + r2 * delt, 4)

    fx = solve_function(x)
    fy = solve_function(y)

    print(f"D={b}-{a}={delt}\nX={a}+{r1}*{delt}={x}\nY={a}+{r2}*{delt}={y}\nf({x})={fx}\nf({y})={fy}\n")
    compare_xy(a, b, e, r1, r2, x, y, fx, fy, n)


def compare_xy(a, b, e, r1, r2, x, y, fx, fy, n):
    n += 1
    print(f"Итерация {n}\n")
    if fx < fy:
        print(f"{fx} < {fy}\n")
        compared_less(a, b, e, r1, r2, x, y, fx, fy, n)
    else:
        print(f"{fx} > {fy}\n")
        compared_greater(a, b, e, r1, r2, x, y, fx, fy, n)


def compared_less(a_old, b_old, e, r1, r2, x_old, y_old, fx_old, fy_old, n):
    a = a_old
    b = y_old
    delt = round(b - a, 4)
    print(f"a={a}\nb={b}\nD={b}-{a}={delt}\n")
    if delt < e:
        print(f"Ответ: x(min)={x_old}, f({x_old})={solve_function(x_old)}")
    else:
        y = x_old
        fy = fx_old
        x = round(a + r1 * delt, 4)
        fx = solve_function(x)
        print(f"Y={y}\nX={x}\nf(y)={fy}\nf(x)={fx}\n")
        compare_xy(a, b, e, r1, r2, x, y, fx, fy, n)


def compared_greater(a_old, b_old, e, r1, r2, x_old, y_old, fx_old, fy_old, n):
    a = x_old
    b = b_old
    delt = round(b - a, 4)
    print(f"a={a}\nb={b}\nD={b}-{a}={delt}\n")
    if delt < e:
        print(f"Ответ: x(min)={x_old}, f({x_old})={solve_function(x_old)}")
    else:
        x = y_old
        fx = fy_old
        y = round(a + r2 * delt, 4)
        fy = solve_function(y)
        print(f"Y={y}\nX={x}\nf(y)={fy}\nf(x)={fx}\n")
        compare_xy(a, b, e, r1, r2, x, y, fx, fy, n)


if __name__ == "__main__":
    main()
