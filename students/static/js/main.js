function initJournal() {
  var indicator = $('#ajax-progress-indicator');

  $('.day-box input[type="checkbox"]').click(function(event){
    var box = $(this);
    $.ajax(box.data('url'), {
      'type': 'POST',
      'async': true,
      'dataType': 'json',
      'data': {
        'pk': box.data('student-id'),
        'date': box.data('date'),
        'present': box.is(':checked') ? '1': '',
        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
      },
      'beforeSend': function(xhr, settings){
        indicator.show();
      },
      'error': function(xhr, status, error){
        alert(error);
        indicator.hide();
      },
      'success': function(data, status, xhr){
        indicator.hide();
      }
    });
  });
}

function initGroupSelector() {
  // look up select element with groups and attach our even handler
  // on field "change" event
  $('#group-selector select').change(function(event) {
    // get value of currently selected group option
    var group = $(this).val();

    if (group) {
      // set cookie with expiration date 1 year since now;
      // cookie creation function takes period in days
      $.cookie('current_group', group, {'path': '/', 'expires': 365});
    } else {
      // otherwise we delete the cookie
      $.removeCookie('current_group', {'path': '/'});
    }

    // and reload a page
    location.reload(true);

    return true;
  });
}

function initDateFields() {
  $('input.dateinput').datetimepicker({
    format: 'YYYY-MM-DD',
    locale: 'uk'
  }).on('dp.hide', function(event){
    $(this).blur();
  });
}

function initCreateStudentPage() {
    $( 'a#student-create-form-link' ).click( function(event){
        var modal = $( '#myModal2' );
        modal.modal( 'show' );

        return false;
    });
}

function initCreateStudentPage() {
  $('a#student-create-form-link').click(function(event){
    var link = $(this);
    $.ajax({
      'url': link.attr('href'),
      'dataType': 'html',
      'type': 'get',
      'success': function(data, status, xhr){
        // check if we got successfull response from the server
        if (status != 'success') {
          alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
          return false;
        }

        // update modal window with arrived content from the server
        var modal = $('#myModal2'),
          html = $(data), form = html.find('#content-column form');
        modal.find('.modal-title').html(html.find('#content-column h2').text());
        modal.find('.modal-body').html(form);

        // // setup and show modal window finally
        // modal.modal('show');

        // init our edit form
        // initEditStudentForm(form, modal);
        initCreateStudentForm(form, modal);

        // setup and show modal window finally
        modal.modal({
          'keyboard': false,
          'backdrop': false,
          'show': true
        });
      },
      'error': function(){
          alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
          return false
      }
    });

    return false;
  });
}

function initCreateStudentForm(form, modal) {
  // attach datepicker
  initDateFields();

  // close modal window on Cancel button click
  form.find('input[name="cancel_button"]').click(function(event){
    modal.modal('hide');
    return false;
  });

  // make form work in AJAX mode
  form.ajaxForm({
    'dataType': 'html',
    'error': function(){
        alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
        return false;
    },

    'beforeSend': function(xhr, settings){
        // indicator.show();
        $("#submit-id-add_button").prop("disabled", true);
        $("#submit-id-cancel_button").prop("disabled", true);
        $('.form-horizontal').html('<img id="loader-img" alt="" src="http://adrian-design.com/images/loading.gif" width="100" height="100" align="center" />', 3000);
        // setTimeout(function () {
        //   $('#content').html('<img id="loader-img" alt=""
        //     src="http://adrian-design.com/images/loading.gif"
        //     width="100" height="100" align="center" />').addClass('border');
        //                       }, 3000);
        // alert('GO!');
      },
    'error': function(xhr, status, error){
        alert(error);
        // indicator.hide();
    },

    'success': function(data, status, xhr) {
        // alert('STOP');

      var html = $(data), newform = html.find('#content-column form');

      // copy alert to modal window
      modal.find('.modal-body').html(html.find('.alert'));

      // copy form to modal if we found it in server response
      if (newform.length > 0) {
        modal.find('.modal-body').append(newform);

        // initialize form fields and buttons
        initCreateStudentForm(newform, modal);
      } else {
        // if no form, it means success and we need to reload page
        // to get updated students list;
        // reload after 2 seconds, so that user can read success message
        setTimeout(function(){location.reload(true);}, 500);
      }
      $("#submit-id-add_button").prop("disabled", false);
    }
  });
}

function initEditStudentPage() {
  $('a.student-edit-form-link').click(function(event){
    var link = $(this);
    $.ajax({
      'url': link.attr('href'),
      'dataType': 'html',
      'type': 'get',
      'success': function(data, status, xhr){
        // check if we got successfull response from the server
        if (status != 'success') {
          alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
          return false;
        }

        // update modal window with arrived content from the server
        var modal = $('#myModal'),
          html = $(data), form = html.find('#content-column form');
        modal.find('.modal-title').html(html.find('#content-column h2').text());
        modal.find('.modal-body').html(form);

        // init our edit form
        initEditStudentForm(form, modal);

        // setup and show modal window finally
        modal.modal({
          'keyboard': false,
          'backdrop': false,
          'show': true
        });
      },
      'error': function(){
          alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
          return false
      }
    });

    return false;
  });
}

function initEditStudentForm(form, modal) {
  // attach datepicker
  initDateFields();

  // close modal window on Cancel button click
  form.find('input[name="cancel_button"]').click(function(event){
    modal.modal('hide');
    return false;
  });

  // make form work in AJAX mode
  form.ajaxForm({
    'dataType': 'html',
    'error': function(){
        alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
        return false;
    },
    'success': function(data, status, xhr) {
      var html = $(data), newform = html.find('#content-column form');

      // copy alert to modal window
      modal.find('.modal-body').html(html.find('.alert'));

      // copy form to modal if we found it in server response
      if (newform.length > 0) {
        modal.find('.modal-body').append(newform);

        // initialize form fields and buttons
        initEditStudentForm(newform, modal);
      } else {
        // if no form, it means success and we need to reload page
        // to get updated students list;
        // reload after 2 seconds, so that user can read success message
        setTimeout(function(){location.reload(true);}, 500);
      }
    }
  });
}


$(document).ready(function(){
  initJournal();
  initGroupSelector();
  initDateFields();
  initEditStudentPage();
  initCreateStudentPage();
});
