phrase = "select disk 1"



if len(phrase) >= 13 and phrase[0:6] == "select" and phrase[7:11] == "disk":
  print(phrase)


