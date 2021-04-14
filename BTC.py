import os

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
print("The platform is :", os.name)

choice='y'
while(choice=='y'):
    persenMeasure=input("Measure \t: ")
    hargaBTC=input("Harga BTC \t: ")

    hasilMeasure=(float(persenMeasure)/100)/10
    hasilFinal=float(hargaBTC)*float(hasilMeasure)
    tp=float(hargaBTC)-float(hasilFinal)

    print("Take Profit di \t:",tp)
    choice=input("Ulang? (y/n) \t:")
    screen_clear()