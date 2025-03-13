

def sort(width, height, length, mass):

  is_bulky = False
  is_heavy = False

  if mass >= 20:
    is_heavy = True    

  if width >= 150 or height>= 150 or length >= 150 or (width * height * length) >= 1_000_000:
    is_bulky = True

  if not is_bulky and not is_heavy:
    return 'STANDARD'
  
  if is_bulky and is_heavy:
    return 'REGECTED'
  
  return 'SPECIAL'

status = sort(100, 90, 100, 10)
print(status)

pass



  
