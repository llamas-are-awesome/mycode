marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"She-Hulk":
  {"real name": "jennifer walters",
  "powers": "super strength & intelligence",
  "archenemy": "Titania"}
             }

char_name= input("Who do you want to know about? Enter Starlord, Mystique or She-Hulk: ")
char_stat= input("What do you want to know about them? Enter real name, powers or archenemy: ")

print(f"{char_name} has the {char_stat} of {marvelchars[char_name][char_stat]}")
