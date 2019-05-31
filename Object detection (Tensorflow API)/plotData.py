# -*- coding: utf-8 -*-
"""
PLOTTING DATA PROVIDED BY TENSORBOARD
@author: burguej1
"""
import plotly
import plotly.graph_objs as go
import plotly.figure_factory as FF
from plotly.offline import *

import numpy as np
import pandas as pd

data = pd.read_csv('precision_second_model.csv')
sample_data_table=FF.create_table(data.head())

trace1=go.Scatter(x=data['Step'],y=data['Value'],name='Precision')

                   
layout = go.Layout(
    title=go.layout.Title(
        text='mean Average Precision (mAP) in the validation set',            
        font=dict(
                family='Calibri Light, monospace',
                size=18,
                color='#7f7f7f'
            ),
        xref='paper',
        x=0
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text='Steps',
            font=dict(
                family='Calibri Light, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text='mAP',
            font=dict(
                family='Calibri Light, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
)
fig = go.Figure(data=[trace1], layout=layout)
fname="figure1"
plotly.offline.plot(fig, filename=fname,image='svg',image_filename=fname)