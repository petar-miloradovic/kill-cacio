def origin(hp, bar):
    print(bar)
    print("What is christian cacciuottolo origin? It's from Italy?",
        "answer \'yes\' or \'no\':")
    answ = input("type here --> ")
    while answ != 'yes' and answ != 'no':
        print("you entered an invalid answer,",
            "plz try again")
        answ = input("type here --> ")
    match answ:
        case 'yes':
            hp += 1
            print('From which part of Italy christian cacciuottolo come from?',
                      "answer \'north\' , \'south\' , \'center':")
            italy = input("type here --> ")
            while italy != 'north' and italy != 'south' and italy != 'center':
                print("you entered an invalid answer,",
                    "plz try again")
                italy = input("type here --> ")
            match italy:
                case 'north':
                    hp += 1
                case 'center':
                    hp += 0
                case 'south':
                    hp -= 1
        case 'no':
            hp -= 1
    print('his actual hp level is:', hp)
    return hp



