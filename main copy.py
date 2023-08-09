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

def main():
    load_dotenv()

    # Load the OpenAI API key from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV 📈")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    if csv_file is not None:

        df = pd.read_csv(csv_file.name)
        agent = create_pandas_dataframe_agent(
            OpenAI(temperature=0,),
            df,
            verbose=True,
            # agent_type=AgentType.OPENAI_FUNCTIONS,
        )
        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))


if __name__ == "__main__":
    main()