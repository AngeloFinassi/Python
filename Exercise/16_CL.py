def Hello(name, lang):
    language = {
        "Port":"Olá",
        "Eng":"Hello",
        "Spanish":"Holla"
    }

    print(f"{language[lang]}! {name}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet"
    )

    parser.add_argument(
        "-l", "--lang", metavar="language", required=True, choices=["Port","Eng","Spanish"], help="The Language of gretting"
    )

    args = parser.parse_args()
     
    Hello(args.name, args.lang)