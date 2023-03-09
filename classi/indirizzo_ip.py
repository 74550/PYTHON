import math

class IPaddress():
    def _init_(self, ip_rete, sbm):
        self.ip_rete = ip_rete
        self.sbm_b = sbm
        self.sbm = (32 - int(sbm[1:]))
        self.ip_rete_bin = self.decToBin(self.ip_rete)
        self.ip_brodcast_bin = self.ipBrodcast()
        self.ip_brodcast =self.binToDec(self.ip_brodcast_bin)

    def deliteDot(self, v):
        l = v.split(".")
        return [i for i in l]

    def decToBin(self, ip_decimal_string):
        temp = self.deliteDot(ip_decimal_string)
        s = ""

        for i in temp:
            s += bin(int(i))[2:] + "."

        temp = self.deliteDot(s[:-1])

        s = ""

        for i in temp:
            s += "0" * (8 - len(i)) + i + "."

        return s[:-1]

    def setDot(self, x):
        s = ""

        for i in range(len(x)):
            if i == 7 or i == 15 or i == 23:
                s += x[i] + "."
            else:
                s += x[i]
        return s

    def ipBrodcast(self):
        l = self.deliteDot(self.ip_rete_bin)
        #SB: print(l)

        s = ""
        for i in l:
            s += i

        s = s[:len(s) - self.sbm] + ("1" * self.sbm)
        #SB: print(s)
        s = self.setDot(s)
        return s

    def convertBinToDec(self, binary):
        decimal, i = 0, 0

        while (binary != 0):
            decimal = decimal + (binary % 10) * pow(2, i)
            binary = binary // 10
            i += 1

        return decimal

    def binToDec(self, ip_binary_string):
        l = self.deliteDot(ip_binary_string)
        s = ""
        for i in l:
            s += str(self.convertBinToDec(int(i))) + "."
        return s[:-1]

    def toString(self):
        return "ip_rete bin: " + self.ip_rete_bin + "\n" + "ip_brodcast bin: " + self.ip_brodcast_bin + "\n" + "ip_rete -> " + self.ip_rete + " " + self.sbm_b + "\n" + "ip_brodcast -> " + self.ip_brodcast + "\n"

class Subnets(IPaddress):
    def _init_(self, ip_rete, sbm, n_sottoreti):
        self.ip_rete = ip_rete
        self. n_sottoreti = n_sottoreti
        self.sbm = "/" + str(int(sbm[1:]) + math.ceil(math.log2(n_sottoreti)))

    def toString(self):
        ip = self.ip_rete
        s = ""

        for i in range(self.n_sottoreti):
            s += "\n" + IPaddress(ip, self.sbm).toString()
            ip = IPaddress(ip, self.sbm).ip_brodcast

            l = self.deliteDot(ip)
            ip = ""
            if int(l[-1]) >= 255:
                l[-1] = 0
                l[-2] = int(l[-2]) + 1

            for i in l:
                ip += str(i) + "."
            ip = ip[:-1]

        return s

def main():
    ip = IPaddress("10.0.0.0", "/16")

    print("RETE PRINCIPALE:\n")
    print(ip.toString())
    subnett = Subnets("10.0.0.0", "/16", 7)
    print("\nSOTTORETI:")
    print(subnett.toString())

if _name_ == "_main_":
    main()