def rich(hp, bar):
    print(bar)
    print("is christian cacciuottolo rich?",
        "answer \'yes\' or \'no\':")
    answ = input("type here --> ")
    while answ != 'yes' and answ != 'no':
        print("you entered an invalid answer,",
            "plz try again")
    match answ:
        case 'yes':
            hp += 1
        case 'no':
            hp -= 1
    print('his actual hp level is:', hp)
    return hp