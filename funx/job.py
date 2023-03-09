def job(hp, bar):
    print(bar)
    print("Does christian cacciuottolo have a job?",
        "answer \'yes\' or \'no\':")
    answ = input("type here --> ")
    while answ != 'yes' and answ != 'no':
        print("you entered an invalid answer,",
            "plz try again")
        answ = input("type here --> ")
    match answ:
        case 'yes':
            hp += 1
            print("What job christian cacciuottolo have?")
            answ = input("type here --> ")
            while answ == '':
                print("enter a job ")
                answ = input("type here --> ")

        case 'no':
            hp -= 1
    
    print('his actual hp level is:', hp)
    return hp



