Pinouts
=======

:lang: en
:slug: tech/pinout

.. contents:: Table of Contents

Cartridge
---------

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
     * +6V
     * B1
     * |OUT|
     * CLK
   * * A2
     * |PWR|
     * +6V
     * B2
     * |OUT|
     * PD1
   * * A3
     * |IN|
     * PE1
     * B3
     * |OUT|
     * PD2
   * * A4
     * |IN|
     * PE2
     * B4
     * |OUT|
     * PD3
   * * A5
     * |IN|
     * PE3
     * B5
     * |OUT|
     * PD4
   * * A6
     * |IN|
     * PE4
     * B6
     * |IN|
     * /GE
   * * A7
     * |IN|
     * PE
     * B7
     * |OUT|
     * /GX
   * * A8
     * |IN|
     * /SB
     * B8
     * |OUT|
     * /GP
   * * A9
     * |IN|
     * /S1
     * B9
     * |OUT|
     * /K7
   * * A10
     * |IN|
     * /SC
     * B10
     * |OUT|
     * /K6
   * * A11
     * |IN|
     * /S2
     * B11
     * |OUT|
     * /K5
   * * A12
     * |IN|
     * /SA
     * B12
     * |OUT|
     * /K4
   * * A13
     * |IN|
     * VIDEO
     * B13
     * |OUT|
     * /K3
   * * A14
     * |IN|
     * B-Y
     * B14
     * |OUT|
     * /K2
   * * A15
     * |IN|
     * REF
     * B15
     * |OUT|
     * /K1
   * * A16
     * |IN|
     * R-Y
     * B16
     * |GND|
     * Gnd
   * * A17
     * |IN|
     * SOUND
     * B17
     * |GND|
     * Gnd
   * * A18
     * |IN|
     * CHROMA
     * B18
     * |GND|
     * Gnd

Signal descriptions
```````````````````

* VDD: +6V power from console
* Gnd: ground
* CLK: 3.579545 Mhz clock from console (NTSC color burst frequency)
* `Key matrix`_:

  * /S1, /S2, /SA, /SB, /SC: column input to console
  * /K1-7: row output from console

* Paddle:

  * PD1-4: analog paddle output from console
  * PE: tied to VDD if any paddle is used
  * PE1-4: tied to VDD if the corresponding paddle is used

* Gun:

  * /GE: unclear, probably tied to Gnd if the gun is used
  * /GP: unclear, probably trigger output from console
  * /GX: unclear, probably photodiode output from console

* AV outputs:

  * VIDEO: luma/sync input to console, +1.5 to +3V
  * B-Y: color input to console, 0 to +2V
  * R-Y: color input to console, 0 to +2V
  * CHROMA: color input to console, 0 to +5V
  * REF: fixed reference input to console, +1V
  * SOUND: sound input to console

Key Matrix
----------

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * *
     * /SB
     * /S1
     * /SC
     * /S2
     * /SA
   * * /K1
     * Start
     *
     *
     *
     * Slide 1 [#jr]_
   * * /K2
     * J2 Right [#jr]_
     * J1 Right
     *
     *
     * Slide 2 [#jr]_
   * * /K3
     * J2 Left [#jr]_
     * J1 Left
     *
     *
     * Slide 3 [#jr]_
   * * /K4
     * Select
     *
     *
     *
     * Slide 4 [#jr]_
   * * /K5
     * Option [#jr]_
     *
     *
     *
     * Slide 5 [#jr]_
   * * /K6
     *
     *
     * Btn 4
     * Btn 2
     *
   * * /K7
     *
     *
     * Btn 3
     * Btn 1
     *

.. [#jr] Not present on Cassette Vision Jr.

.. include:: ../../epilog.rsti
