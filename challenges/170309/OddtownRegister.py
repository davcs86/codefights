def OddtownRegister(requests):
    owners = {}
    startups = {}
    for i in range(len(requests)):
        r = requests[i]
        for j in range(len(r)):
            o = r[j]
            if o not in owners:
                owners[o] = []
            owners[o].append(i)
    for i in range(len(requests)):
        r = requests[i]
        startups[i] = {
            "status": True,
            "owners": [],
            "idx": i
        }
        for j in range(len(r)):
            o = r[j]
            startups[i]["status"] = startups[i]["status"] and len(owners[o]) % 2 == 1
            startups[i]["owners"] += owners[o]
        startups[i]["owners"] = list(set(startups[i]["owners"]))
    startupLst = sorted(startups.values(), key=lambda x: len(x["owners"]) * int(not x["status"]))
    while not startupLst[-1]["status"]:
        startup = startupLst[-1]
        #fix owners
        for o in startup["owners"]:
            if o in startups:
                startups[o]["status"] = True
        # del from dict
        del startups[startup["idx"]]
        # re-index
        startupLst = sorted(startups.values(), key=lambda x: len(x["owners"]) * int(not x["status"]))

    return len(startups.values())

print OddtownRegister([[0,17,22],
 [0,17,35],
 [0,22,35],
 [0],
 [4,5,35]])