import sys

from pylint import lint

TRESHOLD = 10
run = lint.Run("--rcfile=.pylintrc", ['main.py'], exit=False)
score = run.linter.stats.global_note

print(f'{score} pontot ért el a program')

if score < TRESHOLD:
    print(f'Nem érte el a treshold-ot a program. ({TRESHOLD})')
    sys.exit(1)
sys.exit(0)
