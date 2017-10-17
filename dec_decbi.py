# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:15:14 2017

@author: Leonardo Venancio
"""

# parte decimal de conversao decimal binario

def conversor_bi(valor, base):
    if base == '2':

        #parte fracionária
        frac = valor - float(int(valor))
        resultado_frac = '0.'
        while True:
            if frac*2 >= 1:
                resultado_frac += '1'
                frac = frac*2 - int(frac*2)
            elif frac*2 > 0 and frac*2 < 1:
                resultado_frac += '0'
                frac = frac*2
            elif frac == 0:
                if resultado_frac == '0.':
                    resultado_frac = ''
                return resultado_frac


    elif base == '10':

        #parte fracionária
        frac = ''
        i = str(valor).find('.')
        for a in range(len(str(valor))):
            if a > i:
                frac += str(valor)[a]
        print (frac)

        resultado_frac = 0

        while True:
            if frac != '':
                n = -1
                for i in enumerate(str(frac)):
                    resultado_frac += float(i[1])*(2**n)
                    n -= 1
            break

        return resultado_frac
        
print "\nDigite a conversao binaria que deseja para casas decimais\n"
base = str(input("Para base: "))
valor = float(input("Valor: "))
print(conversor_bi(valor, base))