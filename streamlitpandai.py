from langchain.agents import create_csv_agent
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os
import streamlit as st
from langchain.agents.agent_types import AgentType
from langchain.llms import OpenAI
import pandas as pd
from langchain.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

import os
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import pandas as pd

import os
from langchain.llms import OpenAI
from dotenv import load_dotenv, find_dotenv
import langchain
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# matplotlib.use( 'tkagg')


def main():
    _ = load_dotenv(find_dotenv())  # read local .env file
    OpenAI.api_key = os.environ["OPENAI_API_KEY"]


    llm = OpenAI()

    pandas_ai = PandasAI(llm)

    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV 📈")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    if csv_file is not None:


        df = pd.read_csv(csv_file.name, index_col=0)
        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                st.write(pandas_ai.run(df, prompt=user_question))


if __name__ == "__main__":
    main()