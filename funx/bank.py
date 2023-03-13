def bank(bar):
    print(bar)
    print("Does christian cacciuottolo have money?",
        "answer \'yes\' or \'no\':")
    answ = input("type here --> ")
    while answ != 'yes' and answ != 'no':
        print("you entered an invalid answer,",
            "plz try again")
        answ = input("type here --> ")
    match answ:
        case 'yes':
            print("how meny money christian cacciuottolo have?")
            money = int(input("type here --> "))
            if(money < 0):
                return False
            else:
                return True    
        case 'no':
            return False
    
