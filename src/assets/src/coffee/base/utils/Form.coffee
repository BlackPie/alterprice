$ = require 'jquery'
require 'jquery-form'


module.exports = class Form

    constructor: (options) ->
        @form = options.form

        @form.ajaxForm
            dataType: options.dataType or 'json'
            success: (formData, jqForm, options) =>

                console.log 'success'
            error:  (response) =>
                options.form.find('.error-text').remove()
                if response.responseJSON.status == 'fail'
                    for fieldName of response.responseJSON.errors
                        fieldWrapper = options.form.find("*[name=\"#{fieldName}\"]").closest '.field-wrapper'
                        fieldWrapper.find('.field-name').append "<span class=\"error-text\"> - #{response.responseJSON.errors[fieldName]}</span>"