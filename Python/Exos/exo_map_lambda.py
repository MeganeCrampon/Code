invites = ["alice", "bob", "charlie"]
invites_maj = list(map(lambda i : i.upper(), invites))
print (invites_maj)

for i, nom in enumerate(invites_maj, start = 1) :
    print(f"Table n°{i} : {nom}")