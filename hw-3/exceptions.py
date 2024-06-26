"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    return 'Нет топлева'
    

class NotEnoughFuel(Exception):
    return 'Недостаточно топлива'
    

class CargoOverload(Exception):
    return 'Перегрузка'

