import os
from flask import Flask,request,jsonify
from backend.genrate_blog import genrate_blog

app = Flask(__name__)

@app.route('/generate',methods=['POST'])
def generate_blog_endpoint():
    """Handle blog generation requests"""
    data = request.json
    topic = data.get("topic","")

    if not topic:
        return jsonify({"error":"Topic is required"}),400
    
    blog = genrate_blog(topic)

    #Save to file
    blog_filename= f"blogs/{topic.replace(' ',"_").lower()}.md"
    with open(blog_filename,"w",encoding="utf-8") as f:
        f.write(blog)

    return jsonify({"message":"Blog generated successfully!","blog":blog})

if __name__ == "__main__":
    os.makedirs("blogs",exist_ok=True)
    app.run(debug=True)