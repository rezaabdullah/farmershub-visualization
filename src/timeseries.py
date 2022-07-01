import pandas as pd

def load_data():
    """
    load data from csv
    :return df: return dataframe of the csv dataset
    """

    # read dataset
    df = pd.read_csv("clean_df.csv", dtype={"person_id":str, "person_name":str,
            "person_mobile":str, "person_gender":str}, parse_dates=["transaction_date", 
            "dropout_at"])

    return df

# time series data
def sort_time(df):
    """
    identify time series data and filter data for revenue, running total user numbers etc.
    :param df: main dataset
    :return df: time series data in order
    """
    df.sort_values(by=["transaction_date", "country_name", "user_region", "parent_name",
        "user_type", "user_id", "user_type", "user_name"], inplace=True)

    return df

def reorder(df):
    """
    reorder columns for better readability
    :param df: main dataset
    :return df: reordered dataset
    """
    # reorder columns
    df = df[["transaction_date", "country_name", "user_region", "parent_name", "user_type",
        "user_id", "user_name", "status", "latitude", "longitude", "transaction_category",
        "transaction_id", "person_id", "market_type", "person_name", "person_mobile",
        "person_gender", "market_type", "business_category", "category", "product",
        "product_amount", "product_amount_usd", "due_amount", "revenue", "revenue_usd",
        "cogs_amount", "cogs_amount_usd", "product_expenditure", "product_expenditure_usd",  
        "expenditure", "expenditure_usd", "version", "currency_exchange_rate", "dropout_at"]]

    return df

if __name__ == "__main__":
    df = load_data()
    df = sort_time(df)
    df = reorder(df)


