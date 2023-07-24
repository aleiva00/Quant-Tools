############################################################################
#///////////////////////////////////////////////////////////////////////////
############################################################################
#    PAQUETES
############################################################################
#///////////////////////////////////////////////////////////////////////////
############################################################################

# !pip install langchain
# !pip install unstructured # The unstructured library provides open-source components for pre-processing text documents such as PDFs, HTML and Word Documents. 
# !pip install openai
# !pip install pybind11 # pybind11 is a lightweight header-only library that exposes C++ types in Python
# !pip install chromadb # the AI-native open-source embedding database
# !pip install Cython # Cython is an optimising static compiler for both the Python programming language
# !pip install unstructured[local-inference]
# !CC=clang CXX=clang++ ARCHFLAGS="-arch x86_64" pip install 'git+https://github.com/facebookresearch/detectron2.git' # Detectron2 is Facebook AI Research's next generation library that provides state-of-the-art detection and segmentation algorithms.
# !pip install layoutparser[layoutmodels,tesseract] # A Unified Toolkit for Deep Learning Based Document Image Analysis
# !pip install pytesseract # Python-tesseract is an optical character recognition (OCR) tool for python.
# !pip install Pillow==9.0.0 # The Python Imaging Library adds image processing capabilities to your Python interpreter. Need this version, otherwise errors occur.
#!pip install apt-get poppler-utils # error occurs without this, pdf rendering library


# !pip install langchain, openai, chromadb, pypdf
# !pip install openai
# !pip install chromadb
# !pip install pypdf



# Data Mgmt
import pandas as pd

# Viz
import seaborn as sns
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib import dates

# Stats & Math
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Operational/Format
import datetime
import os
from urllib.parse import quote
from urllib.parse import urlencode
import fredapi as fa
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from detectron2.config import get_cfg


# Set time format as the local PC
import locale
locale.setlocale(locale.LC_TIME, 'es_ES')
from datetime import date
from dateutil.relativedelta import relativedelta




from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo,
)




# from pivottablejs import pivot_ui
# pivot_ui(df.tail(), outfile_path=my_path+"_TABLE DISPLAY.html", url="http://localhost/a/b/x.html")



############################################################################
#///////////////////////////////////////////////////////////////////////////
############################################################################
#   Set Working directory
############################################################################
#///////////////////////////////////////////////////////////////////////////
############################################################################


#Fecha de hoy
today = date.today()
#DIRECTORIO DE TRABAJO, DEFINIR SOLAMENTE UNA VEZ ACÁ
my_path=r"C:/Users/Ale Leiva/Documents/GitHub/Quant_Tools"
#Crea una carpeta con el path de arriba en donde se guardará todo
os.mkdir(my_path)


#KEY:    
GPT_key = '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'

# Leemos nuestro API
os.environ['OPENAI_API_KEY'] = 'GPT_key'



llm = OpenAI(temperature=0.1, verbose=True)
PDFA = r'C:/Users/Ale Leiva/Documents/GitHub/Quant-Tools/docs PDF/1GTMEA2023002.pdf'
loader = PyPDFLoader(PDFA)
pages = loader.load_and_split()
store = Chroma.from_documents(pages, collection_name="IMFreport")



vectorstore_info = VectorStoreInfo(
    name="IMF_GTM_report",
    description="IMF last revision of guate",
    vectorstore=store,
)

toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)

agent_executor = create_vectorstore_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)


prompt = input("Enter your search term: ")


response = agent_executor.run(prompt)
print(response)




