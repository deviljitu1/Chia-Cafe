function valid_datas( f ) {

  // Clear previous status
  jQuery('#form_status').html('');

  // Validate Name
  if ( f.name.value.trim() === '' ) {
    jQuery('#form_status').html('<span class="wrong"><i class="fas fa-exclamation-circle"></i> Please enter your name.</span>');
    highlight( f.name );
    return false;
  }

  // Validate Email
  var emailReg = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if ( f.email.value.trim() === '' || !emailReg.test(f.email.value.trim()) ) {
    jQuery('#form_status').html('<span class="wrong"><i class="fas fa-exclamation-circle"></i> Please enter a valid email address.</span>');
    highlight( f.email );
    return false;
  }

  // Validate Subject (dropdown)
  if ( f.subject.value === '' ) {
    jQuery('#form_status').html('<span class="wrong"><i class="fas fa-exclamation-circle"></i> Please select a subject.</span>');
    highlight( f.subject );
    return false;
  }

  // Validate Message
  if ( f.message.value.trim() === '' ) {
    jQuery('#form_status').html('<span class="wrong"><i class="fas fa-exclamation-circle"></i> Please write a message before sending.</span>');
    highlight( f.message );
    return false;
  }

  // All good — submit via AJAX
  jQuery.ajax({
    url: 'mail.php',
    type: 'POST',
    data: jQuery('form#chiacafe-contact').serialize(),
    complete: function(data) {
      jQuery('#form_status').html(data.responseText);
      jQuery('#chiacafe-contact').find('input, textarea, select, button').prop('disabled', false).css({ opacity: 1 });
      jQuery('#chiacafe-contact').slideUp(400);
    }
  });

  // Show loading state
  jQuery('#form_status').html('<span class="loading"><i class="fas fa-spinner fa-spin"></i> Sending your message…</span>');
  jQuery('#chiacafe-contact').find('input, textarea, select, button').prop('disabled', true).css({ opacity: 0.5 });

  return false;
}

function highlight( field ) {
  jQuery('#chiacafe-contact').find('input, textarea, select').css('border-color', '');
  jQuery(field).css('border-color', '#e74c3c');
  jQuery(field).focus();
}