Pinouts
=======

:lang: en
:slug: tech/pinout

.. contents:: Table of Contents

Cartridge
---------

When inserted into the console, pins A1-20 are on the back side and pins B1-20 are on the front, ordered from the left of the console to the right.

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
     * |PWR|
     * VPP
     * B1
     * |PWR|
     * VCC
   * * A2
     * |OUT|
     * CLKOUT
     * B2
     * |IN|
     * /RST
   * * A3
     * |IO|
     * D7
     * B3
     * |OUT|
     * A15
   * * A4
     * |IO|
     * D6
     * B4
     * |OUT|
     * A14
   * * A5
     * |IO|
     * D5
     * B5
     * |OUT|
     * A13
   * * A6
     * |IO|
     * D4
     * B6
     * |OUT|
     * A12
   * * A7
     * |IO|
     * D3
     * B7
     * |OUT|
     * A11
   * * A8
     * |IO|
     * D2
     * B8
     * |OUT|
     * A10
   * * A9
     * |IO|
     * D1
     * B9
     * |OUT|
     * A9
   * * A10
     * |IO|
     * D0
     * B10
     * |OUT|
     * A8
   * * A11
     * |IN|
     * INT2
     * B11
     * |OUT|
     * A7
   * * A12
     * |IN|
     * INT0
     * B12
     * |OUT|
     * A6
   * * A13
     * |OUT|
     * /RD
     * B13
     * |OUT|
     * A5
   * * A14
     * |OUT|
     * /WR
     * B14
     * |OUT|
     * A4
   * * A15
     * |OUT|
     * PC7
     * B15
     * |OUT|
     * A3
   * * A16
     * |OUT|
     * PC6
     * B16
     * |OUT|
     * A2
   * * A17
     * |OUT|
     * PC5
     * B17
     * |OUT|
     * A1
   * * A18
     * |IO|
     * /SCK
     * B18
     * |OUT|
     * A0
   * * A19
     * |IN|
     * SI
     * B19
     * |OUT|
     * SO
   * * A20
     * |GND|
     * Gnd
     * B20
     * |GND|
     * Gnd

Signal descriptions
```````````````````

* VCC: +5V power from console
* VPP: +5V power from console, or EPROM programming voltage from programmer
* Gnd: ground
* CLKOUT: clock output from console (XTAL/2, 2 MHz?)
* /RST: reset input to console
* Data bus

  * D0-7: bidirectional data pins
  * A0-15: address outputs from console
  * /RD: read strobe output from console
  * /WR: write strobe output from console

* PC5-7: banking outputs from console (probably configurable as bidirectional)
* INT0, INT2: interrupt inputs to console
* Serial

  * /SCK: bidirectional serial clock
  * SI: serial data input to console
  * SO: serial data output from console

.. include:: ../../epilog.rsti
