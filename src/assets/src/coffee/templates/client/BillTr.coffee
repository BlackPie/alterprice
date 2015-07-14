Number = require 'base/utils/Number'

template = (locals) =>

    return "
        <td>Счет №#{locals.id}</td>
        <td>#{locals.created}</td>
        <td>
            <a href=\"#\" class=\"view\"><i class=\"icon-eye-grey\"></i></a>
            <a href=\"#\" class=\"download\"><i class=\"icon-download-grey\"></i></a>
        </td>
    "


module.exports = template