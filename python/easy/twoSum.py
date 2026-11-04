class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        vistos = {}  
        # Diccionario (HashMap) para guardar los números ya recorridos con su índice: {valor: índice}
        
        for i, num in enumerate(nums):  
            # Bucle que recorre la lista obteniendo el índice (i) y el valor actual (num)
            complemento = target - num  
            # Calcula cuánto falta para llegar al objetivo (target)
            
            if complemento in vistos:  
                # Revisa si ese complemento ya fue guardado previamente en el diccionario
                return [vistos[complemento], i]  
                # Si existe, retorna el índice del complemento y el índice actual (i)
            
            vistos[num] = i  
            # Si aún no está, guarda el número actual y su posición en el diccionario
            
        return []  
        # Por seguridad, retorna una lista vacía si no encuentra ninguna pareja