s = input('Enter text: ')
def separator_text(s):
  s = s.split()
  f = open('text.txt','a')
  print(*s, sep = ' ', file = f)
  f.close()

separator_text(s)

