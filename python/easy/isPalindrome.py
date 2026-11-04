class Solution:
    def isPalindrome(self, x: int) -> bool:
        q = str(x)  
        # Convierte el número entero a una cadena de texto (string) para poder manipularlo
        return (q == q[::-1])  
        # Compara el string original con su reverso ([::-1]). Retorna True si son idénticos, False si no.
