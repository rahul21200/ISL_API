from flask import Flask, request, Response, jsonify
import os
app = Flask(__name__)

available_words = set()

for file in os.listdir('corpus_gifs'):
    available_words.add(file.split('.')[0])

mp = {chr(c): chr(c) for c in range(97, 123)}
mp['space'] = ' '
mp['hello'] = 'abarcayuiop'


@app.route('/get-gif', methods=['GET'])
def get_gif():
    final_output = []
    args = request.args
    text = args.get('text', default='', type=str)
    if text == '':
        jsonify({'error': 'Enter a text Input'})
    text_list = text.split()
    for word in text_list:
        if word in mp:
            final_output.append(mp[word])
        else:
            for c in word:
                final_output.append(mp[c])
        final_output.append(mp['space'])
        final_output.pop()
    return jsonify(final_output)


if __name__ == "__main__":
    app.run(debug=True)
