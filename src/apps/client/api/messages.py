from django.utils.translation import ugettext_lazy as _

email_errors = {
    'blank': _('Заполните поле E-mail'),
    'invalid': _('E-mail не подходит'),
    'success': _('На ваш E-mail адрес выслана ссылка с подтверждением'),
    'blacklist': _('%s входит в список запрещенных доменов'),
    'not_exists': _('Пользователь с таким e-mail адресом не найден'),
    'already_exist': _('Пользователь с таким E-mail уже существует в системе'),
    'already_sent': _('На данный адрес уже было выслано сообщение. Попробуйте снова через несколько минут.')
}
