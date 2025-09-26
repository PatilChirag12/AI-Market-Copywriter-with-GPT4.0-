import streamlit as st
import cohere
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")

# Initialize Cohere client
co = cohere.Client(cohere_api_key)

st.set_page_config(page_title="🧠 AI Marketing Copywriter (Free with Cohere)", layout="centered")
st.title("🧠 AI Marketing Copywriter (Cohere)")
st.markdown("Generate product descriptions, captions, or ad copy using free LLMs from Cohere!")

# Input fields
product_name = st.text_input("Product Name")
product_features = st.text_area("Product Features / Details")
product_category = st.selectbox("Category", ["Fashion", "Electronics", "Home Decor", "Beauty", "Other"])
tone = st.selectbox("Tone of Voice", ["Professional", "Playful", "Luxury", "Bold", "Friendly"])
output_type = st.selectbox("What do you want to generate?", ["Product Description", "Social Media Caption", "Ad Copy", "SEO Title"])

submit = st.button("Generate Copy ✨")

# Prompt Template
def build_prompt(name, features, category, tone, output_type):
    return f"""Write a {output_type.lower()} in a {tone.lower()} tone for a product.
Product Name: {name}
Category: {category}
Features: {features}
Make it clear, creative, and tailored to e-commerce marketing."""

# Generate with Cohere Chat API
def generate_with_cohere(prompt):
    try:
        response = co.chat(
            model="command-a-03-2025",
            message=prompt,
            max_tokens=200,
            temperature=0.7
        )
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {e}"

# Main logic
if submit:
    if product_name and product_features:
        with st.spinner("Generating..."):
            prompt = build_prompt(product_name, product_features, product_category, tone, output_type)
            result = generate_with_cohere(prompt)
            st.markdown("### ✍️ Generated Copy:")
            st.success(result)
    else:
        st.warning("Please fill in all fields.")
