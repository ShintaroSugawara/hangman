import random

words = ("aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo", "baboon", "badger", "bat", "bear", "beaver", "bee", "bison", "boar", "buffalo", "butterfly", "camel", "capybara", "caribou", "cat", "caterpillar", "cattle", "chamois", "cheetah", "chicken", "chimpanzee", "chinchilla", "chough", "clam", "cobra", "cockroach", "cod", "coyote", "crab", "crane", "crocodile", "crow", "curlew", "deer", "dinosaur", "dog", "dogfish", "dolphin", "donkey", "dormouse", "dotterel", "dove", "dragonfly", "duck", "dugong", "dunlin", "eagle", "echidna", "eel", "eland", "elephant",  "elk", "emu", "falcon", "ferret", "finch", "fish", "flamingo", "fly", "fox", "frog", "gaur", "gazelle", "gerbil", "giraffe", "gnat", "gnu", "goat", "goldfinch", "goldfish", "goose", "gorilla", "goshawk", "grasshopper", "grouse", "guanaco", "gull", "hamster", "hare", "hawk", "hedgehog", "heron", "herring", "hippopotamus", "hornet", "horse", "human", "hummingbird", "hyena", "ibex", "ibis", "jackal", "jaguar", "jay", "jellyfish", "kangaroo", "kingfisher", "koala", "kookabura", "kouprey", "kudu", "lapwing", "lark", "lemur", "leopard", "lion", "llama", "lobster", "locust", "loris", "louse", "lyrebird", "magpie", "mallard", "manatee", "mandrill", "mantis", "marten", "meerkat", "mink", "mole", "mongoose", "monkey", "moose", "mosquito", "mouse", "mule", "narwhal", "newt", "nightingale", "octopus", "okapi", "opossum", "oryx", "ostrich", "otter", "owl", "ox", "oyster", "panda", "panther", "parrot", "partridge", "peafowl", "pelican", "penguin", "pheasant", "pig", "pigeon", "polar-bear", "pony", "porcupine", "porpoise", "quail", "quelea", "quetzal", "rabbit", "raccoon", "rail", "ram", "rat", "raven", "red-deer", "red-panda", "reindeer", "rhinoceros", "rook", "salamander", "salmon", "sand-dollar", "sandpiper", "sardine", "scorpion", "seahorse", "seal", "shark", "sheep", "shrew", "skunk", "snail", "snake", "sparrow", "spider", "spoonbill", "squid", "squirrel", "starling", "stingray", "stoat", "stork", "swallow", "swan", "tapir", "tarsier", "termite", "tiger", "toad", "trout", "turkey", "turtle", "viper", "vulture", "wallaby", "walrus", "wasp", "weasel", "whale", "wildcat", "wolf", "wolverine", "wombat", "woodcock", "woodpecker", "worm", "wren", "yak", "zebra")
selected_word = random.choice(words)

selected_word_list = ["_"] * len(selected_word)

hangman = {1:"あと4回です。",2:"あと3回です。",3:"あと2回です。",4:"あと1回です",5:"死亡"}
count = 0

include = False
win = False

predicted_alphabet_list = []
print(" ".join(selected_word_list))

while count <= 4 and "_" in selected_word_list:
    while True:
        predicted_alphabet = input("含まれている文字を予想してください:")

        if predicted_alphabet in predicted_alphabet_list:
            print("文字を変更してください")
        elif len(predicted_alphabet) == 1:
            predicted_alphabet_list.append(predicted_alphabet)
            break
        else:
            print("一文字のみ有効です。")

    str_count = 0

    for i in selected_word:
        if predicted_alphabet == i:
            selected_word_list[str_count] = predicted_alphabet
            include = True
        str_count += 1

    if include:
        print(predicted_alphabet,"は含まれていました。")
    else:
        print(predicted_alphabet,"は含まれていませんでした。")
        count += 1
        print(hangman[count])

    include = False

    print(" ".join(selected_word_list))

    if not "_" in selected_word_list:
        print("正解です。おめでとうございます。")
    elif count <= 4:
        continue
    else:
        print("正解は",selected_word,"でした。残念。")