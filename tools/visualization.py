import plotly.express as px
from tools import convert

class Grapher:
    def __init__(self, show_figure = False) -> None:
        self.show = show_figure
        self.graphs = convert.MyCoolDict({})

    def line(self, x, y, title, test):
        fig = px.line(x=x, y=y, title=title)
        if self.show:
            fig.show()
        self.graphs[test] = fig
        return fig




# if __name__ == "__main__":
    