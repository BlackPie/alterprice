$ = require 'jquery'
require 'jquery-form'


module.exports = class Form

    constructor: (options) ->
        @form = options.form
        @form.ajaxForm
            type: options.dataType or 'json'