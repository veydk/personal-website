from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.form
        
        # Get form data
        name = data.get('name', '')
        email = data.get('email', '')
        message = data.get('message', '')
        
        if not name or not email or not message:
            return jsonify({
                'success': False,
                'message': 'Please fill in all fields'
            }), 400
        
        # Email configuration
        to_email = "captainveyd@gmail.com"
        subject = f"New Contact Form Submission from {name}"
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Message body
        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email using Gmail SMTP
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                # You'll need to set up an App Password in your Gmail account
                server.login("captainveyd@gmail.com", "YOUR_APP_PASSWORD")
                server.send_message(msg)
            
            return jsonify({
                'success': True,
                'message': 'Message sent successfully!'
            })
            
        except Exception as e:
            return jsonify({
                'success': False,
                'message': f'Failed to send email: {str(e)}'
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error processing request: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
