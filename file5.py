words = ["shit", "crap", "bullshit", "damn", "hell"]
with open("censor.txt", "r") as f:
    data = f.read()
for word in words:
    data = data.replace(word, "*" * len(word))

with open ("censor.txt", "w") as f:
    f.write(data)
    print("Done!")