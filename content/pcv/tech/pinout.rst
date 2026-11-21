Pinouts
=======

:lang: en
:slug: tech/pinout

.. contents:: Table of Contents

Cartridge
---------

Note the similarity of the pin ordering to 28-pin EPROMs.

.. list-table::
   :header-rows: 1
   :widths: auto

   * * #
     * Dir
     * Use
     * #
     * Dir
     * Use
   * * A1
     * |OUT|
     * A14
     * B1
     * |OUT|
     * A13
   * * A2
     * |OUT|
     * A12
     * B2
     * |OUT|
     * A8
   * * A3
     * |OUT|
     * A7
     * B3
     * |OUT|
     * A9
   * * A4
     * |OUT|
     * A6
     * B4
     * |OUT|
     * A11
   * * A5
     * |OUT|
     * A5
     * B5
     * |OUT|
     * A15
   * * A6
     * |OUT|
     * A4
     * B6
     * |OUT|
     * A10
   * * A7
     * |OUT|
     * A3
     * B7
     * |OUT|
     * /RD
   * * A8
     * |OUT|
     * A2
     * B8
     * |IO|
     * D7
   * * A9
     * |OUT|
     * A1
     * B9
     * |IO|
     * D6
   * * A10
     * |OUT|
     * A0
     * B10
     * |IO|
     * D5
   * * A11
     * |IO|
     * D0
     * B11
     * |IO|
     * D4
   * * A12
     * |IO|
     * D1
     * B12
     * |IO|
     * D3
   * * A13
     * |IO|
     * D2
     * B13
     * |IO|
     * /SCK
   * * A14
     * |GND|
     * Gnd
     * B14
     * |IN|
     * SI
   * * A15
     * |PWR|
     * VCC
     * B15
     * |OUT|
     * SO

Signal descriptions
```````````````````

* VCC: +5V power from console
* Gnd: ground
* Data bus

  * D0-7: bidirectional data pins
  * A0-15: address outputs from console
  * /RD: read strobe output from console

* Serial

  * /SCK: bidirectional serial clock
  * SI: serial data input to console
  * SO: serial data output from console

.. include:: ../../epilog.rsti
