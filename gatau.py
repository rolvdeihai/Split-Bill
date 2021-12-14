import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from tabulate import tabulate

class MyGrid(Screen):
    global index
    global item
    global quant
    global price
    global bill1
    global bill2
    global bill3
    index = ObjectProperty(None)
    item = ObjectProperty(None)
    quant = ObjectProperty(None)
    price = ObjectProperty(None)
    bill1 = ObjectProperty(None)
    bill2 = ObjectProperty(None)
    bill3 = ObjectProperty(None)
    bill4 = ObjectProperty(None)
    index = 0
    item = []
    quant = []
    price = []

    def pressed(self):
        item.append(self.item.text)
        quant.append(int(self.quant.text))
        price.append(int(self.price.text))

        global index

        tempitem = self.item.text
        tempquan = int(self.quant.text)
        tempprice = int(self.price.text)

        if(index == 0):
            self.bill1.text = ""
            self.bill2.text = ""
            self.bill3.text = ""
            self.bill4.text = ""

        #self.bill.text += str(int(index+1)) + " | " + str(tempitem) + " | " + str(tempquan) + " | " + str(tempprice) + "\n"

        self.bill1.text += str(int(index+1)) + "\n"
        self.bill2.text += str(tempitem) + "\n"
        self.bill3.text += str(tempquan) + "\n"
        self.bill4.text += str(tempprice) + "\n"

        print(index + 1, " | ", item, " | ", quant, " | ", price, " | \n")

        index += 1

        self.item.text = ""
        self.quant.text = ""
        self.price.text = ""

    def resetbill(self):
        global index
        global item
        global quant
        global price

        index = 0
        item = []
        quant = []
        price = []
        self.bill1.text = ""
        self.bill2.text = ""
        self.bill3.text = ""
        self.bill4.text = ""

class InputNama(Screen):
    global penyokong
    global chris
    penyokong = ObjectProperty(None)

    def next(self):
        global chris
        chris = self.penyokong.text

class Hasil(Screen):
    global split1
    global split2
    global split3
    global split4
    global nobar
    global jubar
    global quant
    global item
    global price
    global index
    global total
    global intnob
    global intjub
    global kontol1
    global kontol2
    global kontol3
    global kontol4

    split1 = ObjectProperty(None)
    split2 = ObjectProperty(None)
    split3 = ObjectProperty(None)
    split4 = ObjectProperty(None)
    nobar = ObjectProperty(None)
    jubar = ObjectProperty(None)
    nobar = "k"
    jubar = "o"
    total = 0

    def calc(self):
        intnob = int(self.nobar.text)
        intjub = int(self.jubar.text)

        satuan = price[(intnob - 1)] / quant[(intnob - 1)] * (intjub)
        #self.split.text += str(int(index)) + " | " + str(item[intnob - 1]) + " | " + str(intjub) + " | " + str(satuan) + "\n"
        self.split1.text += str(int(index)) + "\n"
        self.split2.text += str(item[intnob - 1]) + "\n"
        self.split3.text += str(intjub) + "\n"
        self.split4.text += str(satuan) + "\n"

        global kontol1
        global kontol2
        global kontol3
        global kontol4
        kontol1 = self.split1.text
        kontol2 = self.split2.text
        kontol3 = self.split3.text
        kontol4 = self.split4.text
        print(item[intnob - 1], " ", intjub, " ", satuan, " ")
        global total

        total += satuan
        print("Total = ", total)

        self.nobar.text = ""
        self.jubar.text = ""

    def deltext(self):
        self.split1.text = ""
        self.split2.text = ""
        self.split3.text = ""
        self.split4.text = ""
        global intnob
        global intjub
        intnob = 0
        intjub = 0

class Akhir(Screen):
    global splitresult1
    global splitresult2
    global splitresult3
    global splitresult4
    global total
    global split1
    global split2
    global split3
    global split4
    global sokong
    global showtotal

    splitresult1 = ObjectProperty(None)
    splitresult2 = ObjectProperty(None)
    splitresult3 = ObjectProperty(None)
    splitresult4 = ObjectProperty(None)
    sokong = ObjectProperty(None)
    showtotal = ObjectProperty(None)

    def showresult(self):
        self.sokong.text = str(chris)
        #self.splitresult.text = str(kontol) + "Total = Rp. " + str(total)
        self.splitresult1.text = str(kontol1)
        self.splitresult2.text = str(kontol2)
        self.splitresult3.text = str(kontol3)
        self.splitresult4.text = str(kontol4)
        self.showtotal.text = "Total = Rp. " + str(total)

    def reset(self):
        global total
        global chris
        global split
        global kontol1
        global kontol2
        global kontol3
        global kontol4
        global nobar
        global jubar
        nobar = 0
        jubar = 0
        total = 0
        chris = ""
        kontol1 = ""
        kontol2 = ""
        kontol3 = ""
        kontol4 = ""
        self.splitresult1.text = ""
        self.splitresult2.text = ""
        self.splitresult3.text = ""
        self.splitresult4.text = ""
        self.sokong.text = ""

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("My.kv")

class MyApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    MyApp().run()