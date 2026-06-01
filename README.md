# Shapes

A small project I built to practise object-oriented programming in Python, using a set of geometric shapes.

## What this is

This is a learning exercise — the focus is on how the code is structured.
There's an abstract Shape class at the top, and each specific shape (triangle, rectangle, square) builds on it and works out its own area and perimeter.

## Concepts it demonstrates

- **Abstract base classes** — `Shape` uses `ABC` and `@abstractmethod` to require every
  subclass to implement `area` and `perimeter`.
- **Inheritance with `super()`** — each shape calls the parent's `__init__` before setting
  its own dimensions.
- **Properties** — `is_large` lives on the base class and works for every shape, since it
  builds on the shared `area` method.
- **Polymorphism** — the demo loop treats every shape the same way, because they all share
  the same interface.

## The shapes

- `Shape` — the abstract parent. Defines the interface and the `is_large` check.
- `Triangle` — a right triangle defined by its two legs. Its legs act as the base and
  height for the area, and the hypotenuse is worked out from them for the perimeter.
- `Rectangle` — defined by width and length.
- `Square` — defined by a single side.

## Running it

```bash
python shapes.py
```

This runs a short demo that creates a few shapes and prints each one's area, perimeter,
and whether it counts as large.

## Note

`is_large` returns `True` when a shape's area is greater than 100. The threshold is
arbitrary — it's there to show a property on the base class that depends on a method the
subclasses provide.
