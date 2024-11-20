import os
import google.generativeai as genai

# Configure the API with your API key
genai.configure(api_key='AIzaSyCNxTWjzI2e6V-a5jSZNbz9b4JFFbQxC6A')

def expiry_of_ingredient(ingredient):
    model = genai.GenerativeModel("gemini-1.5-flash")
    # Ask the model if the ingredient needs to be refrigerated
    # response1 = model.generate_content(f"Does {ingredient} need to be refrigerated? Give me YES or NO")
    # print(response1.text)

    # # Check if the ingredient needs refrigeration and get the average expiry date
    # if 'YES' in response1.text.upper():
    #     response = model.generate_content(f"Give me just the number, not text, what is the average expiry date with units (days) of {ingredient} if it is put in a refrigerator in my house? Don't go into details about the food item, temperature, storage conditions, just give me the average.")
    # else:
    #     response = model.generate_content(f"Give me just the number, not text, what is the average expiry date with units (days) of {ingredient} if it is put at room temperature in my house? Don't go into details about the food item, temperature, storage conditions, just give me the average.")
    response = model.generate_content(f"Give me recipe that can be made from {ingredient} assume that I have basic ingredients to make anything.")
    # Print the response
    # print(response.text)
    return response

# print(expiry_of_ingredient("apple"))