from flask import Flask, render_template, request, send_file
import tbcrawl
import tbimg
import StringIO

app = Flask(__name__)

@app.route("/tb-image-generator", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        errors = []
        url = request.form['url']
        print 'getting html from %s' % url
        if url:
            try:
                html = tbcrawl.fetch_page(url)
            except Exception as e:
                errors.append(e.message)
                return render_template('index.html', errors=errors)

            print 'getting logo'
            logo = tbcrawl.get_logo(html)
            print 'getting bk'
            bk = tbcrawl.get_background(html)
            if logo is None:
                errors.append('logo not found')
            if bk is None:
                errors.append('background not found')
            if errors:
                return render_template('index.html', errors=errors)

            try:
                print 'building image'
                img = tbimg.build_image(bk, logo)
                img_io = StringIO.StringIO()
                img.save(img_io, 'JPEG')
                img_io.seek(0)
            except Exception as e:
                errors.append(e.message)
                return render_template('index.html', errors=errors)

            return send_file(img_io,
                             as_attachment=True,
                             attachment_filename='out.png',
                             mimetype='image/jpeg')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
