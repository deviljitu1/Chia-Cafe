<?php

  // Basic token security check
  if( empty( $_POST['token'] ) || $_POST['token'] != 'FsWga4&@f6aw' ){
    echo '<div class="cf-error"><i class="fas fa-times-circle"></i> Security check failed. Please reload and try again.</div>';
    exit;
  }

  // Sanitize inputs
  $name    = htmlspecialchars( strip_tags( $_POST['name'] ) );
  $from    = htmlspecialchars( strip_tags( $_POST['email'] ) );
  $phone   = htmlspecialchars( strip_tags( $_POST['phone'] ) );
  $subject = htmlspecialchars( strip_tags( $_POST['subject'] ) );
  $message = htmlspecialchars( strip_tags( $_POST['message'] ) );

  // === CHANGE THIS EMAIL to the cafe's real email ===
  $to = 'chiacafe.in@gmail.com';

  // Email headers
  $headers  = "MIME-Version: 1.0\r\n";
  $headers .= "Content-type: text/html; charset=UTF-8\r\n";
  $headers .= "From: Chia Cafe Website <noreply@chiacafe.in>\r\n";
  $headers .= "Reply-To: $from\r\n";

  // Email subject line
  $email_subject = "[Chia Cafe Contact] $subject — from $name";

  // Email body (HTML)
  $body = '
  <!DOCTYPE html>
  <html>
  <head><meta charset="UTF-8"><style>
    body { font-family: Arial, sans-serif; color: #333; background: #f5f5f5; margin:0; padding:0; }
    .wrap { max-width: 580px; margin: 30px auto; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.08); }
    .header { background: #0E4935; padding: 28px 32px; }
    .header h1 { color: #fff; font-size: 22px; margin: 0; }
    .header p { color: #a8d4bb; margin: 6px 0 0; font-size: 14px; }
    .body { padding: 28px 32px; }
    .field { margin-bottom: 16px; border-bottom: 1px solid #f0f0f0; padding-bottom: 14px; }
    .field:last-child { border-bottom: none; }
    .label { font-size: 12px; font-weight: bold; color: #84A57B; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
    .value { font-size: 15px; color: #222; }
    .msg-box { background: #f8fdf6; border-left: 4px solid #84A57B; padding: 12px 16px; border-radius: 4px; white-space: pre-wrap; }
    .footer { background: #f8f8f8; padding: 16px 32px; font-size: 12px; color: #aaa; text-align: center; border-top: 1px solid #eee; }
  </style></head>
  <body>
    <div class="wrap">
      <div class="header">
        <h1>🌿 New Message — Chia Cafe</h1>
        <p>You received a new contact form submission from your website.</p>
      </div>
      <div class="body">
        <div class="field"><div class="label">👤 Name</div><div class="value">'.ucwords($name).'</div></div>
        <div class="field"><div class="label">📧 Email</div><div class="value"><a href="mailto:'.($from).'" style="color:#0E4935;">'.($from).'</a></div></div>
        <div class="field"><div class="label">📞 Phone</div><div class="value">'.( $phone ? $phone : '—' ).'</div></div>
        <div class="field"><div class="label">📌 Subject</div><div class="value">'.$subject.'</div></div>
        <div class="field">
          <div class="label">💬 Message</div>
          <div class="msg-box">'.nl2br($message).'</div>
        </div>
      </div>
      <div class="footer">This email was sent from the contact form on chiacafe.in &nbsp;|&nbsp; Reply directly to this email to reach '.$name.'</div>
    </div>
  </body>
  </html>';

  // Send the email
  $sent = mail( $to, $email_subject, $body, $headers );

  if( $sent ){
    echo '<div class="cf-success"><i class="fas fa-check-circle"></i><div><strong>Message sent!</strong><br>Thank you ' . ucfirst($name) . ', we\'ll get back to you soon 🌿</div></div>';
  } else {
    echo '<div class="cf-error"><i class="fas fa-exclamation-circle"></i><div><strong>Something went wrong.</strong><br>Please call us at <a href="tel:09155515655">091555 15655</a> or try again.</div></div>';
  }

?>
