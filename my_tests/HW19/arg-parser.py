import argparse

parser = argparse.ArgumentParser(prog="arg-parser.py", description="Як і просилося в задачі текст "
                                                                   "'Тут могла бути ваша... допомога =)'",
                                 epilog="А це тіпа я заглянув в документацію, і тепер вимахуюсь")

parser.add_argument("-n", "--name", action="store", help="Greeting you here")

args = parser.parse_args()
if args.name == "Мурзік":
    print("А скажітє, Мурзік... Васильович, і не надоїло вам буть отаким суперменом?")
elif args.name == "Валєнтін":
    print("Валєнтін, японскій бог, ти зачєм у ката яйца-та аткрутіл?!")
else:
    print(f"Welcome {args.name}")
