def ab9():
    from PIL import Image
    import os
    a = r"C:\АиП\1.jpg"
    b = r"C:\АиП\a9"
    os.makedirs(b, exist_ok = True)
    for c in os.listdir(a):
        if c.endswith(".jpg") or c.endswith(".png"):
            d = os.path.join(a, c)
            e = Image.open(d)
            f = (e.size[0] // 2, e.size[1] // 2)
            e = e.resize(f)
            g = os.path.join(b, c)
            e.save(g)
            print(f"Сохранено обработанное изображение: {c}")
def c9():
    import csv
    a = 0
    with open('C:\АиП\cc9.csv', 'r') as d:
        b = csv.reader(d)
        next(b)
        print("Нужно купить:")
        for e in b:
            product, quantity, price = e
            f = int(quantity) * int(price)
            a += f
            print(f"{product} - {quantity} шт. за {price} руб.")
        print(f"Итоговая сумма: {a} руб.")