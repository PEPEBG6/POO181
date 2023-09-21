def findMajorityElement(nums):
    # Inicializar una variable para el elemento candidato y un contador
    candidate = None
    count = 0
    
    # Recorrer la lista de números
    for num in nums:
        # Si el contador es 0, asignar el número actual como candidato
        if count == 0:
            candidate = num
        
        # Si el número actual es igual al candidato, incrementar el contador
        if num == candidate:
            count += 1
        else:
            # Si el número actual no es igual al candidato, decrementar el contador
            count -= 1
    
    # Verificar si el candidato es el elemento mayoritario
    count = 0
    for num in nums:
        if num == candidate:
            count += 1
    
    if count > len(nums) / 2:
        return candidate
    else:
        return -1

if __name__ == '__main__':
    data = input("Ingrese los datos separados por comas: ")
    data = data.split(',')
    
    nums = []
    for item in data:
        try:
            num = int(item.strip())  # Eliminar espacios en blanco y convertir a entero
            nums.append(num)
        except ValueError:
            print(f"El valor '{item}' no es un número válido y será omitido.")
    
    if len(nums) > 0:
        result = findMajorityElement(nums)
        
        if result != -1:
            print('El elemento mayoritario es', result)
        else:
            print('El elemento mayoritario no existe')
    else:
        print('No se ingresaron datos válidos.')


