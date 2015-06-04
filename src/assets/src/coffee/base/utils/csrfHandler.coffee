$ = require 'jquery'
require 'jquery.cookie'


csrfSafeMethod = (method) ->
    # these HTTP methods do not require CSRF protection
    return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method)


module.exports = csrfHandler = (xhr, settings) ->
    if not csrfSafeMethod(settings.type) && not this.crossDomain
        xhr.setRequestHeader "X-CSRFToken", $.cookie('csrftoken')