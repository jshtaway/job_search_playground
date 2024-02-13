import plotly.express as px
from tools import convert
import pandas as pd

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
    
    def gantt(self):
        df = pd.DataFrame([
            dict(Task="Jen", Start='2024-01-22', Finish='2024-02-22'),
            dict(Task="Lindsay", Start='2024-01-22', Finish='2024-02-22'),
            dict(Task="Noah", Start='2024-01-22', Finish='2024-02-01'),
            dict(Task="Jenny", Start='2024-02-05', Finish='2024-02-13'),
            dict(Task="Jon", Start='2024-01-28', Finish='2024-02-11'),
            dict(Task="Steph", Start='2024-01-30', Finish='2024-02-05'),
            dict(Task="Atlantis", Start='2024-02-19', Finish='2024-02-22'),
            dict(Task="Claire", Start='2024-02-02', Finish='2024-02-08'),
            dict(Task="Isabel", Start='2024-02-06', Finish='2024-02-10'),
            dict(Task="Grant", Start='2024-02-06', Finish='2024-02-09'),
            dict(Task="Fallon", Start='2024-02-06', Finish='2024-02-09'),
        ])

        fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task")
        fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
        fig.show()




# if __name__ == "__main__":
    