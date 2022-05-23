import pandas as pd

tgt_website = r"https://finance.yahoo.com/quote/PETR4.SA/key-statistics?p=PETR4.SA"

def get_key_stats(tgt_website, ticker):
    df_list = pd.read_html(tgt_website)
    result_df = df_list[0]
    for df in df_list[1:]:
        result_df = result_df.append(df)
    result_df = result_df.rename(columns={1: "Ticker"})
    return  result_df.set_index(0).T


df_petr4 = get_key_stats(tgt_website, 'PETR4')
print(df_petr4)