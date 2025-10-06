from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API")

def genrate_blog(topic):
    """Generates a full blog post on a given topic using Gemini 1.5 Pro."""
    
    template = """
    Write a detailed blog post on the topic "{topic}".
    - Include an engaging introduction
    - Provide 3 key points with explanations
    - Use SEO-friendly keywords
    - End with a strong conclusion and call-to-action.
    Return the blog in structured markdown format.
    """

    prompt = PromptTemplate(
        input_variables=["topic"],
        template=template
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-pro",
        temperature=0.7,
        google_api_key=GEMINI_API_KEY
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    return chain.run(topic=topic)