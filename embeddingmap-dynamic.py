{
 "metadata": {
  "name": "Embedding our map into the notebook"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "import dapbook",
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 2
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "a = dapbook.PydapWMS()\nprint a\na.html",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": "PydapWMS({'layers': [('SST', 'Sea Surface Temperature', 0)], 'template': 'template2.html', 'mapheight': 300, 'centerlon': 0, 'wmsserverurl': 'http://test.pydap.org/coads.nc.wms', 'initialzoom': 2, 'centerlat': 0, 'mapwidth': 400})\n"
      },
      {
       "html": "<iframe src=\"data:text/html;base64,PCFET0NUWVBFIGh0bWwgUFVCTElDICItLy9XM0MvL0RURCBIVE1MIDQuMDEvL0VOIiAiaHR0cDov\nL3d3dy53My5vcmcvVFIvaHRtbDQvc3RyaWN0LmR0ZCI+CjxodG1sPgo8aGVhZD4KICAgIDx0aXRs\nZT5PcGVuTGF5ZXJzIEV4YW1wbGU8L3RpdGxlPgogICAgPHNjcmlwdCBzcmM9Imh0dHA6Ly9vcGVu\nbGF5ZXJzLm9yZy9hcGkvT3BlbkxheWVycy5qcyI+PC9zY3JpcHQ+CiAgICA8bGluayByZWw9InN0\neWxlc2hlZXQiIGhyZWY9Imh0dHA6Ly9vcGVubGF5ZXJzLm9yZy9kZXYvdGhlbWUvZGVmYXVsdC9z\ndHlsZS5jc3MiIHR5cGU9InRleHQvY3NzIj4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJl\nZj0iaHR0cDovL29wZW5sYXllcnMub3JnL2Rldi9leGFtcGxlcy9zdHlsZS5jc3MiIHR5cGU9InRl\neHQvY3NzIj4KICAgIDxzY3JpcHQgc3JjPSJodHRwOi8vY29kZS5qcXVlcnkuY29tL2pxdWVyeS1s\nYXRlc3QuanMiPjwvc2NyaXB0PgogICAgPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiPgog\nICAgdmFyIG1hcCwgb3BlbmxheWVyOwogICAgZnVuY3Rpb24gaW5pdCgpewogICAgICAgIG1hcCA9\nIG5ldyBPcGVuTGF5ZXJzLk1hcCgibWFwIiwgewogICAgICAgIGNvbnRyb2xzOiBbCiAgICAgICAg\nICAgIG5ldyBPcGVuTGF5ZXJzLkNvbnRyb2wuTGF5ZXJTd2l0Y2hlcigpLAogICAgICAgICAgICBu\nZXcgT3BlbkxheWVycy5Db250cm9sLlBhblpvb21CYXIoKSwKICAgICAgICAgICAgbmV3IE9wZW5M\nYXllcnMuQ29udHJvbC5BdHRyaWJ1dGlvbigpLAogICAgICAgICAgICBuZXcgT3BlbkxheWVycy5D\nb250cm9sLk1vdXNlUG9zaXRpb24oKSwKICAgICAgICAgICAgbmV3IE9wZW5MYXllcnMuQ29udHJv\nbC5OYXZpZ2F0aW9uKCksCiAgICAgICAgICAgIF0sCiAgICAgICAgfSk7CiAgICAgICAgb3Blbmxh\neWVyID0gbmV3IE9wZW5MYXllcnMuTGF5ZXIuV01TKCJPcGVuTGF5ZXJzIFdNUyIsCiAgICAgICAg\nICAgICAgICAiaHR0cDovL21hcHMub3Blbmdlby5vcmcvZ2Vvd2ViY2FjaGUvc2VydmljZS93bXMi\nLCB7bGF5ZXJzOiAnb3BlbnN0cmVldG1hcCcsICdmb3JtYXQnOiAnaW1hZ2UvcG5nJ30pOwogICAg\nICAgIG1hcC5hZGRMYXllcihvcGVubGF5ZXIpOwogICAgICAgICAgICBtYXAuYWRkTGF5ZXIobmV3\nIE9wZW5MYXllcnMuTGF5ZXIuV01TKAogICAgICAgICAgICAgICAgIlNlYSBTdXJmYWNlIFRlbXBl\ncmF0dXJlIiwKICAgICAgICAgICAgICAgICJodHRwOi8vdGVzdC5weWRhcC5vcmcvY29hZHMubmMu\nd21zP1NTVFswXSIsCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgbGF5ZXJz\nOiAiU1NUIiwKICAgICAgICAgICAgICAgICAgICB0cmFuc3BhcmVudDogInRydWUiLAogICAgICAg\nICAgICAgICAgICAgIGZvcm1hdDogImltYWdlL3BuZyIsCiAgICAgICAgICAgICAgICB9LAogICAg\nICAgICAgICAgICAgeyAgIGlzQmFzZUxheWVyOiBmYWxzZSwKICAgICAgICAgICAgICAgIH0pKTsK\nICAgICAgICBtYXAuc2V0Q2VudGVyKG5ldyBPcGVuTGF5ZXJzLkxvbkxhdCgwLCAwKSwgMik7CiAg\nICAgICAgfQogICAgPC9zY3JpcHQ+CjwvaGVhZD4KPGJvZHkgb25sb2FkPSJpbml0KCk7Ij4KICAg\nIDxkaXYgaWQ9Im1hcCIgc3R5bGU9IndpZHRoOiA0MDBweDsgaGVpZ2h0OiAzMDBweCI+PC9kaXY+\nCjwvYm9keT4KPC9odG1sPg==\n\" width=\"450\" height=\"350\"></iframe>",
       "output_type": "pyout",
       "prompt_number": 7,
       "text": "<IPython.core.display.HTML at 0x2d9e850>"
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "b = dapbook.PydapWMS(server='http://127.0.0.1:8001/IDT71003_TAS_MinT_SFC.nc.wms',\n                     layers=[('MinT_SFC', 'Min temp day0', 0),\n                            ('MinT_SFC', 'Min temp day2', 2),\n                     ], centerlat=-42, centerlon=147, initialzoom=6,\n                     mapwidth=550, mapheight=400)\nprint b\nb.html",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": "PydapWMS({'layers': [('MinT_SFC', 'Min temp day0', 0), ('MinT_SFC', 'Min temp day2', 2)], 'template': 'template2.html', 'mapheight': 400, 'centerlon': 147, 'wmsserverurl': 'http://127.0.0.1:8001/IDT71003_TAS_MinT_SFC.nc.wms', 'initialzoom': 6, 'centerlat': -42, 'mapwidth': 550})\n"
      },
      {
       "html": "<iframe src=\"data:text/html;base64,PCFET0NUWVBFIGh0bWwgUFVCTElDICItLy9XM0MvL0RURCBIVE1MIDQuMDEvL0VOIiAiaHR0cDov\nL3d3dy53My5vcmcvVFIvaHRtbDQvc3RyaWN0LmR0ZCI+CjxodG1sPgo8aGVhZD4KICAgIDx0aXRs\nZT5PcGVuTGF5ZXJzIEV4YW1wbGU8L3RpdGxlPgogICAgPHNjcmlwdCBzcmM9Imh0dHA6Ly9vcGVu\nbGF5ZXJzLm9yZy9hcGkvT3BlbkxheWVycy5qcyI+PC9zY3JpcHQ+CiAgICA8bGluayByZWw9InN0\neWxlc2hlZXQiIGhyZWY9Imh0dHA6Ly9vcGVubGF5ZXJzLm9yZy9kZXYvdGhlbWUvZGVmYXVsdC9z\ndHlsZS5jc3MiIHR5cGU9InRleHQvY3NzIj4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJl\nZj0iaHR0cDovL29wZW5sYXllcnMub3JnL2Rldi9leGFtcGxlcy9zdHlsZS5jc3MiIHR5cGU9InRl\neHQvY3NzIj4KICAgIDxzY3JpcHQgc3JjPSJodHRwOi8vY29kZS5qcXVlcnkuY29tL2pxdWVyeS1s\nYXRlc3QuanMiPjwvc2NyaXB0PgogICAgPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiPgog\nICAgdmFyIG1hcCwgb3BlbmxheWVyOwogICAgZnVuY3Rpb24gaW5pdCgpewogICAgICAgIG1hcCA9\nIG5ldyBPcGVuTGF5ZXJzLk1hcCgibWFwIiwgewogICAgICAgIGNvbnRyb2xzOiBbCiAgICAgICAg\nICAgIG5ldyBPcGVuTGF5ZXJzLkNvbnRyb2wuTGF5ZXJTd2l0Y2hlcigpLAogICAgICAgICAgICBu\nZXcgT3BlbkxheWVycy5Db250cm9sLlBhblpvb21CYXIoKSwKICAgICAgICAgICAgbmV3IE9wZW5M\nYXllcnMuQ29udHJvbC5BdHRyaWJ1dGlvbigpLAogICAgICAgICAgICBuZXcgT3BlbkxheWVycy5D\nb250cm9sLk1vdXNlUG9zaXRpb24oKSwKICAgICAgICAgICAgbmV3IE9wZW5MYXllcnMuQ29udHJv\nbC5OYXZpZ2F0aW9uKCksCiAgICAgICAgICAgIF0sCiAgICAgICAgfSk7CiAgICAgICAgb3Blbmxh\neWVyID0gbmV3IE9wZW5MYXllcnMuTGF5ZXIuV01TKCJPcGVuTGF5ZXJzIFdNUyIsCiAgICAgICAg\nICAgICAgICAiaHR0cDovL21hcHMub3Blbmdlby5vcmcvZ2Vvd2ViY2FjaGUvc2VydmljZS93bXMi\nLCB7bGF5ZXJzOiAnb3BlbnN0cmVldG1hcCcsICdmb3JtYXQnOiAnaW1hZ2UvcG5nJ30pOwogICAg\nICAgIG1hcC5hZGRMYXllcihvcGVubGF5ZXIpOwogICAgICAgICAgICBtYXAuYWRkTGF5ZXIobmV3\nIE9wZW5MYXllcnMuTGF5ZXIuV01TKAogICAgICAgICAgICAgICAgIk1pbiB0ZW1wIGRheTAiLAog\nICAgICAgICAgICAgICAgImh0dHA6Ly8xMjcuMC4wLjE6ODAwMS9JRFQ3MTAwM19UQVNfTWluVF9T\nRkMubmMud21zP01pblRfU0ZDWzBdIiwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAg\nICAgICBsYXllcnM6ICJNaW5UX1NGQyIsCiAgICAgICAgICAgICAgICAgICAgdHJhbnNwYXJlbnQ6\nICJ0cnVlIiwKICAgICAgICAgICAgICAgICAgICBmb3JtYXQ6ICJpbWFnZS9wbmciLAogICAgICAg\nICAgICAgICAgfSwKICAgICAgICAgICAgICAgIHsgICBpc0Jhc2VMYXllcjogZmFsc2UsCiAgICAg\nICAgICAgICAgICB9KSk7CiAgICAgICAgICAgIG1hcC5hZGRMYXllcihuZXcgT3BlbkxheWVycy5M\nYXllci5XTVMoCiAgICAgICAgICAgICAgICAiTWluIHRlbXAgZGF5MiIsCiAgICAgICAgICAgICAg\nICAiaHR0cDovLzEyNy4wLjAuMTo4MDAxL0lEVDcxMDAzX1RBU19NaW5UX1NGQy5uYy53bXM/TWlu\nVF9TRkNbMl0iLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGxheWVyczog\nIk1pblRfU0ZDIiwKICAgICAgICAgICAgICAgICAgICB0cmFuc3BhcmVudDogInRydWUiLAogICAg\nICAgICAgICAgICAgICAgIGZvcm1hdDogImltYWdlL3BuZyIsCiAgICAgICAgICAgICAgICB9LAog\nICAgICAgICAgICAgICAgeyAgIGlzQmFzZUxheWVyOiBmYWxzZSwKICAgICAgICAgICAgICAgIH0p\nKTsKICAgICAgICBtYXAuc2V0Q2VudGVyKG5ldyBPcGVuTGF5ZXJzLkxvbkxhdCgxNDcsIC00Miks\nIDYpOwogICAgICAgIH0KICAgIDwvc2NyaXB0Pgo8L2hlYWQ+Cjxib2R5IG9ubG9hZD0iaW5pdCgp\nOyI+CiAgICA8ZGl2IGlkPSJtYXAiIHN0eWxlPSJ3aWR0aDogNTUwcHg7IGhlaWdodDogNDAwcHgi\nPjwvZGl2Pgo8L2JvZHk+CjwvaHRtbD4=\n\" width=\"600\" height=\"450\"></iframe>",
       "output_type": "pyout",
       "prompt_number": 8,
       "text": "<IPython.core.display.HTML at 0x2d9efd0>"
      }
     ],
     "prompt_number": 8
    }
   ],
   "metadata": {}
  }
 ]
}
