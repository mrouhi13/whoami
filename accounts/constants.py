from django.utils.translation import ugettext_lazy as _
from djoser.constants import Messages


class CustomMessages(Messages):
    SUCCESS_PROFILE_UPDATE = _('پروفایل شما به‌روز شد.')
    INVALID_CREDENTIALS_ERROR = _('اطلاعات وارد شده صحیح نیست.')
    INACTIVE_ACCOUNT_ERROR = _('این کاربر غیرفعال / حذف شده است.')
    INVALID_TOKEN_ERROR = _('نشان شما مورد تایید نیست.')
    EXPIRED_TOKEN_ERROR = _('نشان شما منقضی شده است.')
    INVALID_UID_ERROR = _('شناسه‌ی کاربر مورد تایید نیست.')
    STALE_TOKEN_ERROR = _('نشان شما مورد تایید نیست.')
    PASSWORD_MISMATCH_ERROR = _('گذرواژه‌ها یکسان نیست.')
    USERNAME_MISMATCH_ERROR = _('{0}‌ها یکسان نیست.')
    INVALID_PASSWORD_ERROR = _('گذرواژه صحیح نیست.')
    EMAIL_NOT_FOUND = _('کاربری با این ایمیل پیدا نشد.')
    EMAIL_UNIQUE_ERROR = _('این ایمیل قبلا ثبت شده است.')
    CANNOT_CREATE_USER_ERROR = _('نمی‌توان حساب جدید ایجاد کرد.')
    USER_WITHOUT_EMAIL_FIELD_ERROR = _('مدل کاربر فیلد ایمیل ندارد.')
    IS_BLANK = _('{0} وارد نشده است.')
    IS_INVALID = _('{0} صحیح نیست.')
