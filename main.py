from funx.intro import intro
from funx.richness import rich

hp = 0
bar = "-*"*50

if __name__ == "__main__":
    intro(bar)
    hp += rich(hp, bar)
    
