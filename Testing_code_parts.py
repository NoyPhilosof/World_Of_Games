import pickle
scores = []



kwarg = {"a":1, "b":2, "c":{"c":3}, "d": [1,2,"Shalom"], (1,2):1}

def func(a,b,d):
	pass

func(**kwarg) = func(kwarg["a"],kwarg["b"], kwarg["c"])








scores_file = "scores.pickle"


with open(scores_file, "wb") as wrt:
    pickle.dump(scores, wrt)


with open(scores_file, "rb") as ld:
    a = pickle.load(ld)


print(a)

a["score"] = 13

with open(scores_file, "wb") as wrt:
    pickle.dump(a, wrt)

with open(scores_file, "rb") as ld:
    a = pickle.load(ld)


print(a)

# with open(path_to_file, "wt") as write_buffer:
# 	text_in_file = read_buffer.readlines()

