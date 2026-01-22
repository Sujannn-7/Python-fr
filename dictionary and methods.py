marks = {
    "Tony" : 88,
    "Steve" : 90,
    "Peter" : 75,
    "Hari" : 68
}
print(marks)
print(marks.items())
print(marks["Steve"])
print(marks.values())
print(marks.get("Tony"))
print(marks.get("Harry"))
marks.update({"Hari":21})
print(marks)
marks.update({"Natasha" : 85})
marks["Clint"] = "29"
print(marks)
print(marks.pop("Hari"))
print(marks)
print(marks.popitem())
print(marks)
marks1 = marks.copy()
print(marks1)
marks1.clear()
print(marks1)
marks2 = list(marks)
print(marks2)
marks3 = list(marks.values())
print(marks3)
d = {}
print(type(d))