import unittest

from colors_source import palettes


EXPECTED_RGB = {
    "PE001": [(136, 57, 60), (129, 209, 208)],
    "PE002": [(19, 115, 122), (251, 202, 137)],
    "PE003": [(129, 154, 148), (233, 131, 137)],
    "PE004": [(170, 167, 174), (231, 208, 200)],
    "PE005": [(231, 136, 97), (183, 241, 224)],
    "PE006": [(0, 68, 55), (213, 179, 142)],
    "PE007": [(106, 98, 35), (212, 199, 146)],
    "PE008": [(246, 163, 51), (104, 55, 48)],
    "PE009": [(205, 170, 75), (66, 125, 119)],
    "PE010": [(153, 92, 74), (131, 145, 107)],
    "PE011": [(130, 175, 190), (229, 178, 97)],
    "PE012": [(233, 89, 73), (243, 219, 188)],
    "PE013": [(67, 64, 40), (138, 113, 64)],
    "PE014": [(201, 124, 98), (135, 141, 139)],
    "PE015": [(199, 84, 41), (223, 193, 158)],
    "PE016": [(136, 151, 148), (254, 237, 225)],
    "PE017": [(179, 102, 108), (180, 107, 2)],
    "PE018": [(147, 203, 132), (93, 131, 63), (240, 169, 1), (213, 97, 177), (232, 223, 207)],
    "PE019": [(31, 47, 29), (107, 127, 94), (122, 106, 58), (214, 205, 186), (14, 18, 3)],
    "PE020": [(194, 79, 42), (140, 203, 154), (27, 107, 90), (232, 220, 200), (107, 58, 34)],
    "PE021": [(242, 183, 5), (246, 225, 29), (124, 163, 59), (47, 79, 30), (232, 216, 182)],
    "PE022": [(244, 180, 0), (138, 201, 110), (0, 107, 78), (232, 93, 61), (230, 220, 194)],
    "PE023": [(36, 107, 115), (212, 122, 91), (130, 149, 87)],
    "PE024": [(113, 63, 93), (105, 144, 120), (211, 164, 59)],
    "PE025": [(56, 86, 109), (129, 125, 182), (220, 116, 108)],
    "PE026": [(42, 100, 120), (217, 138, 80), (169, 154, 194)],
    "PE027": [(49, 92, 76), (166, 78, 99), (199, 166, 74)],
    "PE028": [(69, 90, 122), (94, 150, 136), (216, 117, 104)],
    "PE029": [(40, 92, 77), (223, 146, 84), (123, 78, 112), (98, 160, 173)],
    "PE030": [(53, 64, 95), (197, 110, 121), (118, 145, 83), (209, 161, 60)],
    "PE031": [(31, 110, 120), (184, 93, 76), (139, 120, 163), (212, 173, 63)],
    "PE032": [(73, 97, 122), (208, 107, 88), (216, 174, 73), (120, 147, 107)],
    "PE033": [(94, 75, 117), (183, 99, 118), (108, 145, 124), (211, 155, 74)],
    "PE034": [(46, 95, 119), (111, 142, 88), (200, 111, 80), (167, 133, 166)],
    "PE035": [(0, 107, 78), (230, 220, 194), (244, 180, 0)]
}


class PaletteDataTests(unittest.TestCase):
    def test_exact_palette_collection(self):
        self.assertEqual(set(palettes), set(EXPECTED_RGB))
        for palette_id, expected in EXPECTED_RGB.items():
            with self.subTest(palette_id=palette_id):
                actual = [color["rgb"] for color in palettes[palette_id]["colors"].values()]
                self.assertEqual(actual, expected)

    def test_size_distribution(self):
        counts = {size: 0 for size in range(2, 6)}
        for palette in palettes.values():
            counts[len(palette["colors"])] += 1
        self.assertEqual(counts, {2: 17, 3: 7, 4: 6, 5: 5})

    def test_schema_ranges_roles_and_sources(self):
        self.assertEqual(len(palettes), 35)
        allowed_sources = {"owner_curated_2026", "project_curated_2026"}
        for palette_id, palette in palettes.items():
            with self.subTest(palette_id=palette_id):
                self.assertIn(palette["source"], allowed_sources)
                self.assertIsInstance(palette["name"], str)
                self.assertTrue(palette["name"])

                colors = palette["colors"]
                self.assertGreaterEqual(len(colors), 2)
                for color in colors.values():
                    self.assertIsInstance(color["name"], str)
                    self.assertEqual(len(color["rgb"]), 3)
                    self.assertTrue(all(isinstance(value, int) and 0 <= value <= 255 for value in color["rgb"]))
                    self.assertEqual(len(color["cmyk"]), 4)
                    self.assertTrue(all(isinstance(value, int) and 0 <= value <= 100 for value in color["cmyk"]))

                roles = palette["roles"]
                references = [roles["dominant"], *roles["secondary"], *roles["accent"]]
                self.assertEqual(references, list(colors))


if __name__ == "__main__":
    unittest.main()
