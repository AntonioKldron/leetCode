class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:  # Verifica si la lista de strings está vacía; si es así, retorna un string vacío
            return ""
            
        strs.sort()  # Ordena alfabéticamente la lista de cadenas (los elementos más diferentes quedarán al principio y al final)
            
        first = strs[0]  # Guarda el primer elemento de la lista ordenada (el menor alfabéticamente)
        last = strs[-1]  # Guarda el último elemento de la lista ordenada (el mayor alfabéticamente)
            
        for i in range(min(len(first), len(last))):  # Recorre los índices desde 0 hasta la longitud del string más corto entre el primero y el último
            if first[i] != last[i]:  # Si un carácter difiere entre el primero y el último...
                return first[:i]  # ...corta y retorna todo el prefijo acumulado hasta antes de esa diferencia
                
        return first[:min(len(first), len(last))]  # Si todo el string corto coincide con el largo, retorna el string corto completo

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:  # Si la lista está vacía, retorna un string vacío de inmediato
            return ""
            
        pref = strs[0]  # Toma el primer elemento de la lista como nuestro prefijo inicial de referencia
        
        for s in strs[1:]:  # Recorre el resto de las palabras de la lista a partir del segundo elemento
            while not s.startswith(pref):  # Mientras el string actual (s) NO comience con el prefijo actual (pref)...
                pref = pref[:-1]  # ...recorta la última letra del prefijo para hacerlo más corto
                if not pref:  # Si el prefijo se queda completamente vacío en el proceso...
                    return ""  # ...significa que no hay ningún prefijo en común y retorna un string vacío
                    
        return pref  # Retorna el prefijo común final después de validarlo contra todas las palabras