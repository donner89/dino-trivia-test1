print("Hello and welcome to DINO FIGHT TRIVIA!")

ans = input('Are you ready to play this super, non-biased, awesome trivia? (yes/no): ')
score = 0
num_questions = 4

if ans.lower() == 'yes' or ans.lower() =='y':
    ans = input('1. T-Rex v. Goku, who wins? ')
    if ans.lower() == 'goku':
        score += 1
        print('Duh, of course')
    else:
        print('a T-Rex, really? Versus Goku??')
        score += 0

    ans = input('2. T-Rex v. Saitama, who wins? ')
    if ans.lower() == 'saitama'or ans.lower() == 'one punch man':
        score += 1
        print("well of course, Saitama was frustrated after playing video games with King")
    else:
        print('come on, really?')
        score += 0

    ans = input('3. T-Rex v. Gojo? ')
    if ans.lower() == 'gojo' or ans.lower() == 'satoru':
        score += 1
        print("Correct! When asked, Gojo said,'nah, I'd win'")
    else:
        print("Are you even trying?")
        score += 0

    ans = input('4. T-Rex v. Luffy? ')
    if ans.lower() == 'luffy':
        score += 1
        print("Correct! Afterwards Luffy invited Mr. T-Rex to join his crew.")
    else:
        print('by now, you should know this game is rigged')
        score += 0       

    mark = (score/num_questions) *100
    print("Thank you for playing this super (non-biased) game. You're final score was" , str(mark) +'%.')
    print("You correctly answered",  score, "out of", num_questions,".")

print("See you later alligator.")


    
