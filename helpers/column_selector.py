def get_numeric_columns(df, ask_user=False):
    """
    Detect numeric columns to sum, with optional user input and exclusions.

    Parameters:
        df (DataFrame): The dataframe to analyze.
        ask_user (bool): Whether to prompt the user for manual selection.

    Returns:
        List[str]: List of column names to include in totals.
    """

    # Keywords to exclude from total row (case-insensitive, includes partial matches)
    excluded_keywords = ["id", "age", "year", "yıl", "yas", "doğum", "dogum"]

    # Ask user for manual column selection
    if ask_user:
        answer = input("Would you like to manually select columns to total? (y/n): ").strip().lower()
        if answer == "y":
            user_input = input("Enter column names to total, separated by commas (e.g., budget, price): ")
            return [
                col.strip() for col in user_input.split(",")
                if col.strip() in df.columns
            ]

    # Helper: check if a column should be excluded
    def is_excluded(col_name):
        normalized = col_name.strip().lower()
        return any(keyword in normalized for keyword in excluded_keywords)

    # Auto-detect numeric columns and filter out excluded ones
    return [
        col for col in df.select_dtypes(include=["int64", "float64"]).columns
        if not is_excluded(col)
    ]
def get_numeric_columns(df, ask_user=False):
    excluded_keywords = ["id", "age", "year", "yıl", "yas", "doğum", "dogum"]

    # Print ALL numeric columns before filtering
    print("🧪 All numeric columns:", df.select_dtypes(include=["int64", "float64"]).columns.tolist())

    def is_excluded(col_name):
        col_name = str(col_name).strip().lower()
        return any(keyword in col_name for keyword in excluded_keywords)

    numeric_columns = [
        col for col in df.select_dtypes(include=["int64", "float64"]).columns
        if not is_excluded(col)
    ]

    # Print what will be used
    print("✅ Columns selected for total row:", numeric_columns)

    return numeric_columns
