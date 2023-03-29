# Dishing out DoS: How to Disable\\and Secure the Starlink User Terminal

This repository contains the code for the poster "Dishing out DoS: How to Disable\\and Secure the Starlink User Terminal", as submitted to WiSec 2023.
This work has been a collaboration between co-first authors Edd Salkield and Joshua Smailes, alongside Sebastian Köhler, Simon Birnbach, and Ivan Martinovic, all from the Systems Security Lab at the University of Oxford.

The scripts in `./code` allow the user to disable the Starlink modem through the sending of a malformed request, which crashes the command decoder and freezes the dish in its current state.
When combined with a request to stow the dish, this results in denial of service which persists until physically power-cycled.
The LaTeX source for the paper can also be found in the root of this repository.

We would like to thank Starlink for working with us through the vulnerability disclosure process.
The vulnerability was closed in December 2022 by patch `8c03f1b9-de75-404b-87fd-7986892cdacb.uterm.release`

We would further like to thank armasuisse S+T for giving us access to the hardware for this research.
## Building

To build the abstract pdf, run `make`.
The pdf can be continuously rebuild by `./watch`.
LaTeX temporary build files are put in `./out`, and can be cleaned with `make clean`.
