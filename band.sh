#!/bin/bash
for i in {1..144..1} ; do
	cd ${i}
	sed -i 's/GAMMA/\\Gamma/g' KPOINTS
	sed -i 's/&//g' vasprun.xml
	python ../band.py
#	mv band.pdf ${i}.pdf
	cd ..
done
qpdf --empty --pages */band.pdf -- bs_cof.pdf
