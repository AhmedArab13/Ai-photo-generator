from MukeshAPI import api


response = api.ai_image("orange cats is marrying")
#print(response)
with open("mukesh.jpg", 'wb') as f:
    f.write(response)
print("image generated successfully")


# pip install --upgrade MukeshAPI