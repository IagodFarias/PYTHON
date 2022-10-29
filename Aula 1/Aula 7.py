#Conversor de unidades de medida

measure = float(input("whats measure?"))
# MM DC CM M DAM HEC KM
Km = measure * 1000
Hec = measure * 100
dam= measure * 10
cm = measure * 0.1
dc = measure * 0.01
mm = measure * 0.001

print("a medida em KM é {:.0f} ".format(Km))
print("a medida em HEC é {:.0f} ".format(Hec))
print("a medida em Dam é {:.0f} ".format(dam))
print("a medida em cm é {:.2f}".format(cm))
print("a medida em dc é {}".format(dc))
print("a medida em mm é {}".format(mm))

