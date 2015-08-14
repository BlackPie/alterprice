Number = require 'base/utils/Number'

template = (locals) =>

    if not locals.file_attached
        file = "В обработке"
    else
        file = "
            <!--<a href=\"#\" class=\"view\"><i class=\"icon-eye-grey\"></i></a>-->
            <a href=\"#{locals.invoice_file}\" target=\"_blank\" class=\"download\"><i class=\"icon-download-grey\"></i></a>
        "

    return "
        <td>Счет №#{locals.id}</td>
        <td>#{locals.created}</td>
        <td>#{file}</td>
    "


module.exports = template
