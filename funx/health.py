def health(hp, bar):
    print(bar)
    print("Is christian cacciuottolo in a health state",
        "answer \'yes\' or \'no\':")
    answ = input("type here --> ")
    while answ != 'yes' and answ != 'no':
        print("you entered an invalid answer,",
            "plz try again")
        answ = input("type here --> ")
    match answ:
        case 'yes':
            hp += 1
        case 'no':
            hp -= 1
    
    print('his actual hp level is:', hp)
    return hp