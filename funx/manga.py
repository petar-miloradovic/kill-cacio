def manga(bar):
    print(bar)
    print("Does christian cacciuottolo reads manga?",
        "answer \'yes\' or \'no\':")
    answ = input("type here --> ")
    while answ != 'yes' and answ != 'no':
        print("you entered an invalid answer,",
            "plz try again")
        answ = input("type here --> ")
    match answ:
        case 'yes':
            print("What is he favorite anime: ")
            man = input("type here --> ")
            while man != '':
                print("you entered an invalid answer,",
                    "plz try again")
                man = input("type here --> ")
            return True
        case 'no':
            return False
    