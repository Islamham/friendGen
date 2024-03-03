import random

def randomizer() :
    arr = ["An african-american man","An asian man","A caucasian man","A middle eastern man", "A latino man",
           "An indian man", "An african-american woman","An asian woman","A caucasian woman","A middle eastern woman", "A latina woman",
           "An indian woman", "A 40-year-old happy korean man wearing, who is smiling and standing beside the person"]
    return random.choice(arr)


print(randomizer())