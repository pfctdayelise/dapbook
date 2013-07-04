import os
from genshi.template import TemplateLoader
from IPython.display import HTML

loader = TemplateLoader(os.getcwd())


def getSrcAsBase64(html):
    htmlEncoded = html.encode('base64')
    src = 'data:text/html;base64,{}'.format(htmlEncoded)
    return src


def getSrcAsLocalFile(html):
    """The notebook will serve up any html pages under its
    dir as static files, so if we write our html page to disk
    we can serve it up a bit more simply. This only makes sense
    if we are accessing a local server.
    """
    outputfile = 'output.html'
    outputpath = os.path.join(os.getcwd(), outputfile)
    with open(outputpath, 'w') as g:
        g.write(html)
    url = 'http://127.0.0.1:8888/files/{}'.format(outputfile)
    return url

getSrc = getSrcAsBase64


class PydapWMS(object):
    """A simple object for displaying data from a Pydap WMS.
    """
    def __init__(self, server='http://test.pydap.org/coads.nc.wms',
                 layers=None, centerlat=0, centerlon=0, initialzoom=2,
                 mapwidth=400, mapheight=300, template='template.html'):
        self.wmsserverurl = server
        self.layers = layers if layers else [('SST', 'Sea Surface Temperature', 0)]
        self.centerlat = centerlat
        self.centerlon = centerlon
        self.initialzoom = initialzoom
        self.mapwidth = mapwidth
        self.mapheight = mapheight
        self.template = template

    def __repr__(self):
        return 'PydapWMS({})'.format(str(self.__dict__))

    @property
    def html(self):
        tmpl = loader.load(self.template)
        html = tmpl.generate(**self.__dict__).render('html', doctype='html')
        iframeSrc = getSrc(html)
        iframe = '<iframe src="{}" width="{}" height="{}"></iframe>'
        return HTML(iframe.format(iframeSrc,
                              self.mapwidth + 50,
                              self.mapheight + 50))

