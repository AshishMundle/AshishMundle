#performing with statement

with open("myfile.txt","w") as f:
  f.write("amit\n")
  f.write("ashish\n")
  f.write("prashant\n")
  print("file closed:",f.closed)

print("file closed:",f.closed)