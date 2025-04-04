import random


def horoscope():
    times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
    advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
    promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
                "неожиданного праздника", "приятных перемен"]
    generated_prophecies = []

    for i in range(5):
        time = random.choice(times).title()
        advice = random.choice(advices)
        promise = random.choice(promises)
        prophecy = f" {time} {advice} {promise}."
        generated_prophecies.append(prophecy)

    for generated in generated_prophecies:
        print(generated)


def check_active_user():
    email = input("Введите e-mail ")
    count = 0
    while email.find("@") == -1 and count != 2:
        print("неправильный email. Попробуйте еще раз: ")
        email = input("Введите e-mail ")
        count += 1


def main():
    check_active_user()


if __name__ == "__main__":
    main()
