from KeyPad4x4 import KeyPad4x4

keyPad = KeyPad4x4(21,16,15,23,2,4,5,22)
keyPad.init()

while True:
    key =  keyPad.onPress()
    print("key Pressed", key)


