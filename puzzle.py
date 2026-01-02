from logic import *

people = ["Gilderoy", "Pomona", "Minerva", "Horace"]
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

symbols = []

knowledge = And()

# Create symbols
for person in people:
    for house in houses:
        symbol = Symbol(f"{person}{house}")
        symbols.append(symbol)

# Each person belongs to exactly one house
for person in people:
    knowledge.add(
        Or(
            Symbol(f"{person}Gryffindor"),
            Symbol(f"{person}Hufflepuff"),
            Symbol(f"{person}Ravenclaw"),
            Symbol(f"{person}Slytherin")
        )
    )

    for house1 in houses:
        for house2 in houses:
            if house1 != house2:
                knowledge.add(
                    Implication(
                        Symbol(f"{person}{house1}"),
                        Not(Symbol(f"{person}{house2}"))
                    )
                )

# Each house has exactly one person
for house in houses:
    knowledge.add(
        Or(
            Symbol(f"Gilderoy{house}"),
            Symbol(f"Pomona{house}"),
            Symbol(f"Minerva{house}"),
            Symbol(f"Horace{house}")
        )
    )

    for person1 in people:
        for person2 in people:
            if person1 != person2:
                knowledge.add(
                    Implication(
                        Symbol(f"{person1}{house}"),
                        Not(Symbol(f"{person2}{house}"))
                    )

                )

knowledge.add(

    Or(Symbol("GilderoyGryffindor"),Symbol("GilderoyRavenclaw"))
)
knowledge.add(Not(Symbol("PomonaSlytherin")))
knowledge.add(Symbol("MinervaGryffindor"))



# print(knowledge.formula())
for symbol in symbols:
        if model_check(knowledge, symbol):
            print(symbol)


