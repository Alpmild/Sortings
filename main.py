from matplotlib import pyplot
import numpy as np
from scipy.optimize import curve_fit

from Sorts.Quick.quick import sorted_file as q_s_file
from Sorts.Merge.merge import sorted_file as m_s_file
from Sorts.Heap.heap import sorted_file as h_s_file
from Sorts.Shell.shell import shell_sorted_file as s_s_s_file
from Sorts.Shell.shell import hibbard_sorted_file as s_h_s_file
from Sorts.Shell.shell import pratt_sorted_file as s_p_s_file

colors = ("red", "blue", "green", "black", "orange", "purple", "gray",)


class Models:
    @staticmethod
    def poly2_model(n, a, b, c):
        return a * np.pow(n, 2) + b * n + c

    @staticmethod
    def poly3_2_model(n, a, b, c):
        return a * np.pow(n, 1.5) + b * n + c

    @staticmethod
    def log_model(n, a, b, c):
        return a * n * np.log(n) + b * n + c

    @staticmethod
    def log_p2_model(n, a, b, c):
        return a * n * np.pow(np.log(n), 2) + b * n + c

    @staticmethod
    def line_model(n, a, b):
        return a * n + b


class Plot:
    def __init__(self, file_dir, model, label):
        self.label = file_dir
        self.model = model
        self.label = label

        with open(file_dir) as file:
            data = sorted((map(lambda x: x.replace('|', ' ').split(), file.readlines())), key=lambda x: int(x[0]))
        self.x, self.y = [], []
        for n, t in data:
            self.x.append(int(n))
            self.y.append(float(t))

        self.params = params(self.model, self.x, self.y)

    def points(self):
        return self.x, self.y

    def draw_points(self, color, label=None):
        if label is None:
            label = self.label
        pyplot.plot(self.x, self.y, '.', color=color, label=label)

    def draw_plot(self, color, label=None):
        if label is None:
            label = self.label
        pyplot.plot(self.x, self.y, color=color, label=label)

    def draw_model(self, color, label=None, cnt=100, model=None, params__=None,):
        if label is None:
            label = self.label
        if model is None:
            model = self.model
            params__ = params(self.model, self.x, self.y)
        if params__ is None:
            params__ = self.params

        new_x = np.linspace(1, max(self.x), cnt)
        new_y = model(new_x, *params__)
        pyplot.plot(new_x, new_y, color=color, label=label)


def params(model, x, y):
    return curve_fit(model, x, y)[0]


def rmse(y, model, params__):
    return np.sqrt(sum(map(lambda i: (model(i, *params__) - i) ** 2, y)) / len(y))


def get_points(file_dir: str):
    with open(file_dir) as file:
        data = sorted((map(lambda x: x.replace('|', ' ').split(), file.readlines())), key=lambda x: int(x[0]))
    x, y = [], []
    for n, t in data:
        x.append(int(n))
        y.append(float(t))
    return x, y


def compare_plots(*args):
    for i in range(len(args)):
        args[i].draw_model(colors[i])


def out_params(seq: np.ndarray):
    for i in range(len(seq)):
        if 'e' in str(seq[i]):
            m, exp = str(seq[i]).split('e')
            print(f"{round(float(m), 3)}*10^{int(exp)}")
        else:
            print(round(seq[i], 3))


def main():
    compare_plots(
        Plot(q_s_file, Models.log_model, "Quick"),
        Plot(m_s_file, Models.log_model, "Merge"),
        Plot(h_s_file, Models.log_model, "Heap"),
        Plot(s_s_s_file, Models.log_model, "Shell - Shell seq."),
        Plot(s_h_s_file, Models.log_model, "Shell - Hibbard seq."),
        Plot(s_p_s_file, Models.log_model, "Shell - Pratt seq."),
    )

    # plot = Plot(pratt_sorted_file, Models.log_model, "")
    # plot.draw_points("Blue", "Изначальное время")
    # plot.draw_model("Red", "Регрессионная кривая")
    #
    # out_params(plot.params)

    pyplot.grid()
    pyplot.title(f"Сравнение отсортированного случая")
    pyplot.xlabel("Размерность, n")
    pyplot.ylabel("Время, сек")
    pyplot.legend()
    pyplot.show()


main()
