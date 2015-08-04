Number = require 'base/utils/Number'

template = (locals) =>
    if not locals.sum
        locals.sum = 0
    return "<td><a href=\"/product/detail/#{locals.id}/\" target=\"_blank\">#{locals.name}</a></td>
    <th class=\"text-center\">#{locals.count}</th>
    <th class=\"text-center\">#{locals.sum}</th>"


module.exports = template