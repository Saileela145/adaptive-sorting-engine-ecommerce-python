
class DecisionEngine:
    def decide(self, analysis):
        """
        Decide sorting strategy based on analysis result.
        """

        size = analysis["size"]
        sortedness = analysis["sortedness"]
        duplicates = analysis["duplicates"]

        # Rule 1: Small dataset
        if size == "small":
            return "simple_sort"

        # Rule 2: Nearly or already sorted data
        if sortedness in ("already_sorted", "reverse_sorted"):
            return "adaptive_sort"

        # Rule 3: High duplicate values
        if duplicates == "high":
            return "duplicate_aware_sort"

        # Rule 4: Default case for large/unsorted data
        return "efficient_sort"
