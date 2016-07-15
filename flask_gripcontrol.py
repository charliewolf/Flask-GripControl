from flask import current_app, _app_ctx_stack
from gripcontrol import GripPubControl


class GripControl(object):

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('GRIP_URI', 'http://localhost:5561/')

    def _create(self):
        return GripPubControl({'control_uri': current_app.config.get('GRIP_URI'), 'control_iss': current_app.config.get('GRIP_REALM'), 'key': current_app.config.get('GRIP_KEY')})

    def publish(self, *args, **kwargs):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'gripcontrol'):
                ctx.gripcontrol = self._create()
            return ctx.gripcontrol.publish(*args, **kwargs)
