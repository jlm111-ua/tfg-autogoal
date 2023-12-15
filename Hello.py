# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="AutoGOAL",
        page_icon="👋",
    )

    st.write("# :balloon: Welcome to AutoGOAL! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        AutoGOAL is a Python library for automatically finding the best way to solve a given task. 
        It has been designed mainly for Automated Machine Learning (aka AutoML) but it can be used 
        in any scenario where you have several possible ways to solve a given task.

        Technically speaking, AutoGOAL is a framework for program synthesis, i.e., 
        finding the best program to solve a given problem, provided that the user can describe the space of all possible programs. 
        AutoGOAL provides a set of low-level components to define different spaces and efficiently search in them. 
        In the specific context of machine learning, AutoGOAL also provides high-level components that can be used as a black-box in almost any type of problem and dataset format.
        
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
