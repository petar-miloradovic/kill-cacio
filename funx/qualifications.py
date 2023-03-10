def rich(bar):
    print(bar)
    print("does christian cacciuottolo have qualifications?",
        "answer \'yes\' or \'no\':")
    answ = input("type here --> ")
    while answ != 'yes' and answ != 'no':
        print("you entered an invalid answer,",
            "plz try again")
    match answ:
        case 'yes':
            return True
        case 'no':
            return False
 
    