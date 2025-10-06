import os
from flask import Flask,request,jsonify
from backend.genrate_blog import genrate_blog

app = Flask(__name__)

@app.route('/genrate',methods=['POST'])
def generate_blog_endpoint():
    """Handle blog generation requests"""
    data = request.json
    topic = data.get("topic","")

    if not topic:
        return jsonify({"error":"Topic is required"}),400
    
    blog = genrate_blog(topic)