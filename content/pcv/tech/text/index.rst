Text
====

:lang: en
:slug: tech/text

Encoding
--------

.. figure:: text/font.png
   :alt: Game Pokekon font
   :width: 288px

   Game Pokekon font

.. figure:: text/encoding.svg
   :alt: Text encoding table

   Text encoding table

The built-in text routines output characters encoded in one of three blocks:

* $00..$3F: 5x7 characters from the ASCII/JIS X 0201 range $20..$5F
* $40..$63: 5x5 characters, digits followed immediately by capital letters
* $64..$FF: user-defined characters from a table pointed to by $4005
