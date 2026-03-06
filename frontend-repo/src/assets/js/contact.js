/*-----------------------------------------------------------
 * Template Name    : RectCV - Personal Bootstrap 4 HTML Template
 * Author           : Narek Sukiasyan
 * Version          : 1.0.0
 * Created          : May 2020
 * File Description : Contact US script file for theme
 *--
 */

//Disable Form function
function contact_state(state) {
  if (state == "disable") {
    $("#contact-btn").removeClass("btn-loading");
    $("#contact-btn").removeClass("active");
    $("#contact-btn").addClass("disabled");

    $("#contact-form .form-control").each(function () {
      $(this).addClass("disabled");
    });
  }

  if (state == "loading") {
    $("#contact-btn").addClass("btn-loading");
  }
}

$(function () {
  this.sended = false;
  var that = this;

  var form = $("#contact-form"),
    successMessage = "Message Send",
    warningMessage = "Something wrong! Please try later";

  // Submit via AJAX to backend
  form.on("submit", function (event) {
    event.preventDefault();
    contact_state("loading");
    if (!that.sended) {
      var payload = {
        name: $("#name").val(),
        email: $("#email").val(),
        subject: $("#subject").val(),
        message: $("#text").val()
      };
      $.ajax({
        url: "/api/contact",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(payload),
        success: function (response) {
          if (response && response.ok) {
            custom_alert(successMessage, "success");
            contact_state("disable");
          } else {
            custom_alert(warningMessage, "error");
            contact_state("disable");
          }
        },
        error: function (response) {
          custom_alert(warningMessage, "error");
          contact_state("disable");
        }
      });
      that.sended = true;
    }
  });

  // Open mail client button
  $(document).on('click', '#open-mail-client', function (e) {
    e.preventDefault();
    var to = 'Bdby0706@gmail.com';
    var subject = $("#subject").val() || '';
    var name = $("#name").val() || '';
    var email = $("#email").val() || '';
    var message = $("#text").val() || '';
    var body = '';
    if (name) body += 'Nom: ' + name + '\n';
    if (email) body += 'Email: ' + email + '\n\n';
    if (message) body += message + '\n';
    var mailto = 'mailto:' + encodeURIComponent(to) + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    window.location.href = mailto;
  });
});
