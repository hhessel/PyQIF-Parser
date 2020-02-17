# PyQIF-Parser

A(nother) Python-based Parser for Quicken / Lexware Finance Manager QIF files.

## Why

There are already some Python-based parsers for QIF files, however they had issues with the file my (German) Lexware Financial Manager 2019 is spitting out. 

What I basically need is a tool to convert a QIF file into a pandas dataframe, so this is my main motivation. 

## Resources

* https://github.com/jemmyw/Qif/blob/master/QIF_references for a QIF reference

## Proof of Concept

I hacked together a proof of concept, see it here: https://gist.github.com/UweZiegenhagen/08885a0c08a6f23bd2c3855106a1522c

It's pretty ugly but parses my QIF file w/o errors, so it will be the basis for this project.

