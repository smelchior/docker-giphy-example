from flask import Flask, render_template, request, make_response, redirect
import giphypop, re, socket

g = giphypop.Giphy()

version ='2.0'
hostname = socket.gethostname()

print "Starting web container %s" % hostname

app = Flask(__name__)

@app.route('/')
def index():
    host_header = request.headers['Host']
    # extract animal from hostname, very pretty
    reg = re.search('^web-(.+)-(.+)\.(.+)\.(.+)', host_header)
    if reg:
      animal = reg.group(1)
    else:
      animal = 'dog'
    g_results = g.random_gif(tag=animal)
    url = g_results.fixed_height.url
    return render_template('pets.html', url=url, hostname=hostname, version=version, host= animal)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
