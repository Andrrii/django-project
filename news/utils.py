class MyTestMixin(object):
    mixin_str_up = ''
    def get_up(self):
        return self.mixin_str_up.upper()