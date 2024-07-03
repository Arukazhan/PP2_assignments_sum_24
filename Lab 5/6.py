'''Replace all occurrences of space, comma, or dot with a colon.'''

import re

a = "I am truly devastated. How are you, darling?"
res = re.sub('[., ]', ':', a)

print(res)
