def generate_password(n):
    result = ""
    for i in range(1, 21):
        for j in range(i + 1, 21):
            pair_sum = i + j

            # Проверяем кратность
            if n % pair_sum == 0:
                result = result + f"{i}{j}"

    return result
n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    print(generate_password(n))
else:
    print("Число должно быть от 3 до 20.")