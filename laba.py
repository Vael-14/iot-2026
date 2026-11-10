def peppa_cipher(s, k):
    chars = []
    for ch in s:
        chars.append(ch)

    result = ""
    pos = 0

    while len(chars) > 0:
        pos = (pos + k - 1) % len(chars)

        result += chars[pos]

        new_chars = []
        for i in range(len(chars)):
            if i != pos:
                new_chars.append(chars[i])
        chars = new_chars

    return result

s = input("Введіть рядок S: ")

k = int(input("Введіть ключ K (цифра від 1 до 10): "))
while k < 1 or k > 10:
    print("Ключ має бути від 1 до 10!")
    k = int(input("Введіть ключ K (цифра від 1 до 10): "))

c = peppa_cipher(s, k)
print("Шифр C:", c)