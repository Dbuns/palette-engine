import importlib
import unittest
from unittest.mock import patch

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

import plot_examples


class PlotExampleTests(unittest.TestCase):
    colors = [
        (0.10, 0.20, 0.40),
        (0.65, 0.20, 0.20),
        (0.80, 0.55, 0.10),
        (0.20, 0.55, 0.45),
        (0.55, 0.30, 0.65),
    ]

    def tearDown(self):
        plt.close("all")

    def test_import_does_not_run_showcase(self):
        plt.close("all")
        importlib.reload(plot_examples)
        self.assertEqual(plt.get_fignums(), [])

    def test_each_example_renders_independently(self):
        functions = [
            plot_examples.plot_discrete_lines,
            plot_examples.plot_continuous_lines,
            plot_examples.plot_scatter_fit,
            plot_examples.plot_grouped_bars,
            plot_examples.plot_heatmap,
            plot_examples.plot_multi_panel,
            plot_examples.plot_black_background,
        ]
        for function in functions:
            with self.subTest(function=function.__name__):
                with patch("matplotlib.pyplot.show") as show:
                    function(self.colors)
                show.assert_called_once()
                plt.close("all")

    def test_heatmap_uses_semantic_low_neutral_high_order(self):
        colors = plot_examples.get_heatmap_colors()
        self.assertEqual(
            colors,
            [
                (0 / 255.0, 107 / 255.0, 78 / 255.0),
                (230 / 255.0, 220 / 255.0, 194 / 255.0),
                (244 / 255.0, 180 / 255.0, 0 / 255.0),
            ],
        )


if __name__ == "__main__":
    unittest.main()
