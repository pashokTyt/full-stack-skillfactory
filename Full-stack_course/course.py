import random


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
