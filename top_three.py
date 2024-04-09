import pandas as pd

def top3(df, country, favorite_item):
    """
    #top3 favorite item  for a specific given country
    :param df:  survey df
    :param country: any country in the dataset
    :param favorite_item: color or movie or food
    :return: top 3 favorite item
    """
    top = df[df['country'] == country][favorite_item].value_counts(sort=True)
    return top[0:3]


def top3_all_countries(df, favorite_item):
    """
    top3 favorite_item for all the countries in the dataset
    :param df: survey df
    :param favorite_item:color or movie or food
    :return: top_3_per_country
    """
    per_country = df.groupby(["country", favorite_item]).size().reset_index(name='counts')
    per_country.sort_values(['country', "counts", favorite_item], ascending=[True, False, True], inplace=True)
    top_3_per_country = per_country.groupby('country').head(3)
    return top_3_per_country

def faster_top3_all_countries(df, favorite_item):
    """
    This is much faster than the top3, becasue it uses heap based nlargest versus sorting  to find the top3
    :param df: survey df
    :param favorite_item:color or movie or food
    :return: top_3_per_country
    """
    counts = df.groupby(['country', favorite_item]).size()
    top_3_per_country = counts.groupby(level=0).nlargest(3).reset_index(level=0, drop=True).reset_index(name='Count')
    print("top_3_per_countries sorted by count!")
    print(top_3_per_country)
    top_3_per_country= top_3_per_country.groupby("country").aggregate({"movie":lambda x: ','.join(x)})
    top_3_per_country.rename({favorite_item: "top3 " + favorite_item}, inplace=True, axis=1)
    top_3_per_country.reset_index( inplace=True)
    return top_3_per_country

if __name__ == "__main__":
    df = pd.read_csv("survey.csv")
    item_of_interest = "movie"
    print("sample df:")
    print(df)
    # country = "france"
    # result= top3(df,country=country, favor=favor)
    # print(f"top3 {favor} for the  given country{country}: ")

    print()
    print()
    print()

    result = faster_top3_all_countries(df, favorite_item=item_of_interest)
    print()
    print()
    print()
    print("Top3 results:")
    print(result)

