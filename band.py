import matplotlib as plt
from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSDOSPlotter, BSPlotter
bs_vasprun=Vasprun("vasprun.xml")
bs_data=bs_vasprun.get_band_structure(line_mode=True)
band_fig = BSDOSPlotter(bs_projection=None, vb_energy_range=2.0, fixed_cb_energy=2.0, bs_legend=None)
band_fig.get_plot(bs=bs_data)
plt.pyplot.savefig("band.pdf",format='pdf')
