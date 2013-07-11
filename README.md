dapbook
=======

Examples of integrated [Pydap](http://www.pydap.org/) (OPeNDAP server) with [WMS](http://www.pydap.org/responses.html#web-map-service) into the [IPython Notebook](http://ipython.org/notebook.html). Check out [the slides](https://github.com/pfctdayelise/dapbook/raw/master/slides.pdf) (also [on Slideshare](http://www.slideshare.net/pfctdayelise/slides-24141056)) for a more verbose explanation.

* [A simple example of Pydap WMS data integrated with OpenStreetMap/OpenLayers](https://rawgithub.com/pfctdayelise/dapbook/master/example-openlayers.html).
* [Same data with OpenStreetMap/Leaflet](https://rawgithub.com/pfctdayelise/dapbook/master/example-leaflet.html).
* [Both maps displayed in the IPython notebook](http://nbviewer.ipython.org/urls/raw.github.com/pfctdayelise/dapbook/master/embeddingmap-simple.ipynb).

`dapbook.py` and `template.html` can be used together to easily embed map data from Pydap WMS servers into your IPython notebooks. They can read from a remote server or local.


Dependencies:

* all (to run notebooks) - ipython, tornado, pyzmq
* readingdatafrompydap.ipynb - pydap only
* embeddingmap-simple.ipynb - can be run without any further dependencies (as in nbviewer above)
* embeddingmap-dynamic.ipynb - requires pydap, pydap.handlers.netcdf, pydap.responses.wms


Pydap uses Genshi which is why my template is in Genshi. If you don't intend to run a local Pydap server and you don't want to install it, you could just install Genshi. Or your favourite templating library, and make a template for that.

The data in my examples is a sample grid available from the Bureau of Meteorology. See the [Australian Digital Forecast Database](http://www.bom.gov.au/catalogue/data-feeds.shtml) for more information (and to freely download).

Inspired to make your own WMS-ish app and do the map tile generation yourself? Check out [leafvis](https://github.com/nfaggian/leafvis) :)
