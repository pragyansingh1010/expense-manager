# Expense Manager — QA Checklist

- Validate that amount is positive and finite before saving an expense.
- Check category, date, and description validation.
- Verify totals after adding, editing, and deleting an entry.
- Test empty storage and malformed stored JSON safely.
- Confirm monthly summaries do not mix months or years.
- Check that user-entered descriptions are rendered as text, not HTML.