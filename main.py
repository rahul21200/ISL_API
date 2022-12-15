from flask import Flask, request, Response, jsonify
import os

# import cloudinary
# import cloudinary.uploader
# import cloudinary.api
import json
# config = cloudinary.config(secure=True)


app = Flask(__name__)

# CLOUDINARY_URL = "cloudinary: // 668392227291592: xu62jmYnry7dRp54lBu2wEvxB2U@dkpwoyryv"


available_words = set()

mp = {}
count = 1
for file in os.listdir('corp'):
    count += 1
    print(file.split('_')[0])
    mp[file.split('_')[0]] = file
# print(mp, count)
# print()
# print(mp.keys())
# print()
# if 'm' in mp.keys():
#     print('hello world')
# else:
#     print('dkjns')


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
            final_output.append(
                'https://res.cloudinary.com/dkpwoyryv/image/upload/v1671104274/corpus/' + mp[word])
        else:
            for c in word:
                final_output.append(
                    'https://res.cloudinary.com/dkpwoyryv/image/upload/v1671104274/corpus/' + mp[c])
        # final_output.pop()
    return jsonify(final_output)


if __name__ == "__main__":
    app.run(debug=True)
