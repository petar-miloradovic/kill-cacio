def furry(bar):
    print(bar)
    print("Is christian cacciuottolo a furry?",
        "answer \'yes\' or \'no\':")
    answ = input("type here --> ")
    while answ != 'yes' and answ != 'no':
        print("you entered an invalid answer,",
            "plz try again")
        answ = input("type here --> ")
    match answ:
        case 'yes':
            print('what type of furry are you?',
            'you can choose betweem \'canine\', \'feline\' abd \'other\'')
            fur = input("type here --> ")
            while fur != 'canine' and fur != 'feline' and fur != 'other':
                print("you entered an invalid answer,",
                    "plz try again")
                fur = input("type here --> ")
            match fur:
                case 'canine':
                    return True
                case 'feline':
                    return False
                case 'other':
                    return False
        case 'no':
            return False


   