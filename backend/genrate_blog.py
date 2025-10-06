from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

#Load api key
load_dotenv()
GEMINI_API = os.getenv("GEMINI_API")

def genrate_blog(topic):
    """Genrates a full blog post based on a given topic using gemini-2.5"""
    template = """ write a detailed blog post on the topic "{topic}".
    - Include an engaging introduction
    - Provide 3 key points with explanations
    - Use SEO-friendly keywords
    - End with a conclution and call to action

    return the blog in structured markdown formate.
    """

    propmt = PromptTemplate(
        input_variables=['topic'],
        template=template
        )
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)
    chain = LLMChain(llm=llm,propmt=propmt)

    return chain.run(topic=topic)