import plotly.graph_objects as go
import plotly.io as pio

pio.templates['mds_theme'] = go.layout.Template(
    layout_title_font_size = 22,
    layout_xaxis_title_font_size = 18,
    layout_yaxis_title_font_size = 18,
    layout_xaxis_tickfont_size = 16,
    layout_yaxis_tickfont_size = 16,
    layout_legend_font_size = 14,
    layout_annotations=[
        go.layout.Annotation(
            text='© Mongolian Data Stories', 
            x=1.01, 
            y=-.15,                         
            showarrow = False, 
            xref='paper', 
            yref='paper', 
            xanchor='right', 
            yanchor='auto', 
            font=dict(size=14),
        )
    ]
)