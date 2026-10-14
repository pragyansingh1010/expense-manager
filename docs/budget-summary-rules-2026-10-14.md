## Budget summary rules

- Treat amounts as numbers internally and format them only for display.
- Keep income and expenses separate when calculating the remaining balance.
- Handle empty transaction lists without producing `NaN` or misleading totals.
- Apply the selected date range consistently to both charts and summary cards.
- After editing or deleting a transaction, recompute every affected total.