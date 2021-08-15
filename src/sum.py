"""Programa de prueba."""
import sys


def my_sum(a, b):
    """Suma dos numeros."""
    print(int(a) + int(b))


my_sum(sys.argv[1], sys.argv[2])