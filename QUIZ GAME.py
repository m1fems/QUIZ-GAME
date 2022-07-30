def points_won(number):
    print(f'You got {number} questions right')
    quit()


points = 0
print('WELCOME TO THE QUIZ GAME')
print(" ")

print('How many legs does a spider have?')
answer1 = str(input())
if answer1 == '8' or 'eight':
    points += 1
else:
    points_won(points)

print('What is the name of the toy cowboy in Toy Story?')
answer1 = str(input())
if answer1 == 'Woody':
    points += 1
else:
    points_won(points)

print('What is the color of an emerald?')
answer1 = str(input())
if answer1 == 'Green':
    points += 1
else:
    points_won(points)

print('What is something you hit with a hammer?')
answer1 = str(input())
if answer1 == 'Nail':
    points += 1
else:
    points_won(points)

print('What’s the name of a place you go to see lots of animals?')
answer1 = str(input())
if answer1 == 'Zoo':
    points += 1
else:
    points_won(points)

print('Whose nose grew longer every time he lied?')
answer1 = str(input())
if answer1 == 'Pinocchio':
    points += 1
else:
    points_won(points)

print('What is the name of the fairy in Peter Pan?')
answer1 = str(input())
if answer1 == 'Tinkerbell':
    points += 1
else:
    points_won(points)

print('If you freeze water, what do you get?')
answer1 = str(input())
if answer1 == 'Ice':
    points += 1
else:
    points_won(points)

print('How many planets are in our solar system?')
answer1 = str(input())
if answer1 == 'Eight' or '8':
    points += 1
else:
    points_won(points)

print('What fruit do kids traditionally give to teachers?')
answer1 = str(input())
if answer1 == 'Apple':
    points += 1
else:
    points_won(points)

print('In which capital city of Europe would you find the Eiffel Tower?')
answer1 = str(input())
if answer1 == 'Paris':
    points += 1
else:
    points_won(points)

print('What is the opposite of ‘cheap’?')
answer1 = str(input())
if answer1 == 'Expensive':
    points += 1
else:
    points_won(points)

print('A scientist who studies rocks is called a what?')
answer1 = str(input())
if answer1 == 'Geologist':
    points += 1
else:
    points_won(points)

print('If you suffer from arachnophobia, which animal are you scared of?')
answer1 = str(input())
if answer1 == 'Spiders':
    points += 1
else:
    points_won(points)

print('What kind of tree do acorns come from?')
answer1 = str(input())
if answer1 == 'Oak':
    points += 1
else:
    points_won(points)

print('How many bones do sharks have?')
answer1 = str(input())
if answer1 == 'Zero' or '0':
    points += 1
else:
    points_won(points)

print('The Statue of Liberty came from which country to the United States?')
answer1 = str(input())
if answer1 == 'France':
    points += 1
else:
    points_won(points)

print('What is the imaginary line called that connects the north and south pole?')
answer1 = str(input())
if answer1 == 'Prime Meridian':
    points += 1
else:
    points_won(points)

print('How many Great Lakes are there?')
answer1 = str(input())
if answer1 == 'Five' or '5':
    points += 1
else:
    points_won(points)

print('Which famous ocean liner sank on her first voyage in 1912?')
answer1 = str(input())
if answer1 == 'Titanic':
    points += 1
    print('CONGRATULATIONS YOU GOT ALL 20 QUESTIONS RIGHT')
else:
    points_won(points)
