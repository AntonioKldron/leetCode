class Solution:
    def romanToInt(self, s: str) -> int:
        valores = {  
            # Diccionario que mapea cada letra romana con su valor numérico correspondiente
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        nums = reversed(s)  
        # Invierte el orden del string para empezar a leerlo desde el final (derecha a izquierda)
        total = 0  
        # Variable acumuladora para el resultado numérico final
        anteriro = 0  
        # Variable auxiliar para recordar el valor del símbolo anterior procesado (Nota: tiene un pequeño typo en tu código original "anteriro")
        
        for num in nums:  
            # Bucle que recorre cada carácter romano ya invertido
            actual = valores[num]  
            # Obtiene el valor numérico entero del símbolo actual
            
            if actual < anteriro:  
                # Si el valor actual es menor que el anterior (ej. 'I' antes de 'V'), aplica una resta
                total -= actual
            else:  
                # De lo contrario, se trata de una suma normal
                total += actual
                
            anteriro = actual  
            # Actualiza la variable 'anteriro' con el valor actual para la siguiente iteración
            
        return total  
        # Retorna la suma/resta total convertida a entero
