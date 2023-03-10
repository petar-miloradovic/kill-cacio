from funx.intro import intro
from funx.richness import rich
from funx.furry import furry
from funx.origins import origin
from funx.job import job
from funx.anime import anime
from funx.loli import loli
from funx.health import health
from funx.bank import bank
from funx.family import family
from funx.funny import funny
from funx.intro import intro
from funx.manga import manga
from funx.porn import porn
from funx.worth import worth


def main():
    hp = 0
    bar = "-*"*50
    #intro
    
    intro(bar)

    #funzioni 
    if(rich(bar) is True):
        hp += 1
    else:
        hp -= 1
    print('his actual hp level is:', hp)

    if(furry(bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)    

    if(origin(bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)

    if(job(bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)    

    if(anime(bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)

    if(loli(bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)

    if(health(bar) is True):
        hp += 1
    else:
        hp -= 1
    
    print('his actual hp level is:', hp)

    if(bank(bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)    

    if(family(bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)

    if(funny(bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)    

    if(manga(bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)

    if(porn(bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)

    if(worth(bar) is True):
        hp += 1
    else:
        hp -= 1

    if(hp < 0):
        print('christian cacciuottolo will be eliminated, fortunately')
    else:
        print('are you sure, he can live?\nFine , for now he is ok but not for far :)')    


if __name__ == "__main__":
        main()

  