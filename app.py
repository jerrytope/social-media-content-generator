from flask import Flask, render_template, request
import config
import ai_content

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())



@app.route('/product-description', methods=["GET", "POST"])
def productDescription():

    if request.method == 'POST':
        submission = request.form['productDescription']
        query = "Generate a detailed product description for {}".format(submission)
        openAIAnswer = ai_content.Openaiquary(query).replace("\n", "<br>")
        prompt = 'AI Suggestions for {} are:'.format(submission)
        #   = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    return render_template('product-description.html', **locals())



@app.route('/job-description', methods=["GET", "POST"])
def jobDescription():

    if request.method == 'POST':
        submission = request.form['jobDescription']
        query = "Generate a detailed job description for {}".format(submission)
        openAIAnswer = ai_content.Openaiquary(query).replace("\n", "<br>")
        prompt = 'AI Suggestions for {} are:'.format(submission)
    return render_template('job-description.html', **locals())



@app.route('/tweet-ideas', methods=["GET", "POST"])
def tweetIdeas():

    if request.method == 'POST':
        submission = request.form['tweetIdeas']

        part1 = ai_content.Openaiquary("Generate a detailed tweet idea for {}. \n".format(submission))
        part2 = ai_content.Openaiquary("Generate twitter hashtags for  {}".format(submission))
        query = "Generate a detailed tweet idea for {}".format(submission)
        openAIAnswer = """
        {}  {}
        <br>
        {}
        """.format(submission, part1, part2)
        prompt = 'AI Suggestions for {} are:'.format(submission)
    return render_template('tweet-ideas.html', **locals())



@app.route('/cold-emails', methods=["GET", "POST"])
def coldEmails():

    if request.method == 'POST':
        submission = request.form['coldEmails']
        query = "write a cold email to potential clients about {}".format(submission)
        openAIAnswerUnformatted = ai_content.Openaiquary(query)
        openAIAnswer = openAIAnswerUnformatted.replace("\n", "<br>")
        prompt = 'AI Suggestions for {} are:'.format(submission)



    return render_template('cold-emails.html', **locals())



@app.route('/social-media', methods=["GET", "POST"])
def socialMedia():

    if request.method == 'POST':
        submission = request.form['socialMedia']
        query = "Generate a detailed ad campaign for {}".format(submission)
        openAIAnswer = ai_content.Openaiquary(query).replace("\n", "<br>")
        prompt = 'AI Suggestions for {} are:'.format(submission)


    return render_template('social-media.html', **locals())


@app.route('/business-pitch', methods=["GET", "POST"])
def businessPitch():

    if request.method == 'POST':
        submission = request.form['businessPitch']
        query = "Generate a detailed business pitch for {}".format(submission)
        openAIAnswer = ai_content.Openaiquary(query).replace("\n", "<br>")
        prompt = 'AI Suggestions for {} are:'.format(submission)
    return render_template('business-pitch.html', **locals())


@app.route('/video-ideas', methods=["GET", "POST"])
def videoIdeas():

    if request.method == 'POST':
        submission = request.form['videoIdeas']
        query = "Generate a detailed explaination for {}".format(submission)
        openAIAnswer = ai_content.Openaiquary(query).replace("\n", "<br>")
        prompt = 'AI Suggestions for {} are:'.format(submission)
    return render_template('video-ideas.html', **locals())


@app.route('/video-description', methods=["GET", "POST"])
def videoDescription():

    if request.method == 'POST':
        submission = request.form['videoDescription']
        query = "Generate a detailed video Description for {}".format(submission)
        openAIAnswer = ai_content.Openaiquary(query).replace("\n", "<br>")
        prompt = 'AI Suggestions for {} are:'.format(submission)
    return render_template('video-description.html', **locals())










if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
