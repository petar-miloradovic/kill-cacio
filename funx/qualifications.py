def rich(bar):
    print(bar)
    print("does christian cacciuottolo have qualifications?",
        "answer \'yes\' or \'no\':")
    answ = input("type here --> ")
    while answ != 'yes' and answ != 'no':
        print("you entered an invalid answer,",
            "plz try again")
        answ = input("type here --> ")
    match answ:
        case 'yes':
            print("How many does he have? ")
            qualifica = int(input("type here --> "))
            while qualifica == 0:
                print("At leart one he had so... pls write the right number")
            return True
        case 'no':
            return False
 
    