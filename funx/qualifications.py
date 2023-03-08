def rich(hp, bar):
    print(bar)
    print("does christian cacciuottolo have qualifications?",
        "answer \'yes\' or \'no\':")
    answ = input("type here --> ")
    while answ != 'yes' and answ != 'no':
        print("you entered an invalid answer,",
            "plz try again")
    match answ:
        case 'yes':
            n = list()
            hp += 1
        case 'no':
            hp -= 1
    print('how many qualifications do cacio have?')
    
    print('his actual hp level is:', hp)
    return hp