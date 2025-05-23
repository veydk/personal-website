<?php
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = $_POST['name'] ?? '';
    $email = $_POST['email'] ?? '';
    $message = $_POST['message'] ?? '';

    if (!empty($name) && !empty($email) && !empty($message)) {
        $to = "captainveyd@gmail.com";
        $subject = "New Contact Form Submission from " . $name;
        $body = "Name: " . $name . "\n";
        $body .= "Email: " . $email . "\n";
        $body .= "Message: " . $message . "\n";

        $headers = "From: " . $email . "\r\n";
        $headers .= "Reply-To: " . $email . "\r\n";
        $headers .= "Content-type: text/plain; charset=UTF-8\r\n";

        if (mail($to, $subject, $body, $headers)) {
            echo json_encode(['success' => true, 'message' => 'Message sent successfully!']);
        } else {
            echo json_encode(['success' => false, 'message' => 'Failed to send message. Please try again later.']);
        }
    } else {
        echo json_encode(['success' => false, 'message' => 'Please fill in all fields.']);
    }
} else {
    echo json_encode(['success' => false, 'message' => 'Invalid request method.']);
}
?>
