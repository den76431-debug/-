class Book:
    """
    Класс, описывающий книгу.

    """

    def _init_(self, title: str, author: str, year: int):

        if year < 0 or year > 2024:
            raise ValueError("Год издания должен быть положительным и не превышать текущий год.")

        self.title = title
        self.author = author
        self.year = year

    def get_age(self) -> int:

        from datetime import datetime
        current_year = datetime.now().year
        return current_year - self.year

    def is_old(self, threshold: int = 50) -> bool:

        return self.get_age() > threshold


class Tree:
    """
    Класс, описывающий дерево.

    """

    def init(self, species: str, age: int, height: float):

        if age < 0 or height < 0:
            raise ValueError("Возраст и высота не могут быть отрицательными.")

        self.species = species
        self.age = age
        self.height = height

    def grow(self, years: int = 1) -> None:
        """
        Увеличивает возраст дерева на указанное количество лет и корректирует высоту.

        :param years: Количество лет, на которое дерево растет (по умолчанию 1 год).

        """
        self.age += years
        self.height += years * 0.3  # Пример: дерево растет на 0.3 метра в год

    def can_be_cut(self, min_age: int = 30) -> bool:
        """
        Проверяет, можно ли спиливать дерево (достигло ли оно минимального возраста).

        """
        return self.age >= min_age

    class SocialNetwork:
        """
        Класс, описывающий социальную сеть.

        """

        def __init__(self):
            self.name = None

        def init(self, name: str, users: int, founded_year: int):
            """
            Инициализация объекта "Социальная сеть".

            """
            if users < 0:
                raise ValueError("Количество пользователей не может быть отрицательным.")
            if founded_year > 2024:
                raise ValueError("Год основания не может быть в будущем.")

            self.name = name
            self.users = users
            self.founded_year = founded_year

        def add_users(self, new_users: int) -> None:
            """
            Добавляет новых пользователей в социальную сеть.

            """
            if new_users < 0:
                raise ValueError("Количество новых пользователей не может быть отрицательным.")
            self.users += new_users

        def years_since_foundation(self) -> int:

            from datetime import datetime
            current_year = datetime.now().year
            return current_year - self.founded_year

        if __name__ == "_main_":
            import doctest
            doctest.testmod(verbose=True)
