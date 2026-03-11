cars = ["Toyota", "Honda", "BMW", "Audi", "Mercedes", "Ford", "Hyundai", "Kia", "Tesla", "Nissan"]
print(cars)

favorite = input("which is your favorite car?")
print(favorite)
result = favorite in cars 
print("your favorite car in list ",result)
result = favorite not in cars 
print("your favorite car not in list ",result)

#tuple
companies = ("Google", "Microsoft", "OpenAI", "Amazon", "Meta", "IBM", "NVIDIA", "Tesla", "Apple", "Intel")

work = input("In which company you work?")
print("your company is top most ai company ?",work in companies)

ai = "ChatGPT DALL-E Midjourney StableDiffusion Gemini Claude Sora Copilot LLaMA Grok"
agent = input("Which agent you use daily")
print("your daily useage agent in topmost generate ai list ",agent in ai )

