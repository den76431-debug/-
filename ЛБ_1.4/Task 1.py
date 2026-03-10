


class Vehicle:
    """
    Базовый класс, транспортное средство.
    """

    def __init__(self, brand: str, model: str, year: int):
        self.brand: str = brand
        self.model: str = model
        self.year: int = year
        # Инкапсуляция: серийный номер скрыт, так как это внутренняя
        # техническая информация, которую не стоит менять напрямую.
        self.__serial_number: str = "VIN-12345-BASE"

    def get_info(self) -> str:
        """
        Возвращает информацию о Т.С.
        """
        return f"{self.brand} {self.model} ({self.year})"

    def __str__(self) -> str:
        """Пользовательское строковое представление объекта."""
        return f"Транспорт: {self.brand} {self.model}"

    def __repr__(self) -> str:
        """Официальное строковое представление."""
        return f"Vehicle(brand='{self.brand}', model='{self.model}', year={self.year})"


class ElectricCar(Vehicle):
    """
    Дочерний класс, электромобиль.
    """

    def __init__(self, brand: str, model: str, year: int, battery_capacity: int):
        """
        Расширяем конструктор базового класса, добавляя емкость батареи.
        """
        # Вызов констрктора родительского класса
        super().__init__(brand, model, year)
        self.battery_capacity: int = battery_capacity

    def get_info(self) -> str:
        """
        Перегрузка метода get_info.

        Для электромобиля емкость аккумулятора это ключевая характеристика.
        """
        base_info = super().get_info()
        return f"{base_info}, Батарея: {self.battery_capacity} кВт*ч"

    def charge(self) -> None:
        """Метод для имитации процесса зарядки."""
        print(f"{self.brand} {self.model} заряжается...")

    def __str__(self) -> str:
        """Перегружаем магический метод str для уточнения типа транспорта."""
        return f"Электромобиль: {self.brand} {self.model}"

    def __repr__(self) -> str:
        return f"ElectricCar(brand='{self.brand}', model='{self.model}', year={self.year}, battery={self.battery_capacity})"
