#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
from array import array

def gcd(a,b):
        while(b != 0):
            m = a%b
            print("%d" %m)
            a = b
            b = m
            if(m == 0):
                return 0
                break
            elif(m == 1):
                return 1
                break
def modulo(x,y):
    result = x/y
    remainder = x -(y*result)
    return remainder

class  Bob(object):

    def Encryption_func(self,widget,entry,place):
        
        # Converting user text to corresponding integer
        arr = []
        for i in entry.get_text():
            arr.append(ord(i)) 
        print arr
        asci = ""
        intm = []

        # Integer to stream of hex representation
        for m in arr:
            power = pow(m,c.xx)
            modulus = modulo(power,c.mul)
            asci= asci + hex(modulus)

        # Main Encryptin algorithm applying
        for m in arr:
            intm.append(modulo(pow(m,c.xx),c.mul))
        print intm
        place.set_text(str(asci))
        print asci

    def __init__(self):

        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("destroy", lambda w: gtk.main_quit())
        window.set_title("RSA ENCRYPTION")

        # Outer vertical box inside the window 
        main_vbox = gtk.VBox(False, 5)
        main_vbox.set_border_width(10)
        window.add(main_vbox)
        
        # Encryption starting here
        encrypt_frame = gtk.Frame("Bob Window :")
        main_vbox.pack_start(encrypt_frame,True,True,0)

        encry_vbox = gtk.VBox(False, 0)
        encry_vbox.set_border_width(5)
        encrypt_frame.add(encry_vbox)

        encry_hbox = gtk.HBox(False, 0)
        encry_vbox.pack_start(encry_hbox, False, True, 5)

        encry_vbox_label = gtk.VBox(False,0)
        encry_hbox.pack_start(encry_vbox_label,True,True,5)

        label = gtk.Label("Enter Message :")
        label.set_alignment(0, 0.5)
        encry_vbox_label.pack_start(label, False, False, 0)

        encry_vbox_text = gtk.VBox(False,0)
        encry_hbox.pack_start(encry_vbox_text,True,True,5)

        entry = gtk.Entry()
        entry.set_text("Hello World")
        entry.select_region(0, len(entry.get_text()))
        encry_vbox_text.pack_start(entry, gtk.TRUE, gtk.TRUE, 0)
        entry.show()

        button_hbox = gtk.HBox(False, 0)
        encry_vbox.pack_start(button_hbox, False, True, 5)

        encrypt_label = gtk.Label("Encrypted Message :")
        encrypt_label.set_alignment(0, 0.5)#
        place_entry = gtk.Entry()
        button = gtk.Button("Encrypt")
        button.connect("clicked", self.Encryption_func ,entry,place_entry)
        button_hbox.pack_start(button, True, True, 5)

        entry_hbox = gtk.HBox(False, 0)
        encry_vbox.pack_start(entry_hbox, False, True, 5) 
        entry_hbox.pack_start(encrypt_label, False, False, 0)#
        entry_hbox.pack_start(place_entry, gtk.TRUE, gtk.TRUE, 0)
        place_entry.show()
 
        hbox1 = gtk.HBox(False, 0)
        main_vbox.pack_start(hbox1, False, True, 0)
        button = gtk.Button("Close")
        button.connect("clicked", lambda w: gtk.main_quit())
        hbox1.pack_start(button, True, True, 5)
        window.show_all()
        
    def main(self):
        gtk.main()   

class Cryptography:
    xx = 0
    d = 0
    mul = 0
    def get_value(self, widget, spin, spin2, label,tot_label,spin3,mul_inv):
        
        buf = "%d" % spin.get_value_as_int()
        buf2 = "%d" %spin2.get_value_as_int()
        self.mul = int(buf)*int(buf2)
        self.mul1 = (int(buf)-1)*(int(buf2)-1)
        put = str(self.mul)
        put1 = str(self.mul1)
        
        label.set_text(put)
        tot_label.set_text(put1)

        ex = "%d" % spin3.get_value_as_int()
        self.xx = int(ex)
        i = gcd(self.mul1,self.xx)
        if (i == 1):
            print("found ")
            for self.d in range(1,self.mul1):
                #print("%d" % d)
                if(((self.d*self.xx) % self.mul1) == 1):
                    mul_inv.set_text(str(self.d))
                    break
            
        else :
            spin3.set_value(3)
   
    def Bob_call(self,widget,entry):
        Bob().main()

    def Decryption_func(self,widget,bob_text,show):

        asci = bob_text.get_text()
        length = len(asci)
        byte = []
        stri =""

        # Separate different hex number from stream of hex digit
        for i in range(0,length):
            stri = ""
            if (asci[i] == '0' and asci[i+1] == 'x'):
                for a in range((i + 2),length):
                    if asci[a] == '0' and asci[a+1] == 'x':
                        p = a
                        break
                for j in range(i,p):
                    stri = stri + asci[j]

                byte.append(str(stri))
                
        byte.pop()
        for t in range(p,length):
            stri = stri + asci[t]
        byte.append(str(stri))
        print byte              
        # End of hex extraction from stream of hex

        # Hex to integer convert
        dint = []
        for i in byte:
            dint.append(int(i[2:-1],16))
        print dint

        # Applying algorithm to decrypt the encripted message
        mtoint = []
        for m in dint:
            p = pow(m,self.d)
            mtoint.append(modulo(p,self.mul))
        print mtoint

        # Ascii (integer) to corresponding character converting
        intoc = ""
        for a in mtoint:
            intoc += chr(a)
        show.set_text(intoc)
        print intoc

    
    def __init__(self):
        color = '#000000'
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("destroy", lambda w: gtk.main_quit())
        window.set_title("RSA ENCRYPTION")
        main_vbox = gtk.VBox(False, 5)
        main_vbox.set_border_width(10)
        window.add(main_vbox)
        
        
        frame = gtk.Frame("Alice Window :")
        main_vbox.pack_start(frame, True, True, 0)

        child_vbox = gtk.VBox(False,0)
        child_vbox.set_border_width(5)
        frame.add(child_vbox)

        key_frame = gtk.Frame("Key Generation :")
        child_vbox.pack_start(key_frame,True,True,0)

        vbox = gtk.VBox(False, 0)
        vbox.set_border_width(5)
        key_frame.add(vbox)
  
        hbox = gtk.HBox(False, 0)
        vbox.pack_start(hbox, False, True, 5)
  
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)
  
        label = gtk.Label("First Prime(p):")
        label.set_alignment(0, 0.5)
        vbox2.pack_start(label, False, False, 0)
  
        adj = gtk.Adjustment(1213, 0, 100000, 0.5, 100, 0)
        spinner1 = gtk.SpinButton(adj, 1.0, 2)
        spinner1.set_wrap(True)
        spinner1.set_size_request(100, -1)
        vbox2.pack_start(spinner1, False, False, 0)
  
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)
  
        label = gtk.Label("Second Prime(q):")
        label.set_alignment(0, 0.5)
        vbox2.pack_start(label, False, True, 0)
  
        adj = gtk.Adjustment(2113, 0, 100000, 0.5, 100.0, 0)
        spinner2 = gtk.SpinButton(adj, 1.0, 2)
        spinner2.set_wrap(True)
        vbox2.pack_start(spinner2, False, True, 0)
  
        
        modulus_lebel = gtk.Label("Modulus\n[n = p*q]:")
        mod_val_level = gtk.Label("")
        totient_lebel = gtk.Label("Totient\n[t=(p-1)*(q-1)]:")
        tot_val_level = gtk.Label("")

        exponent_lebel = gtk.Label("Exponent(e) :")
        adj = gtk.Adjustment(35489, 0, 100000.0, 0.5, 100.0, 0.0)
        spinner3 = gtk.SpinButton(adj, 1.0, 2)
        spinner3.set_wrap(True)
        mul_inverse_lebel = gtk.Label("Mul_Inverse(d):")
        mul_in_val_level = gtk.Label("")

        hbox = gtk.HBox(False, 0)
        vbox.pack_start(hbox, False, True, 5)
        button = gtk.Button("Genarate")
        button.connect("clicked", self.get_value, spinner1, spinner2,
                       mod_val_level,tot_val_level,spinner3,mul_in_val_level)
        hbox.pack_start(button, True, True, 5)
        
        # Modulus value assigning
        hbox = gtk.HBox(False,0)
        vbox.pack_start(hbox, False, True, 5)
        hbox.pack_start(modulus_lebel,True,True,0)
        hbox.pack_start(mod_val_level, True, True, 0)
        mod_val_level.set_text("0")

        # Totiont value determining
        hbox.pack_start(totient_lebel,True,True,0)
        hbox.pack_start(tot_val_level,True,True,0)
        tot_val_level.set_text("0") 

        # Place to enter private key exponent (e)
        hbox = gtk.HBox(False,0)
        vbox.pack_start(hbox, False, True, 5)
        hbox.pack_start(exponent_lebel,True,True,0)
        hbox.pack_start(spinner3,False,True,0)

        # Multiplicative inverse (d) deriving
        hbox.pack_start(mul_inverse_lebel,True,True,0)
        hbox.pack_start(mul_in_val_level,True,True,0)
        mul_in_val_level.set_text("0")

        # Button to connect with Bob
        bob_frame = gtk.Frame("Key Generation :")
        child_vbox.pack_start(bob_frame,True,True,0)

        bob_vbox = gtk.VBox(False, 0)
        bob_vbox.set_border_width(5)
        bob_frame.add(bob_vbox)

        ask_bob = gtk.HBox(False, 0)
        bob_vbox.pack_start(ask_bob, False, True, 5)
        button = gtk.Button("Click to connect with Bob")
        button.connect("clicked", self.Bob_call ,"bob")
        ask_bob.pack_start(button, True, True, 5)

        # Decryption starting here
        decrypt_frame = gtk.Frame("Decryption :")
        child_vbox.pack_start(decrypt_frame,True,True,0)

        decry_vbox = gtk.VBox(False, 0)
        decry_vbox.set_border_width(5)
        decrypt_frame.add(decry_vbox)

        bob_hbox = gtk.HBox(False, 0)   # Place to paste encrypted message
        decry_vbox.pack_start(bob_hbox,False,True,5)
        bob_vbox = gtk.VBox(False,0)
        bob_hbox.pack_start(bob_vbox,True,True,5)

        bob_label = gtk.Label("Enter Encrypted \n Message :") 
        bob_label.set_alignment(0, 0.5)
        bob_vbox.pack_start(bob_label, False, False, 0)

        bob_vbox_text = gtk.VBox(False,0)
        bob_hbox.pack_start(bob_vbox_text,True,True,5)

        bob_entry = gtk.Entry()
        bob_vbox_text.pack_start(bob_entry, gtk.TRUE, gtk.TRUE, 0)
        bob_entry.show()

        decrypt_label = gtk.Label("") 
        decrypt_label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#008000'))
        button_hbox = gtk.HBox(False, 0)
        decry_vbox.pack_start(button_hbox, False, True, 5)
        button = gtk.Button("Decrypt")###       ###        ###
        button.connect("clicked", self.Decryption_func, bob_entry,decrypt_label)
        button_hbox.pack_start(button, True, True, 5)

        decry_hbox = gtk.HBox(False, 0)
        decry_vbox.pack_start(decry_hbox, False, True, 5)

        decry_vbox_label = gtk.VBox(False,0)
        decry_hbox.pack_start(decry_vbox_label,True,True,5)

        label = gtk.Label("Decrypted Message :")
        label.set_alignment(0, 0.5)
        decry_vbox_label.pack_start(label, False, False, 0)

        decry_vbox_text = gtk.VBox(False,0)
        decry_hbox.pack_start(decry_vbox_text,True,True,5)
        ###         ###         ###
        decrypt_label.set_alignment(0, 0.5)
        decry_vbox_text.pack_start(decrypt_label, False, False, 0)
        
        hbox1 = gtk.HBox(False, 0)
        main_vbox.pack_start(hbox1, False, True, 0)
        button = gtk.Button("Close")
        button.connect("clicked", lambda w: gtk.main_quit())
        hbox1.pack_start(button, True, True, 5)
        window.show_all()
    
    def main(self):
        gtk.main()

if __name__ == "__main__":
    c = Cryptography()
    c.main()