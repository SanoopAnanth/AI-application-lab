l=["a","b","c","d"]
l.insert(4,"e")
print("inserting an element to existing list at specified position")
print(l)
print("Append operation")
l.append("f")
print(l)
m=["g","f","h"]
l.extend(m)
print("Using extend operation")
print(l)
print("Deleting operation")
l.remove("h")
print(l)
