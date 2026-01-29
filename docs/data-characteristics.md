# Data Characteristics Analysis

## 1. Introduction
In real-world e-commerce platforms, product data varies continuously.
Before selecting a sorting strategy, the system analyzes key
characteristics of the product list to ensure efficient sorting.

This analysis helps the system adapt to different data conditions
instead of using a fixed sorting algorithm.

---

## 2. Data Size
Data size refers to the number of products present in the listing.

- Small dataset: few products (e.g., products in a local store)
- Medium dataset: thousands of products (e.g., category-level listing)
- Large dataset: millions of products (e.g., entire marketplace)

Larger datasets require more efficient sorting strategies.

---

## 3. Degree of Sortedness
This refers to how much the data is already sorted.

- Fully unsorted data
- Partially sorted data
- Nearly sorted data

For example, newly added products are often already ordered by date,
making re-sorting faster if handled correctly.

---

## 4. Duplicate Values
Duplicate values occur when multiple products share the same attribute
value.

Examples:
- Many products priced at the same value
- Similar customer ratings (e.g., 4.0 or 4.5)

High duplication affects how efficiently sorting can be performed.

---

## 5. Sorting Key Type
Different attributes behave differently during sorting.

- Price: numeric value
- Rating: decimal value
- Date: timestamp value

The nature of the sorting key influences the choice of sorting strategy.

---

## 6. Frequency of Updates
Product data is not static in e-commerce systems.

Examples of updates:
- New products added
- Price changes
- Rating updates

Frequent updates require adaptive handling to avoid repeated full sorting.

---

## 7. Outcome of Data Analysis
The output of this step is not a sorted list.
Instead, it provides insights about the data that guide the sorting
strategy selection in the next step.
