animal = ['Deer', 'Tiger', 'Fox', 'Donkey ', 'Lion', 'Monkey']
animal = [x for (i,x) in enumerate(animal) if i not in (0,4,5)]
print(animal)