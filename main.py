from funx.intro import intro
from funx.richness import rich
from funx.furry import furry
from funx.origins import origin
from funx.job import job
from funx.anime import anime
from funx.loli import loli
from funx.health import health
hp = 0
bar = "-*"*50

if __name__ == "__main__":
    intro(bar)
    hp += rich(hp, bar)
    hp += furry(hp, bar)
    hp += origin(hp,bar)
    hp += job(hp,bar)
    hp += anime(hp,bar)
    hp += loli(hp,bar)
    hp += health(hp,bar)