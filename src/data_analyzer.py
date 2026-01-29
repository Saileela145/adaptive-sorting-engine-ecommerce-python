
from collections import Counter


class DataAnalyzer:
    def analyze(self, products, key):
        """
        Analyze data characteristics for a given sorting key.
        key can be 'price', 'rating', or 'date_added'
        """

        analysis = {}

        # 1. Data size
        analysis["size"] = self._analyze_size(products)

        # 2. Degree of sortedness
        analysis["sortedness"] = self._analyze_sortedness(products, key)

        # 3. Duplicate density
        analysis["duplicates"] = self._analyze_duplicates(products, key)

        return analysis

    def _analyze_size(self, products):
        count = len(products)

        if count <= 10:
            return "small"
        elif count <= 1000:
            return "medium"
        else:
            return "large"

    def _analyze_sortedness(self, products, key):
        values = [getattr(p, key) for p in products]

        if values == sorted(values):
            return "already_sorted"
        elif values == sorted(values, reverse=True):
            return "reverse_sorted"
        else:
            return "unsorted"

    def _analyze_duplicates(self, products, key):
        values = [getattr(p, key) for p in products]
        counts = Counter(values)

        max_frequency = max(counts.values())

        if max_frequency > len(values) / 2:
            return "high"
        else:
            return "low"
