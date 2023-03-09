def furry(hp, bar):
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
            hp += 1
            print('what type of furry are you?',
                  'you can choose betweem \'canine\', \'feline\' abd \'other\'')
            fur = input("type here --> ")
            while fur != 'canine' and fur != 'feline' and fur != 'other':
                print("you entered an invalid answer,",
                    "plz try again")
                fur = input("type here --> ")
            match fur:
                case 'canine':
                    hp += 2
                case 'feline':
                    hp += 1
                case 'other':
                    hp -= 1
        case 'no':
            hp -= 1
    print('his actual hp level is:', hp)
    return hp