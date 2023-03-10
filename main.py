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
    if(rich(hp, bar) is True):
        hp += 1
    else:
        hp -= 1
    print('his actual hp level is:', hp)

    if(furry(hp, bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)    

    if(origin(hp, bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)

    if(job(hp, bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)    

    if(anime(hp, bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)

    if(loli(hp, bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)

    if(health(hp, bar) is True):
        hp += 1
    else:
        hp -= 1
    
    print('his actual hp level is:', hp)

    if(bank(hp, bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)    

    if(family(hp, bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)

    if(funny(hp, bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)    

    if(manga(hp, bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)

    if(porn(hp, bar) is True):
        hp += 1
    else:
        hp -= 1

    print('his actual hp level is:', hp)

    if(worth(hp, bar) is True):
        hp += 1
    else:
        hp -= 1

    if(hp < 0):
        print('christian cacciuottolo will be eliminated, fortunately')
    else:
        print('are you sure, he can live?\nFine , for now he is ok but not for far :)')    


if __name__ == "__main__":
        main()

  