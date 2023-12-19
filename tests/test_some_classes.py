import pytest
from src.some_classes import Animal, Cat


class TestAnimal:
    def test_init(self):
        animal = Animal("Human", "Homo sapien", "Hominidae")
        assert animal.name == "Human"
        assert animal.specie == "Homo sapien"
        assert animal.family == "Hominidae"
        assert animal.kingdom == "Animalia"

    def test_make_sound(self, capsys):
        animal = Animal("Human", "Homo sapien", "Hominidae")
        animal.make_sound()
        captured = capsys.readouterr()
        assert captured.out == "Grrrr...\n"

    def test_repr(self):
        animal = Animal("Human", "Homo sapien", "Hominidae")
        assert animal.__repr__() == "Homo sapien is a Hominidae and belongs to the Animalia kingdom."


class TestCat:
    def test_init(self):
        cat = Cat("Cat", "Felis catus", "Felidae")
        assert cat.name == "Cat"
        assert cat.specie == "Felis catus"
        assert cat.family == "Felidae"
        assert cat.kingdom == "Animalia"

    def test_make_sound(self, capsys):
        cat = Cat("Cat", "Felis catus", "Felidae")
        cat.make_sound()
        captured = capsys.readouterr()
        assert captured.out == "Meow!\n"

    def test_repr(self):
        cat = Cat("Cat", "Felis catus", "Felidae")
        assert cat.__repr__() == "Felis catus is a Felidae and belongs to the Animalia kingdom."