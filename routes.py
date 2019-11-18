from flask import Flask, render_template, redirect, request
from forms import MyForm
app = Flask(__name__)
app.secret_key = 'abcdefg'

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
	return render_template('index.html', the_title='This is my Homepage!', subtitle='This is a subtitle!')

@app.route('/symbol.html')
def symbol():
	return render_template('symbol.html', the_title='Tiger As Symbol')

@app.route('/myth.html')
def myth():
	return render_template('myth.html', the_title='Tiger in Myth and Legend')

@app.route('/encrypt', methods=('GET', 'POST'))
def encrypt():
	form = MyForm()
	if form.validate_on_submit():
		message = request.form.get('message')
		shift = int(request.form.get('shift'))
		encoded = ''

		for n in range(len(message)):
			if message[n].isalpha():
				if message[n].islower():
					num = ord(message[n])+shift
					if num > ord('z'):
						num -= 26
						print(f'new value: {num}')
						encoded += chr(num)
					else:
						encoded += chr(num)

				elif message[n].upper():
					num = ord(message[n])+shift
					if num > ord('Z'):
						num -= 26
						encoded = encoded + chr(num)
					else:
						encoded += chr(num)
				
			elif ord(message[n]) == 32:
				encoded += ' '
				
			else:
				encoded += message[n]

					

		return render_template('enc_message.html', encoded=encoded)
	return render_template('encrypt.html', form=form)

@app.route('/decrypt', methods=('GET', 'POST'))
def decrypt():
	form = MyForm()
	if form.validate_on_submit():
		message = request.form.get('message')
		shift = int(request.form.get('shift'))
		encoded = ''

		for n in range(len(message)):
			if message[n].isalpha():
				if message[n].islower():
					num = ord(message[n])-shift
					if num > ord('z'):
						num -= 26
						print(f'new value: {num}')
						encoded += chr(num)
					else:
						encoded += chr(num)

				elif message[n].upper():
					num = ord(message[n])-shift
					if num > ord('Z'):
						num -= 26
						encoded = encoded + chr(num)
					else:
						encoded += chr(num)
				
			elif ord(message[n]) == 32:
				encoded += ' '
				
			else:
				encoded += message[n]

							

		return render_template('enc_message.html', encoded=encoded)
	return render_template('decrypt.html', form=form)


@app.route('/success')
def success():
	return '<h1>Form submitted successfully!</h1>'


if __name__ == '__main__':
	app.run()
