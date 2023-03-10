def family(bar):
    print(bar)
    print("Does christian cacciuottolo have a family?",
        "answer \'yes\' or \'no\':")
    answ = input("type here --> ")
    while answ != 'yes' and answ != 'no':
        print("you entered an invalid answer,",
            "plz try again")
        answ = input("type here --> ")
    match answ:
        case 'yes':
            return True
        case 'no':
            return False
    