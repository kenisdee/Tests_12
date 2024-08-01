import unittest
from tests_12_1 import RunnerTest
from tests_12_2 import TournamentTest

# Декоратор для пропуска тестов
def skip_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return method(self, *args, **kwargs)
    return wrapper

# Добавляем атрибут is_frozen в классы
RunnerTest.is_frozen = False
TournamentTest.is_frozen = True

# Применяем декоратор к методам классов
for name, method in vars(RunnerTest).items():
    if callable(method) and not name.startswith('__') and not name.startswith('setUp') and not name.startswith('tearDown'):
        setattr(RunnerTest, name, skip_frozen(method))

for name, method in vars(TournamentTest).items():
    if callable(method) and not name.startswith('__') and not name.startswith('setUp') and not name.startswith('tearDown'):
        setattr(TournamentTest, name, skip_frozen(method))

# Создаем объект TestSuite
test_suite = unittest.TestSuite()

# Добавляем тесты из RunnerTest и TournamentTest в TestSuite
test_suite.addTest(unittest.makeSuite(RunnerTest))
test_suite.addTest(unittest.makeSuite(TournamentTest))

# Создаем объект TextTestRunner с аргументом verbosity=2
runner = unittest.TextTestRunner(verbosity=2)

# Запускаем TestSuite
runner.run(test_suite)