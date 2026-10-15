import unittest
from copy import deepcopy
from unittest.mock import patch

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from colors_engine import (
    _interp_lab,
    get_palette,
    list_palettes,
    show_palettes,
    wcag_contrast_ratio,
)
from colors_source import palettes as bundled_palettes


TEST_PALETTES = {
    "TEST": {
        "source": "test",
        "colors": {
            "A": {"rgb": (20, 40, 80), "cmyk": (75, 50, 0, 69)},
            "B": {"rgb": (130, 30, 30), "cmyk": (0, 77, 77, 49)},
            "C": {"rgb": (170, 110, 0), "cmyk": (0, 35, 100, 33)},
        },
        "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]},
    }
}


class ColorEngineTests(unittest.TestCase):
    def tearDown(self):
        plt.close("all")

    def test_wcag_reference_values(self):
        self.assertAlmostEqual(wcag_contrast_ratio((0, 0, 0), (255, 255, 255)), 21.0)
        self.assertAlmostEqual(wcag_contrast_ratio((255, 255, 255), (255, 255, 255)), 1.0)

    def test_list_and_get_discrete_screen_palette(self):
        self.assertEqual(list_palettes(TEST_PALETTES, size=3), ["TEST"])
        colors, palette_id = get_palette(TEST_PALETTES, size=3, palette_id="TEST")
        self.assertEqual(palette_id, "TEST")
        self.assertEqual(len(colors), 3)
        self.assertEqual(colors[0], (20 / 255.0, 40 / 255.0, 80 / 255.0))

    def test_background_filter_is_optional(self):
        colors, palette_id = get_palette(
            bundled_palettes,
            size=5,
            palette_id="PE018",
        )
        self.assertEqual(palette_id, "PE018")
        self.assertEqual(len(colors), 5)

        with self.assertRaises(ValueError):
            get_palette(
                bundled_palettes,
                size=5,
                palette_id="PE018",
                background="white",
            )

    def test_continuous_palette_has_requested_size_and_endpoints(self):
        anchors = [(20, 40, 80), (130, 30, 30), (170, 110, 0)]
        output = _interp_lab(anchors, 11)
        self.assertEqual(len(output), 11)
        self.assertEqual(output[0], anchors[0])
        self.assertEqual(output[-1], anchors[-1])

    def test_print_mode_returns_cmyk(self):
        colors, _ = get_palette(TEST_PALETTES, size=2, palette_id="TEST", mode="p")
        self.assertEqual(colors, [(75, 50, 0, 69), (0, 77, 77, 49)])

    def test_list_and_get_apply_the_same_print_requirements(self):
        incomplete = deepcopy(TEST_PALETTES)
        incomplete["TEST"]["colors"]["A"]["cmyk"] = None
        self.assertEqual(list_palettes(incomplete, size=2, mode="p"), [])
        with self.assertRaises(ValueError):
            get_palette(incomplete, size=2, palette_id="TEST", mode="p")

    def test_print_mode_does_not_validate_unused_background(self):
        colors, _ = get_palette(
            TEST_PALETTES,
            size=2,
            palette_id="TEST",
            mode="p",
            background="not-used-for-print",
        )
        self.assertEqual(len(colors), 2)

    def test_print_mode_rejects_continuous_output_case_insensitively(self):
        with self.assertRaises(ValueError):
            get_palette(TEST_PALETTES, size=2, n_out=4, palette_id="TEST", mode="P")

    def test_invalid_arguments_fail_clearly(self):
        for kwargs in ({"size": 0}, {"size": True}, {"n_out": 0}, {"mode": "web"}, {"mode": None}):
            with self.subTest(kwargs=kwargs):
                with self.assertRaises(ValueError):
                    get_palette(TEST_PALETTES, palette_id="TEST", **kwargs)
        with self.assertRaises(KeyError):
            get_palette(TEST_PALETTES, palette_id="missing")
        with self.assertRaises(ValueError):
            list_palettes(TEST_PALETTES, mode=None)
        with self.assertRaises(ValueError):
            list_palettes(TEST_PALETTES, size=0)
        with self.assertRaises(ValueError):
            get_palette(TEST_PALETTES, palette_id="TEST", background=(256, 0, 0))

    def test_gallery_can_render_without_opening_a_window(self):
        with patch("matplotlib.pyplot.show") as show:
            show_palettes(TEST_PALETTES, size=2, max_rows=1)
        show.assert_called_once()

    def test_gallery_rejects_print_mode(self):
        with self.assertRaisesRegex(ValueError, "only supports mode='s'"):
            show_palettes(TEST_PALETTES, size=2, mode="p")


if __name__ == "__main__":
    unittest.main()
