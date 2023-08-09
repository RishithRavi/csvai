import os
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import pandas as pd

import os
from langchain.llms import OpenAI
from dotenv import load_dotenv, find_dotenv
import langchain

_ = load_dotenv(find_dotenv())  # read local .env file
OpenAI.api_key = os.environ["OPENAI_API_KEY"]


llm = OpenAI()

pandas_ai = PandasAI(llm)


df = pd.read_csv("./constituents_csv.csv", index_col=0)
df.head(3)

result = pandas_ai.run(df, prompt='What are all the companies in the financial sector?')

print(result)