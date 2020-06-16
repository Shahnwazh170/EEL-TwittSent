import eel

eel.init('gui')

@eel.expose
def dummy(para):
    print("I received a parameter : ",para)
    return 1,1.5,"hello",[2,5,2],(8,6,3)


eel.start("index.html", size=(900, 720))

