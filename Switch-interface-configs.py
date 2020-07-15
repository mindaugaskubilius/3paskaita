class interface:

    def __init__(self, interface_name, interface_description):
        self.interface_name = str(interface_name)
        self.interface_description = str(interface_description)
        s = 1

    def funkcija1(self):
        des = self.interface_description
        nam = self.interface_name
        #print("\n" + "set interfaces", self.interface_name, "description", self.interface_description)
        #print("set interfaces", self.interface_name, "aggregated-ether-options link-speed 10g")
        #print("set interfaces", self.interface_name, "aggregated-ether-options  lacp active")
        #print("set interfaces", self.interface_name, "aggregated-ether-options lacp force-up")
        #print("set interfaces", self.interface_name, "unit 0 family ethernet-switching interface-mode access" + "\n")
        c = int(des[5:])
        b = int(nam[2:])
        #veliau si kintamaji lokacija naudosiu cikle
        lokacija=str(des[:5])

        client_list = [ des[5], des[6], des[7]]

        print("is paduodamo serverio description'o suformuojame sarasa: ", client_list)
        trecias_narys_sarase = client_list[2]
        antras_narys_sarase = client_list[1]
        pirmas_narys_sarase = client_list[0]
        int(trecias_narys_sarase)
        int(antras_narys_sarase)
        int(pirmas_narys_sarase)
        print("pirmas_narys_sarase:", pirmas_narys_sarase)
        print("antras_narys_sarase:", antras_narys_sarase)
        print("trecias_narys_sarase:", trecias_narys_sarase)
        print('\n')
        print('isparsintas pirmo dedikuoto interface numeris kaip sveikas skaicius:', b)
        print('isparsintas pirmo dedikuoto ID is description kaip sveikas skaicius:', c, '\n' )
        print('funkcijoje isgautas reiksmes per sarasus prasuku per 12 iteraciju cikla, taip sudedamas atitinkamas reiksmes dvylikai nodeu:', '\n')

        iteracija = 1
        while iteracija <=12:
            client_list2 = [str(b), str(c) ]

            if len(client_list2[1]) <= 1:
                temp_str=client_list2[1]
                client_list2[1]=lokacija+"00"+temp_str
            if len(client_list2[1]) <= 2:
                temp_str=client_list2[1]
                client_list2[1]=lokacija+"0"+temp_str
            if len(client_list2[1]) <=3:
                temp_str = client_list2[1]
                client_list2[1] = lokacija + temp_str
            print("set interfaces", "ae"+client_list2[0], "description", client_list2[1])  # self.interface_description)
            print("set interfaces", "ae"+client_list2[0], "aggregated-ether-options link-speed 10g")
            print("set interfaces", "ae"+client_list2[0], "aggregated-ether-options  lacp active")
            print("set interfaces", "ae"+client_list2[0], "aggregated-ether-options lacp force-up")
            print("set interfaces", "ae"+client_list2[0], "unit 0 family ethernet-switching interface-mode access" + "\n")
            iteracija = iteracija + 1
            b = b + 1
            c = c + 1

interface1 = interface(input("Nurodykite startini interface'a : "), input("Nurodykite startini serverio description'a: "))
interface1.funkcija1()
